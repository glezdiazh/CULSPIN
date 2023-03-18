#!/usr/bin/env python
# -*- coding: cp1252 -*- 
# main window

'''
Created on 06/05/2009

@author: Chachy
'''

#===============================================================================
# Importar modulos necesarios
#===============================================================================
import wx
import FiltrosSeq_v_1_0_imp
import BuildSpiral_v_1_0_imp
import Grid_v_1_0_imp
import HelpHtml_v_1_0_imp
import SpiralGraph_v_1_0_imp
import About_v_1_0_imp
import CalcIndices_v_1_0_imp
import numpy
import math
import os, sys

orig_dir = os.getcwd() + "\\"


#===============================================================================
# Clase MySplash para crear la ventana de inicio del programa
#===============================================================================
class MySplash( wx.SplashScreen ):
    def __init__( self, parent, duration = 3000 ):
        # Imagen que va a aparecer en la ventana de presentacion
        image_file = orig_dir + 'images/inicio.jpg'
        bmp = wx.Bitmap( image_file )
        # ventana de presentación
        wx.SplashScreen( bmp,
                        wx.SPLASH_CENTRE_ON_PARENT | wx.SPLASH_TIMEOUT,
                        duration, parent, wx.ID_ANY )

#===============================================================================
# Clase MyMenu para crear el menu y barra de estado
#===============================================================================
class MyMenu( wx.Frame ):
    def __init__( self, parent, id, title ):
        wx.Frame.__init__( self, parent, id, title, wx.DefaultPosition, wx.Size( 970, 650 ),
                          style = wx.CAPTION | wx.SYSTEM_MENU | wx.MINIMIZE_BOX | wx.CLOSE_BOX )

    #===============================================================================
    #   Inicializar algunas variables globales
    #===============================================================================
        self.raiz_images = orig_dir
        self.input_file_names = []
        self.input_file_paths = []
        self.lista_openfile_wildcard = []
        self.lista_openfile_style = []
        self.input_file_csv = ''
        self.inputf = ''
        self.data = []
        self.countgauge = 0
        self.data_numerica = []
        self.lista_casos_orig = []
        self.lista_casos_names_orig = []
        self.lista_casos_sequences_orig = []
        self.lista_casos_clases_orig = []
        self.lista_casos = []
        self.lista_casos_view = []
        self.lista_casos_names = []
        self.lista_casos_sequences = []
        self.lista_casos_clases = []
        self.si_fastaprotein = False
        self.si_casos_cargados = False
        self.si_graph_build = False
        self.si_indices_calculed = False
        self.lista_casos_selected = []
        self.lista_names_selected = []
        self.lista_sequences_selected = []
        self.lista_clases_selected = []
        self.lista_items_selected = []
        self.codes_letras = ['A', 'C', 'D', 'E', 'F',
                             'G', 'H', 'I', 'K', 'L',
                             'M', 'N', 'P', 'Q', 'R',
                             'S', 'T', 'V', 'W', 'Y']
        self.codes_forfastaprot = {'A':'B', 'C':'J', 'D':'O', 'E':'O', 'F':'B',
                                   'G':'B', 'H':'U', 'I':'B', 'K':'U', 'L':'B',
                                   'M':'B', 'N':'J', 'P':'B', 'Q':'J', 'R':'U',
                                   'S':'J', 'T':'J', 'V':'B', 'W':'J', 'Y':'J'}
        self.ct_linea1 = []
        self.ct_linea2 = []
        self.ct_bloque_coord_atom = []
        self.ct_bloque_conectivity = []
        self.lista_ulam_casos = []
        self.lista_grG_casos = []
        self.indices_clases_gnomones_casos = []
        self.indices_clases_globales_casos = []
        self.indices_gnomones_casos = []
        self.indices_calculated = []
        self.resultados = ''
        self.view_dimen = ''
        self.visor_spiral_graph = ''
        self.indices_tipo = 0

    #===============================================================================
    #   Tipos de letra a utilizar
    #===============================================================================
        self.font11RIBUn = wx.Font( 11, wx.ROMAN, wx.ITALIC, wx.BOLD, underline = True )
        self.font11RIB = wx.Font( 11, wx.ROMAN, wx.ITALIC, wx.BOLD )
        self.font10RNB = wx.Font( 10, wx.ROMAN, wx.NORMAL, wx.BOLD )
        self.font10normal = wx.Font( 10, wx.ROMAN, wx.NORMAL, wx.NORMAL )
        self.font11normal = wx.Font( 11, wx.ROMAN, wx.NORMAL, wx.NORMAL )

    #===============================================================================
    #   Crear el Notebook donde se van a poner todos los botones, bitmaps, listbox, etc
    #===============================================================================
        self.notebook = wx.Notebook( self, 1000, size = ( 945, 550 ), style = wx.BK_DEFAULT )
        self.notebook.SetBackgroundColour( wx.Colour( 160, 160, 255, 250 ) )
        self.notebook.SetFont( self.font11RIBUn )
        
        self.notebook_pane_1 = wx.Panel( self.notebook, 1001 )
        
        self.notebook.AddPage( self.notebook_pane_1, "Options" )
        self.notebook.Enable( True )

    #===============================================================================
    #    Crear la barra del Menu con todos los submenus y separadores
    #===============================================================================
        self.menuBar = wx.MenuBar() # Instacia de la barra de menu

        #===============================================================================
        #    Menu File
        #===============================================================================
        self.opcion_file = wx.Menu() # Instancia de la opcion File de la barra de menu

        self.opcion_file_open = wx.MenuItem( self.opcion_file, 11, '&Open\tCtrl+O', 'Open input file' ) # Construye item open
        self.opcion_file_open.SetBitmap( wx.Bitmap( self.raiz_images + 'images/open.png' ) ) # Asigna imagen al item open
        self.opcion_file.AppendItem( self.opcion_file_open ) # Adiciona o vincula el item a la opcion file de la barra de menu

        self.opcion_file_reload = wx.MenuItem( self.opcion_file, 12, '&Reload sequences\tCtrl+R', 'Reload the originals sequences of letters' ) # Construye item reload
        self.opcion_file_reload.SetBitmap( wx.Bitmap( self.raiz_images + 'images/reload.png' ) ) # Asigna imagen al item reload
        self.opcion_file.AppendItem( self.opcion_file_reload ) # Adiciona o vincula el item a la opcion file de la barra de menu

        self.opcion_file.AppendSeparator() # Adicionar un separador de items en la opcion file

        self.opcion_file_mkcopy = wx.Menu()
        self.opcion_file_mkcopy_origen = wx.MenuItem( self.opcion_file_mkcopy, 13001, 'Original sequences', 'Make a copy of the original sequences in .txt file' )
        self.opcion_file_mkcopy_origen.SetBitmap( wx.Bitmap( self.raiz_images + 'images/makecopy.png' ) )
        self.opcion_file_mkcopy.AppendItem( self.opcion_file_mkcopy_origen )
        self.opcion_file_mkcopy.AppendSeparator()
        self.opcion_file_mkcopy_studied = wx.MenuItem( self.opcion_file_mkcopy, 13002, 'Studied sequences', 'Make a copy of the studied sequences in .txt file' )
        self.opcion_file_mkcopy_studied.SetBitmap( wx.Bitmap( self.raiz_images + 'images/makecopy.png' ) )
        self.opcion_file_mkcopy.AppendItem( self.opcion_file_mkcopy_studied )
        self.opcion_file.AppendMenu( 13, '&Make a copy of', self.opcion_file_mkcopy, 'Make a copy of sequences obtained by means of numeric data encoding' )

        self.opcion_file_export_spiral = wx.Menu()
        self.opcion_file_export_spiralct = wx.MenuItem( self.opcion_file_export_spiral, 14001, 'As *.ct files', 'Export spiral graphs as *.ct files' )
        self.opcion_file_export_spiralct.SetBitmap( wx.Bitmap( self.raiz_images + 'images/exportar.png' ) )
        self.opcion_file_export_spiral.AppendItem( self.opcion_file_export_spiralct )
        self.opcion_file_export_spiral.AppendSeparator()
        self.opcion_file_export_spiralnet = wx.MenuItem( self.opcion_file_export_spiral, 14002, 'As *.net files', 'Export spiral graphs as *.net files' )
        self.opcion_file_export_spiralnet.SetBitmap( wx.Bitmap( self.raiz_images + 'images/exportar.png' ) )
        self.opcion_file_export_spiral.AppendItem( self.opcion_file_export_spiralnet )
        self.opcion_file.AppendMenu( 14, '&Export Graph', self.opcion_file_export_spiral, 'Export spiral graphs as *.net or *.net files' )

        self.opcion_file_save_indices = wx.MenuItem( self.opcion_file, 15, '&Save Indices\tCtrl+I', 'Save indices in *.txt file' )
        self.opcion_file_save_indices.SetBitmap( wx.Bitmap( self.raiz_images + 'images/save.png' ) )
        self.opcion_file.AppendItem( self.opcion_file_save_indices )

        self.opcion_file.AppendSeparator() # Adicionar un separador de items en la opcion file

        self.opcion_file_quit = wx.MenuItem( self.opcion_file, 19, '&Quit\tCtrl+X', 'Quit of Application' )
        self.opcion_file_quit.SetBitmap( wx.Bitmap( self.raiz_images + 'images/gtk-quit.png' ) )
        self.opcion_file.AppendItem( self.opcion_file_quit )

        self.menuBar.Append( self.opcion_file, "&File" ) # Adiciona o vincula la opcion file a la barra de menu

        #===============================================================================
        #    Menu Submit
        #===============================================================================
        self.opcion_submit = wx.Menu() # Instancia de la opcion submit de la barra de menu

        self.opcion_submit_build = wx.MenuItem( self.opcion_submit, 21, '&Build Spiral\tCtrl+B',
                                            'Build the Ulam-Spiral from selected sequences' )
        self.opcion_submit_build.SetBitmap( wx.Bitmap( self.raiz_images + 'images/build.png' ) )
        self.opcion_submit.AppendItem( self.opcion_submit_build )

        self.opcion_submit.AppendSeparator() 

        self.opcion_submit_calculate = wx.MenuItem( self.opcion_submit, 22, 'Calculate &Indices\tCtrl+I',
                                            'Calculate indices from spiral graph of each selected sequence' )
        self.opcion_submit_calculate.SetBitmap( wx.Bitmap( self.raiz_images + 'images/calcula.jpg' ) )
        self.opcion_submit.AppendItem( self.opcion_submit_calculate )

        self.menuBar.Append( self.opcion_submit, "&Submit" ) # Adiciona o vincula la opcion tools a la barra de menu

        #===============================================================================
        #    Menu View
        #===============================================================================
        self.opcion_view = wx.Menu() # Instancia de la opcion View de la barra de menu

        self.opcion_view_vselectcodes = wx.MenuItem( self.opcion_view, 31, '&View a Graph\tCtrl+V',
                                            'View Spiral Graph of one converted sequence' )
        self.opcion_view_vselectcodes.SetBitmap( wx.Bitmap( self.raiz_images + 'images/spiral.png' ) )
        self.opcion_view.AppendItem( self.opcion_view_vselectcodes )

        self.menuBar.Append( self.opcion_view, "&View" ) # Adiciona o vincula la opcion view a la barra de menu

        #===============================================================================
        #    Menu Help
        #===============================================================================
        self.opcion_help = wx.Menu() # Instancia de la opcion Help de la barra de menu

        self.opcion_help_contents = wx.MenuItem( self.opcion_help, 91, '&Help\tCtrl+H', 'Help contents' )
        self.opcion_help_contents.SetBitmap( wx.Bitmap( self.raiz_images + 'images/help.png' ) )
        self.opcion_help.AppendItem( self.opcion_help_contents )

        self.opcion_help.AppendSeparator() # Adicionar un separador de items en la opcion Help

        self.opcion_help_about = wx.MenuItem( self.opcion_help, 92, 'A&bout\tCtrl+A', 'About CULSPIN V-1.0' )
        self.opcion_help_about.SetBitmap( wx.Bitmap( self.raiz_images + 'images/about.png' ) )
        self.opcion_help.AppendItem( self.opcion_help_about )

        self.menuBar.Append( self.opcion_help, "&Help" ) # Adiciona o vincula la opcion help a la barra de menu

        #===============================================================================
        #    Hace instacia de la barra de menu para hacerla visible
        #===============================================================================
        self.SetMenuBar( self.menuBar ) # Asocia la barra de menu con la frame y pasa a ser una propiedad de esta

        #===============================================================================
        #    Desactivar opciones de menu que no se pueden usar por el momento
        #===============================================================================
        self.menuBar.Enable( 12, False ) # Desactiva opcion file/reload hasta que se modifique el contenido de la lista inicial
        self.menuBar.Enable( 13, False ) # Desactiva opcion file/make copy hasta se obtengan secuencias de letras a partir de datos numericos
        self.menuBar.Enable( 14, False ) # Desactiva opcion file/export hasta que hayan secuencias convertidas en espirales
        self.menuBar.Enable( 15, False ) # Desactiva opcion file/save indices hasta que hayan indices calculados
        self.menuBar.Enable( 21, False ) # Desactiva opcion submit/build hasta que hayan secuencias seleccionadas
        self.menuBar.Enable( 22, False ) # Desactiva opcion submit/calculate hasta que hayan secuencias seleccionadas
        self.menuBar.Enable( 31, False ) # Desactiva opcion view/view spiral graph hasta que hayan secuencias convertidas

        #===============================================================================
        #    Crear Barra de estado y colocar en ella la bienvenida
        #===============================================================================
        self.CreateStatusBar() # Instancia de la barra de estado
        self.StatusBar.SetFieldsCount( 3 )
        self.StatusBar.SetStatusWidths( [-8, -1, -4] )
        self.SetStatusText( "Welcome to CULSPIN V-1.0", 0 ) # Asigar el texto Welcome ... a la barra de estado

        #===============================================================================
        #    Eventos que redireccionan a los metodos asociados a cada item de las opciones del la barra de menu
        #===============================================================================
        self.Bind( wx.EVT_MENU, self.OnOpenFile, id = 11 )
        self.Bind( wx.EVT_MENU, self.OnReloadSeq, id = 12 )
        self.Bind( wx.EVT_MENU, self.OnMakeCopyOrigen, id = 13001 )
        self.Bind( wx.EVT_MENU, self.OnMakeCopyStudied, id = 13002 )
        self.Bind( wx.EVT_MENU, self.OnExportSpiralCt, id = 14001 )
        self.Bind( wx.EVT_MENU, self.OnExportSpiralNet, id = 14002 )
        self.Bind( wx.EVT_MENU, self.OnSaveFilesIndices, id = 15 )
        self.Bind( wx.EVT_MENU, self.OnQuit, id = 19 )
        self.Bind( wx.EVT_MENU, self.OnBuild, id = 21 )
        self.Bind( wx.EVT_MENU, self.OnCalculate, id = 22 )
        self.Bind( wx.EVT_MENU, self.OnView, id = 31 )
        self.Bind( wx.EVT_MENU, self.OnHelp, id = 91 )
        self.Bind( wx.EVT_MENU, self.OnAbout, id = 92 )

    #===============================================================================
    #   Grupo formato de fichero de entrada
    #===============================================================================
        #===============================================================================
        #    Crear el Box con los formatos de fichero que lee el programa
        #===============================================================================
        self.format_inputfile_staticbox = wx.StaticBox( self.notebook_pane_1, -1,
                                                       'Input file(s) format', ( 15, 20 ), ( 580, 210 ) )
        self.format_inputfile_staticbox.SetFont( self.font11RIB ) # letra 11 Roman italica negrita

        #===============================================================================
        #    Formato by rows
        #===============================================================================
        self.lista_formato_inputf = ['Text file by rows:     Case Name ',
                                     'Text file by columns:                   Case Name',
                                     'Text file in FASTA format',
                                     'Text or CSV file(s) of MS data  ( two colum by case, m/z and I )']
        self.rbformat_textby_row = wx.RadioButton( self.notebook_pane_1, 100, self.lista_formato_inputf[0],
                                                    ( 30, 50 ), ( 188, 20 ), style = wx.RB_GROUP ) # crea el encabezado del formato comboBox
        self.rbformat_textby_row.SetFont( self.font10RNB )
        self.formato_inputf = 0

        self.lista_formatos_sequences_byrow = ['AGCTTCCGAAGTCAGCAGCTT...  (Letter Sequence)',
                                               '12.00 1.02 3.17 80.23 0.77 114.78...  (Numeric Sequence)']
        self.formato_sequences = 0
        self.comboBox_byrow = wx.ComboBox( self.notebook_pane_1, 101,
                                          self.lista_formatos_sequences_byrow[0],
                                          ( 218, 48 ), ( 360, -1 ), self.lista_formatos_sequences_byrow,
                                          wx.CB_DROPDOWN | wx.CB_READONLY )
        self.comboBox_byrow.SetFont( self.font10RNB )

        #===============================================================================
        #    Formato by columns
        #===============================================================================
        self.rbformat_textby_col = wx.RadioButton( self.notebook_pane_1, 110, self.lista_formato_inputf[1],
                                                    ( 30, 90 ), ( 248, 20 ) ) # crea el encabezado del formato comboBox
        self.rbformat_textby_col.SetFont( self.font10RNB )
        self.lista_formatos_sequences_bycol = ['   Letter Sequence',
                                               'Numeric Sequence']
        self.comboBox_bycol = wx.ComboBox( self.notebook_pane_1, 111,
                                          self.lista_formatos_sequences_bycol[0],
                                          ( 175, 110 ), ( 138, -1 ), self.lista_formatos_sequences_bycol,
                                          wx.CB_DROPDOWN | wx.CB_READONLY )
        self.comboBox_bycol.SetFont( self.font10RNB )
        self.comboBox_bycol.Enable( False )

        #===============================================================================
        #    Formato Fasta
        #===============================================================================
        self.rbformat_tex_fasta = wx.RadioButton( self.notebook_pane_1, 120, self.lista_formato_inputf[2],
                                                    ( 30, 150 ), ( 162, 20 ) ) # crea el encabezado del formato comboBox
        self.rbformat_tex_fasta.SetFont( self.font10RNB )

        #===============================================================================
        #    Check box que permite seleccionar si es un fichero fasta de una proteina
        #===============================================================================
        self.checkbox_fastaprotein = wx.CheckBox( self.notebook_pane_1, 121 , 'Protein (output as four charge/polarity classes)',
                                               ( 200, 152 ), ( 280, -1 ) ) # Construye el checkbox protein
        self.checkbox_fastaprotein.SetFont( self.font10RNB ) # letra 11 Roman italica negrita
        self.checkbox_fastaprotein.Enable( False )
        self.si_fastaprotein = False

        #------------------------------------------------------------------------------ 
        #Formato Mass Spectre (by columns m/z and intensitiy)
        self.rbformat_tex_ms = wx.RadioButton( self.notebook_pane_1, 130, self.lista_formato_inputf[3],
                                                    ( 30, 190 ), ( 350, 20 ) ) # crea el encabezado del formato comboBox
        self.rbformat_tex_ms.SetFont( self.font10RNB )

        #===============================================================================
        #    Ayuda sobre formatos del fichero de entrada
        #===============================================================================
        self.bitmap_format_help = wx.Bitmap( self.raiz_images + 'images/bitmaphelp.jpg' )
        self.bitmapButton_format_help = wx.BitmapButton( self.notebook_pane_1, 190, self.bitmap_format_help, ( 515, 155 ),
                                                        ( self.bitmap_format_help.GetWidth() + 15,
                                                         self.bitmap_format_help.GetHeight() + 15 ), wx.BU_AUTODRAW )

        #===============================================================================
        #   Eventos que direccionan a los metodos de opciones de formato
        #===============================================================================
        self.Bind( wx.EVT_RADIOBUTTON, self.OnClickradiobyrow, id = 100 )
        self.Bind( wx.EVT_COMBOBOX, self.OnClickcboxbyrow, id = 101 )
        self.Bind( wx.EVT_RADIOBUTTON, self.OnClickradiobycol, id = 110 )
        self.Bind( wx.EVT_COMBOBOX, self.OnClickcboxbycol, id = 111 )
        self.Bind( wx.EVT_RADIOBUTTON, self.OnClickradiofasta, id = 120 )
        self.Bind( wx.EVT_RADIOBUTTON, self.OnClickradioms, id = 130 )
        self.Bind( wx.EVT_BUTTON, self.OnClickformatohelp, id = 190 )
        self.Bind( wx.EVT_CHECKBOX, self.OnSelectFastaProtein,
                    self.checkbox_fastaprotein, id = 121 )# Evento al seleccionar el checkbox fasta protein

    #===============================================================================
    #   Grupo numero de clases par las secuencias numericas
    #===============================================================================
        #===============================================================================
        #    Crear Box de numero de clases
        #===============================================================================
        self.format_numclass_staticbox = wx.StaticBox( self.notebook_pane_1, -1,
                                                       'Classes for numerics sequences', ( 610, 20 ), ( 330, 210 ) )
        self.format_numclass_staticbox.SetFont( self.font11RIB )
        self.format_numclass_staticbox.Enable( False )

        #===============================================================================
        #    Lista con Formatos clase numerica
        #===============================================================================
        self.lista_formato_clase_numerica_tipo = [' n  Regular Interval Classes',
                                                  ' n SD-Interval Classes']

        #===============================================================================
        #    Formato clase numerica a intervalos regulares
        #===============================================================================
        self.rbnumclases_regular = wx.RadioButton( self.notebook_pane_1, 200, self.lista_formato_clase_numerica_tipo[0] ,
                                                   ( 625, 55 ), ( 170, 20 ), style = wx.RB_GROUP )
        self.rbnumclases_regular.SetFont( self.font10RNB )
        self.rbnumclases_regular.Enable( False )

        self.rbnumclases_regular_continua = wx.StaticText( self.notebook_pane_1, -1, '(a-1)*Ymax/n < Yi < a*Ymax/n', ( 640, 80 ) )
        self.rbnumclases_regular_continua.SetFont( self.font10RNB )
        self.rbnumclases_regular_continua.Enable( False )

        self.clases_numericas_tipo = 0

        self.spin_regular_clases = wx.SpinCtrl( self.notebook_pane_1, 201, '4', ( 820, 60 ), ( 45, 20 ), min = 2, max = 10 )
        self.spin_regular_clases.SetFont( self.font11normal )
        self.spin_regular_clases.Enable( False )

        self.clases_n = '4' #esta opcion (intervalo regular)  y este valor es el implicito

        #===============================================================================
        #    Formato clase numerica a intervalos dependientes de la desviacion standar
        #===============================================================================
        self.rbnumclases_sigma = wx.RadioButton( self.notebook_pane_1, 210, self.lista_formato_clase_numerica_tipo[1],
                                                    ( 625, 115 ), ( 150, 20 ) )
        self.rbnumclases_sigma.SetFont( self.font10RNB )
        self.rbnumclases_sigma.Enable( False )

        self.rbnumclases_sigma_continua = wx.StaticText( self.notebook_pane_1, -1, 'Yavg-n*SD/2 < Yi < Yavg+n*SD/2', ( 640, 140 ) )
        self.rbnumclases_sigma_continua.SetFont( self.font10RNB )
        self.rbnumclases_sigma_continua.Enable( False )

        self.spin_sigma_clases = wx.SpinCtrl( self.notebook_pane_1, 211, '2', ( 820, 120 ), ( 45, 20 ), min = 2, max = 4 )
        self.spin_sigma_clases.SetFont( self.font11normal )
        self.spin_sigma_clases.Enable( False )

        #===============================================================================
        #    Ayuda sobre los intervalos para definir las clases
        #===============================================================================
        self.bitmap_clases_help = wx.Bitmap( self.raiz_images + 'images/bitmaphelp.jpg' )
        self.bitmapButton_clases_help = wx.BitmapButton( self.notebook_pane_1, 290, self.bitmap_clases_help, ( 860, 155 ),
                                                        ( self.bitmap_clases_help.GetWidth() + 15,
                                                         self.bitmap_clases_help.GetHeight() + 15 ), wx.BU_AUTODRAW )

        self.bitmapButton_clases_help.Enable( False ) #inactivo inicialmente pues opcion de letras es la implicita

        #===============================================================================
        #   Eventos que direccionan a los metodos de numero de classes para secuencias numericas
        #===============================================================================
        self.Bind( wx.EVT_RADIOBUTTON, self.OnClickradioregular, id = 200 )
        self.Bind( wx.EVT_SPINCTRL, self.OnClickspinregular, id = 201 )
        self.Bind( wx.EVT_RADIOBUTTON, self.OnClickradiosigma, id = 210 )
        self.Bind( wx.EVT_SPINCTRL, self.OnClickspinsigma, id = 211 )
        self.Bind( wx.EVT_BUTTON, self.OnClickclaseshelp, id = 290 )

    #===============================================================================
    #   Grupo Tipos de indices. Crear Box del tipos de índices
    #===============================================================================
        #===============================================================================
        #    Crear Box del tipos de índices
        #===============================================================================
        self.indicestype_staticbox = wx.StaticBox( self.notebook_pane_1, -1,
                                                       'Indices levels', ( 735, 280 ), ( 202, 210 ) )
        self.indicestype_staticbox.SetFont( self.font11RIB )
        self.indicestype_staticbox.Enable( False )

        #===============================================================================
        #    Lista con tipos de indices
        #===============================================================================
        self.lista_indicestype = [' by classes in gnomons',
                                  ' by classes in global graph',
                                  ' by gnomons']

        #===============================================================================
        #    Radio botoms
        #===============================================================================
        self.rbindices_classgnomones = wx.RadioButton( self.notebook_pane_1, 300, self.lista_indicestype[0] ,
                                                   ( 750, 320 ), ( 140, 20 ), style = wx.RB_GROUP )
        self.rbindices_classgnomones.SetFont( self.font10RNB )
        self.rbindices_classgnomones.Enable( False )

        self.rbindices_classglobal = wx.RadioButton( self.notebook_pane_1, 310, self.lista_indicestype[1] ,
                                                   ( 750, 360 ), ( 160, 20 ) )
        self.rbindices_classglobal.SetFont( self.font10RNB )
        self.rbindices_classglobal.Enable( False )

        self.rbindices_gnomones = wx.RadioButton( self.notebook_pane_1, 320, self.lista_indicestype[2] ,
                                                   ( 750, 400 ), ( 100, 20 ) )
        self.rbindices_gnomones.SetFont( self.font10RNB )
        self.rbindices_gnomones.Enable( False )

        #===============================================================================
        #    Ayuda sobre tipos de indices
        #===============================================================================
        self.bitmap_indices_help = wx.Bitmap( self.raiz_images + 'images/bitmaphelp.jpg' )
        self.bitmapButton_indices_help = wx.BitmapButton( self.notebook_pane_1, 390, self.bitmap_indices_help, ( 858, 415 ),
                                                        ( self.bitmap_indices_help.GetWidth() + 15,
                                                         self.bitmap_indices_help.GetHeight() + 15 ), wx.BU_AUTODRAW )

        self.bitmapButton_indices_help.Enable( False ) #inactivo inicialmente pues opcion de letras es la implicita

        #===============================================================================
        #   Eventos que direccionan a los metodos tipo de indices
        #===============================================================================
        self.Bind( wx.EVT_RADIOBUTTON, self.OnClickradioindclassgno, id = 300 )
        self.Bind( wx.EVT_RADIOBUTTON, self.OnClickradioindclassglob, id = 310 )
        self.Bind( wx.EVT_RADIOBUTTON, self.OnClickradioindgno, id = 320 )
        self.Bind( wx.EVT_BUTTON, self.OnClickindiceshelp, id = 390 )

    #===============================================================================
    #    Crear la listbox, su encabezado, propiedades, tipo de letra, etc y checkbox select all
    #===============================================================================
        #===============================================================================
        #    Static Text encabezado de la listbox
        #===============================================================================
        self.list_box_statictext = wx.StaticText( self.notebook_pane_1, -1,
                                                    'Select the cases to build the spiral and calculate their indices:' ,
                                                    ( 25, 260 ) ) # crea el encabezado de la listbox
        self.list_box_statictext.SetFont( self.font11RIB ) # letra 11 Roman italica negrita
        self.list_box_statictext.Enable( False ) # hacer transparente el encabezado de la listbox (en inicio vacia)

        #===============================================================================
        #    List box como tal
        #===============================================================================
        self.list_box = wx.ListBox( self.notebook_pane_1, 900, ( 15, 290 ), ( 705, 200 ), self.lista_casos,
                                        wx.LB_EXTENDED | wx.LB_HSCROLL | wx.LB_NEEDED_SB ) # Construye la listbox
        self.list_box.Enable( False ) # hacer transparente e inaccesible la listbox (en inicio vacia)
        self.list_box.SetFont( self.font10normal )
        self.list_box.SetBackgroundColour( wx.Colour( 230, 250, 250 ) )

        #===============================================================================
        #    Check box que permite seleccionar toda la lista de secuencias desmarcarla
        #===============================================================================
        self.checkbox_selectall = wx.CheckBox( self.notebook_pane_1, 901 , 'Select All',
                                               ( 15, 510 ), ( 90, -1 ) ) # Construye el checkbox selectall
        self.checkbox_selectall.SetFont( self.font11RIB ) # letra 11 Roman italica negrita
        self.checkbox_selectall.Enable( False ) # hacer transparente e inaccesible el checkbox (listbox en inicio vacia)

    #===============================================================================
    #    Eventos que redireccionan a metodos relacionados con la listbox
    #===============================================================================
        #===============================================================================
        #    Evento de la listbox
        #===============================================================================
        self.Bind( wx.EVT_LISTBOX, self.OnSelectItem,
                   self.list_box, id = 900 )# Evento al seleccionar un item de la listbox
        #===============================================================================
        #    Evento del checkbox
        #===============================================================================
        self.Bind( wx.EVT_CHECKBOX, self.OnSelectAllItem,
                    self.checkbox_selectall, id = 901 )# Evento al seleccionar el checkbox selectall

#===============================================================================
# Metodos o acciones a realizar en cada evento menu
#===============================================================================
    #===============================================================================
    #    Metodo opcion file/quit
    #===============================================================================
    def OnQuit( self, event ):
        alert = wx.MessageDialog( self, "Do you really want to quit" )
        response = alert.ShowModal()
        alert.Destroy()
       
        if response == wx.ID_OK:
            self.Close()            
        else:
            event.Skip()   

    #===============================================================================
    #    Metodo opcion file/open
    #===============================================================================
    def OnOpenFile( self, event ):
        #Inicicion de variables
        self.input_file_names = []
        self.input_file_paths = []
        self.input_file_csv = ''

        #===============================================================================
        #    Ventana de dialogo Open file
        #===============================================================================
        self.lista_openfile_wildcard = ["Text files (*.txt)|*.txt",
                                        "Text files (*.txt)|*.txt|CSV files (*.csv)|*.csv"]
        self.lista_openfile_style = [wx.OPEN | wx.CHANGE_DIR,
                                     wx.OPEN | wx.CHANGE_DIR | wx.MULTIPLE]

        if self.formato_inputf != 3:
            ind = 0
        else:
            ind = 1

        self.open_dialog = wx.FileDialog( None, "Choose a file", os.getcwd(), "",
                                         self.lista_openfile_wildcard[ind] ,
                                         self.lista_openfile_style[ind] )

        if self.open_dialog.ShowModal() == wx.ID_OK:
            if ind:
                self.input_file_names[:] = self.open_dialog.GetFilenames() # nombre de los ficheros seleccionados
                self.input_file_paths[:] = self.open_dialog.GetPaths()  # almacenar el path de los ficheros
                self.input_file_csv = self.open_dialog.GetFilterIndex() # 0 si est .txt y 1 si es csv
            else:
                self.input_file_names.append( self.open_dialog.GetFilename() ) # nombre del fichero seleccionado
                self.input_file_paths.append( self.open_dialog.GetPath() ) # almacenar el path del fichero
            self.open_dialog.Destroy()
        else:
            self.open_dialog.Destroy()
            return

        #===============================================================================
        #    Abrir el fichero de texto seleccionado capturando posibles errores en la apertura
        #    leer datos, filtrarlos y convertirlos en seq de letras y mostrarlos en list box.
        #===============================================================================
        self.inputf = ''
        self.data = []

        for path in self.input_file_paths:
            #===============================================================================
            #    Capturar errores al abrir los ficheros
            #===============================================================================
            try:
                self.inputf = open( path, "r" ) # abrir el fichero selecionado en modo solo lectura
            except IOError, ( errno ): # captura un error de input/output y el numero asociado a este
                    if errno == 2 : # error 2, ocurre cuando se cierra la ventana openfile sin seleccionar ningun fichero
                        if self.lista_casos: # si aun contamos con datos de un fichero abierto anteriormente
                            return # no hay nada que hacer y seguimos trabajando con los datos que teniamos
                        else: # si no contamos con datos anteriores recordamos que se necesita un fichero para trabajar
                            self.errorfiledlg = wx.MessageDialog( self, 'Forgot select an File. ConvSqToUSpCT need an File to works',
                                                                  'Missing File', wx.OK | wx.ICON_ERROR )
                            self.errorfiledlg.ShowModal()
                    return
            except UnicodeDecodeError, error: # captura error relacionado con letras no legibles. CREO QUE EN ESTE CONTEXTO NO FUNCIONA
                self.errorfiledlg = wx.MessageDialog( self, 'The file ' + path + 
                                                      ' contains at least one non-unicode characther. Please check your file and try again.'
                                                      + str( error ), 'Unicode Error', wx.OK | wx.ICON_ERROR )
                self.errorfiledlg.ShowModal()
                return
            else: # si no tiene lugar ningun error, se abre el fichero y para leer las secuencias
                self.inputf = open( path, "r" ) # abrir fichero en modo lectura par tomar los codes
                self.data.append( self.inputf.readlines() ) # Obtengo codes como una lista con todas las lineas del fichero.txt
                self.inputf.close ()

        #===============================================================================
        #  Re inicializar variables involucradas, limpirar list box
        #===============================================================================
        self.lista_casos = []
        self.lista_casos_names = []
        self.lista_casos_sequences = []
        self.lista_casos_clases = []
        self.lista_casos_orig = []
        self.lista_casos_names_orig = []
        self.lista_casos_sequences_orig = []
        self.lista_casos_clases_orig = []
        self.lista_casos_selected = []
        self.lista_names_selected = []
        self.lista_sequences_selected = []
        self.lista_clases_selected = []
        self.lista_items_selected = []
        self.lista_casos_view = []

        self.list_box.Clear() # lipia la lista antes de llenarla con los codes (util si estaba llena de un fichero anterior)
        if self.notebook.GetPageCount() > 1:
            self.notebook.DeletePage( 1 )

        #===============================================================================
        #    Redireccionar a los filtros que revisan data de entrada y conviertena secuencias de letras
        #===============================================================================
        if self.formato_inputf == 0: # by rows
            if self.formato_sequences == 0: # by rows letras
                FiltrosSeq_v_1_0_imp.filtroByRowsLett( self )
            if self.formato_sequences == 1: # by rows numeros
                FiltrosSeq_v_1_0_imp.filtroByRowsNum( self )
        elif self.formato_inputf == 1: # by columns
            if self.formato_sequences == 0: # by columns letras
                FiltrosSeq_v_1_0_imp.filtroByColLett( self )
            if self.formato_sequences == 1: # by columns numeros
                FiltrosSeq_v_1_0_imp.filtroByColNum( self )
        elif self.formato_inputf == 2: # fichero fasta
            FiltrosSeq_v_1_0_imp.filtroFasta( self )
        else: # fichero ms
            FiltrosSeq_v_1_0_imp.filtroMs( self )

        #===============================================================================
        #    Activar la list box y cargarla con la lista de casos
        #===============================================================================
        self.list_box_statictext.SetLabel( 'Select the cases to build the spiral:' )
        self.list_box_statictext.SetFont( self.font11RIB )
        self.list_box_statictext.Enable( True ) # hace completamente visible el cabezado de la listbox
        self.list_box.Enable( True ) # hace completamente visible y accesible la listbos (ya se va a llenar)
        self.lista_casos_view = []

        #===============================================================================
        #    Recortar secuencias muy largas para que aparezcan en la lista, solo para ver, la seq no se alteran
        #===============================================================================
        for caso in self.lista_casos:
            if len( caso ) > 2000:
                self.lista_casos_view.append( caso[:2000] )
            else:
                self.lista_casos_view.append( caso )

        self.list_box.Set( self.lista_casos_view ) # rellena listbox con los codes almacenados en variable global lista_casos_view
        self.checkbox_selectall.Enable( True ) # hace visible y accesible el checkbox (ya se tiene listbox llena)pass
        
        self.checkbox_selectall.SetValue( False )

        #===============================================================================
        # Hacer copia de listas originales por si se quiere guardar en un fichero
        #===============================================================================
        self.lista_casos_orig[:] = self.lista_casos
        self.lista_casos_names_orig[:] = self.lista_casos_names
        self.lista_casos_sequences_orig[:] = self.lista_casos_sequences
        self.lista_casos_clases_orig[:] = self.lista_casos_clases

        #===============================================================================
        #    Activar/Desactivar opciones según lo que se puede hacer hasta en estos momentos. 
        #===============================================================================
        self.si_casos_cargados = True # variable global que permite saber que sen han cargo los codes
        self.si_graph_build = False
        self.si_indices_calculed = False
        
        self.menuBar.Enable( 12, False )

        if self.formato_inputf == 0 and self.formato_sequences == 0:
            self.menuBar.Enable( 13, False )
        else:
            self.menuBar.Enable( 13, True )
            if self.lista_casos != self.lista_casos_orig:
                self.menuBar.Enable( 13002, True )
            else:
                self.MenuBar.Enable( 13002, False )

        self.menuBar.Enable( 14, False )
        self.menuBar.Enable( 15, False )
        self.menuBar.Enable( 21, False )
        self.menuBar.Enable( 22, False )
        self.menuBar.Enable( 31, False )

        self.indicestype_staticbox.Enable( False )
        self.rbindices_classgnomones.Enable( False )
        self.rbindices_classglobal.Enable( False )
        self.rbindices_gnomones.Enable( False )
        self.bitmapButton_indices_help.Enable( False ) 

        #===============================================================================
        # Restablecer barra de progreso
        #===============================================================================
        self.StatusBar.SetStatusText( ' ', 1 )
        self.StatusBar.SetStatusText( ' ', 2 )

    #===============================================================================
    #    Metodo opcion convert/convert
    #===============================================================================
    def OnBuild( self, event ):
        #===============================================================================
        #   Verificar si se ha seleccionado alguna secuencia para convertir
        #===============================================================================
        if not self.lista_items_selected: # Si no se selecciono ninguna secuencia
            no_codes_txt = """
            There is not any selected code. You have to select the sequences
            that you wants to build the spirals."""
            self.Alerta( no_codes_txt, 'Missing sequences' )
            return

        self.ct_linea1 = []
        self.ct_linea2 = []
        self.ct_bloque_coord_atom = []
        self.ct_bloque_conectivity = []
        self.lista_ulam_casos = []
        self.indices_clases_gnomones_casos = []
        self.indices_clases_globales_casos = []
        self.indices_gnomones_casos = []
        self.lista_grG_casos = []

        #===============================================================================
        # Llamar la funcion convtospiral del modulo BuildSpiral_v_1_0_impCT_imp para construir la espiral de Ulam
        # de la(s) secuencias selecionadas, calcular los indices y todo lo relacionado con la(s)
        # conectividad(es) en formato CT.
        #===============================================================================
        self.ct_linea1, self.ct_linea2, self.ct_bloque_coord_atom, self.ct_bloque_conectivity, self.lista_ulam_casos, self.lista_gnomones_casos, self.lista_grG_casos = BuildSpiral_v_1_0_imp.convtospiral( self )

        #===============================================================================
        # Casos con spiral construida pasan a ser los casos bases de trabajo
        #===============================================================================
        self.lista_casos[:] = self.lista_casos_selected
        self.lista_casos_names[:] = self.lista_names_selected
        self.lista_casos_sequences[:] = self.lista_sequences_selected
        self.lista_casos_clases[:] = self.lista_clases_selected

        #===============================================================================
        #    Cambiar encabazado de la listbox y hacerlo visible
        #===============================================================================
        self.list_box_statictext.SetLabel( 'Select the cases to calculate indices or one case to view its spiral:' )
        self.list_box_statictext.SetFont( self.font11RIB )
        self.list_box_statictext.Enable( True ) # hace completamente visible el cabezado de la listbox

        #===============================================================================
        #    Limpiar la lista y hacerla visible
        #===============================================================================
        self.lista_casos_view = []
        self.list_box.Clear() # lipia la lista antes de llenarla con los codes (util si estaba llena de un fichero anterior)
        self.list_box.Enable( True ) # hace completamente visible y accesible la listbos (ya se va a llenar)
        
        #===============================================================================
        #    Recortar secuencias muy largas para que aparezcan en la lista, solo para ver, las seq no se alteran
        #===============================================================================
        for caso in self.lista_casos:
            if len( caso ) > 2000:
                self.lista_casos_view.append( caso[:2000] )
            else:
                self.lista_casos_view.append( caso )

        self.list_box.Set( self.lista_casos_view ) # rellena listbox con los codes almacenados en variable global list_casos_view

        self.checkbox_selectall.SetValue( False )
        self.checkbox_selectall.Enable( True ) # hace visible y accesible el checkbox (ya se tiene listbox llena)pass

        #===============================================================================
        #    Activar/Desactivar opciones según lo que se puede hacer hasta en estos momentos. 
        #===============================================================================
        self.si_graph_build = True
        self.si_indices_calculed = False

        if self.lista_casos != self.lista_casos_orig:
            self.menuBar.Enable( 12, True )
        else:
            self.menuBar.Enable( 12, False )

        if self.formato_inputf == 0 and self.formato_sequences == 0:
            self.menuBar.Enable( 13, False )
        else:
            self.menuBar.Enable( 13, True )
            if self.lista_casos != self.lista_casos_orig:
                self.menuBar.Enable( 13002, True )
            else:
                self.MenuBar.Enable( 13002, False )

        self.menuBar.Enable( 14, True )
        self.menuBar.Enable( 15, False )
        self.menuBar.Enable( 21, False )
        self.menuBar.Enable( 22, True )
        self.menuBar.Enable( 31, True )
        ActivarIndicesTipo ( self, True )
        

        #===============================================================================
        # Re inicializar las listas de seleccion 
        #===============================================================================
        self.lista_casos_selected = []
        self.lista_names_selected = []
        self.lista_sequences_selected = []
        self.lista_clases_selected = []
        self.lista_items_selected = []

        #===============================================================================
        # Restablecer barra de progreso
        #===============================================================================
        self.StatusBar.SetStatusText( ' ', 1 )
        self.StatusBar.SetStatusText( ' ', 2 )

    #===============================================================================
    #    Metodo opcion convert/convert
    #===============================================================================
    def OnCalculate( self, event ):
        #===============================================================================
        #   Verificar si se ha seleccionado alguna secuencia para convertir
        #===============================================================================
        if not self.lista_items_selected: # Si no se selecciono ninguna secuencia
            no_codes_txt = """
            There is not any selected code. You have to select the sequences
            that you wants to calculate the indices."""
            self.Alerta( no_codes_txt, 'Missing sequences' )
            return

        self.indices_calculated = []
        self.indices_calculated = CalcIndices_v_1_0_imp.myIndices( self )

        #===============================================================================
        # Colocar indices en el Grid
        #===============================================================================
        if self.indices_tipo == 0:
            #===============================================================================
            #    Preparar Encabezado de las columnas
            #===============================================================================
            self.colLabels = []
#
            for ind_clas_gnom in self.indices_calculated[0]:
                for ind_clas in ind_clas_gnom:
                    self.AvanGauge( self )
                    self.colLabels.append( 'Fr(%3s;%3s)' % ( ind_clas[0].center( 3 ), str( ind_clas[1] ).center( 3 ) ) )
#
            for ind_clas_gnom in self.indices_calculated[0]:
                for ind_clas in ind_clas_gnom:
                    self.AvanGauge( self )
                    self.colLabels.append( 'Sh(%3s;%3s)' % ( ind_clas[0].center( 3 ), str( ind_clas[1] ).center( 3 ) ) )
#
            #===============================================================================
            #    Preparar Encabezado de las filas
            #===============================================================================
            self.rowLabels = []
            self.data_indices = []
#
            for nsecu in range( len( self.lista_items_selected ) ):
                self.rowLabels.append( '%6s' % self.lista_names_selected[nsecu] )
                indice_caso = []
                for ind_clas_gnom in self.indices_calculated[nsecu]:
                    self.AvanGauge( self )
                    for ind_clas in ind_clas_gnom:
                        self.AvanGauge( self )
                        indice_caso.append( '%9.5f' % ind_clas[2] )
                for ind_clas_gnom in self.indices_calculated[nsecu]:
                    self.AvanGauge( self )    
                    for ind_clas in ind_clas_gnom:
                        self.AvanGauge( self )
                        indice_caso.append( '%9.5f' % ind_clas[3] )
                self.data_indices.append( indice_caso )

        elif self.indices_tipo == 1:
            #===============================================================================
            #    Prepar Encabezado de las columnas
            #===============================================================================
            self.colLabels = []

            for ind_clas_glob in self.indices_calculated[0]:
                self.AvanGauge( self )
                self.colLabels.append( 'Fr(%3s)' % ( ind_clas_glob[0].center( 3 ) ) )
            for ind_clas_glob in self.indices_calculated[0]:
                self.AvanGauge( self )
                self.colLabels.append( 'Sh(%3s)' % ( ind_clas_glob[0].center( 3 ) ) )

            #===============================================================================
            #    Preparar Encabezado de las filas
            #===============================================================================
            self.rowLabels = []
            self.data_indices = []

            for nsecu in range( len( self.lista_items_selected ) ):
                self.rowLabels.append( '%6s' % self.lista_names_selected[nsecu] )
                indice_caso = []
                for ind_clas_glob in self.indices_calculated[nsecu]:
                    self.AvanGauge( self )
                    indice_caso.append( '%9.5f' % ind_clas_glob[1] )
                for ind_clas_glob in self.indices_calculated[nsecu]:
                    self.AvanGauge( self )    
                    indice_caso.append( '%9.5f' % ind_clas_glob[2] )
                self.data_indices.append( indice_caso )

        else:
            #===============================================================================
            #    Prepar Encabezado de las columnas
            #===============================================================================
            self.colLabels = []

            for ind_gnomones in self.indices_calculated[0]:
                self.AvanGauge( self )
                self.colLabels.append( 'Fr(%3s)' % ( str( ind_gnomones[0] ).center( 3 ) ) )

            for ind_gnomones in self.indices_calculated[0]:
                self.AvanGauge( self )
                self.colLabels.append( 'Sh(%3s)' % ( str( ind_gnomones[0] ).center( 3 ) ) )

            #===============================================================================
            #    Preparar Encabezado de las filas
            #===============================================================================
            self.rowLabels = []
            self.data_indices = []

            for nsecu in range( len( self.lista_items_selected ) ):
                self.rowLabels.append( '%6s' % self.lista_names_selected[nsecu] )
                indice_caso = []
                for ind_gnomones in self.indices_calculated[nsecu]:
                    self.AvanGauge( self )
                    indice_caso.append( '%9.5f' % ind_gnomones[1] )
                for ind_gnomones in self.indices_calculated[nsecu]:
                    self.AvanGauge( self )    
                    indice_caso.append( '%9.5f' % ind_gnomones[2] )
                self.data_indices.append( indice_caso )

        #===============================================================================
        # Llamar la funcion HugeTableGrid del modulo Grid_v_1_0_imp para construir el grid y 
        # colocar los encabezados de columnas y filas y los valores de los indices en el.
        #===============================================================================
        self.resultados = ''
        self.resultados = Grid_v_1_0_imp.HugeTableGrid( self.notebook, sys.stdout, self.colLabels, self.rowLabels, self.data_indices )

        #===============================================================================
        #    Poner el grid en el la segunda pagina del notebook titulada Indices
        #===============================================================================
        if self.notebook.GetPageCount() > 1:
            self.notebook.DeletePage( 1 )
            self.notebook.AddPage( self.resultados, "Indices", wx.NB_TOP )
        else:
            self.notebook.AddPage( self.resultados, "Indices", wx.NB_TOP )
        self.resultados.SetFocus()

        self.menuBar.Enable( 15, True )
        self.StatusBar.SetStatusText( ' ', 1 )
        self.StatusBar.SetStatusText( ' ', 2 )

    #===============================================================================
    #    Metodo opcion view/view
    #===============================================================================
    def OnView( self, event ):
        if len( self.lista_items_selected ) > 1:
            only_one_graph_txt = """
            Only one Spiral Graph can be shown at time. 
            Please select only one converted sequence."""
            self.Alerta( only_one_graph_txt, 'To much sequeces selected' )
        elif len( self.lista_items_selected ) == 0:
            not_graph_txt = """
            There is not any sequence selected. You have to select
            the sequence that you wants see its Spiral graph."""
            self.Alerta( not_graph_txt, 'Not sequece selected' )
        else:
            item = ''
            item = self.lista_items_selected[0]
            if math.sqrt( self.ct_linea2[item][0] ) == int( math.sqrt( self.ct_linea2[item][0] ) ): # si es un entero
                self.view_dimen = ( int( math.sqrt( self.ct_linea2[item][0] ) ) - 1 )
            else: # si la raiz de tope no es un entero
                self.view_dimen = ( int( math.sqrt( self.ct_linea2[item][0] ) ) )

            self.visor_spiral_graph = SpiralGraph_v_1_0_imp.SpiralFrame ( self.ct_linea1[item],
                                                                    self.ct_linea2[item],
                                                                    self.ct_bloque_coord_atom[item],
                                                                    self.ct_bloque_conectivity[item],
                                                                    self.view_dimen )
            self.visor_spiral_graph.Show()

    #===============================================================================
    #    Metodo opcion file/reload sequences
    #===============================================================================
    def OnReloadSeq( self, event ):
        #===============================================================================
        # Restaurar valores originales
        #===============================================================================
        self.lista_casos[:] = self.lista_casos_orig
        self.lista_casos_names[:] = self.lista_casos_names_orig
        self.lista_casos_sequences[:] = self.lista_casos_sequences_orig
        self.lista_casos_clases[:] = self.lista_casos_clases_orig

        #===============================================================================
        # Re inicializar las listas de seleccion y otras asignaciones de variables 
        #===============================================================================
        self.lista_casos_selected = []
        self.lista_names_selected = []
        self.lista_sequences_selected = []
        self.lista_clases_selected = []
        self.lista_items_selected = []

        self.ct_linea1 = []
        self.ct_linea2 = []
        self.ct_bloque_coord_atom = []
        self.ct_bloque_conectivity = []
        self.lista_ulam_casos = []
        self.indices_clases_gnomones_casos = []
        self.indices_clases_globales_casos = []

        self.indices_calculated = []
        self.colLabels = []
        self.rowLabels = []
        self.data_indices = []
        
        self.resultados = ''
        if self.notebook.GetPageCount() > 1:
            self.notebook.DeletePage( 1 )

        #===============================================================================
        #    Cambiar encabazado de la listbox y hacerlo visible
        #===============================================================================
        self.list_box_statictext.SetLabel( 'Select the cases to build the spiral and calculate their indices:' )
        self.list_box_statictext.SetFont( self.font11RIB )
        self.list_box_statictext.Enable( True ) # hace completamente visible el cabezado de la listbox

        #===============================================================================
        #    Limpiar la lista y hacerla visible
        #===============================================================================
        self.lista_casos_view = []
        self.list_box.Clear() # lipia la lista antes de llenarla con los codes (util si estaba llena de un fichero anterior)
        self.list_box.Enable( True ) # hace completamente visible y accesible la listbos (ya se va a llenar)
        
        #===============================================================================
        #    Recortar secuencias muy largas para que aparezcan en la lista, solo para ver, las seq no se alteran
        #===============================================================================
        for caso in self.lista_casos:
            if len( caso ) > 2000:
                self.lista_casos_view.append( caso[:2000] )
            else:
                self.lista_casos_view.append( caso )

        self.list_box.Set( self.lista_casos_view ) # rellena listbox con los codes almacenados en variable global list_casos_view

        self.checkbox_selectall.SetValue( False )
        self.checkbox_selectall.Enable( True ) # hace visible y accesible el checkbox (ya se tiene listbox llena)pass

        #===============================================================================
        #    Activar/Desactivar opciones según lo que se puede hacer hasta en estos momentos. 
        #===============================================================================
        self.si_casos_cargados = True # variable global que permite saber que sen han cargo los codes
        self.si_graph_build = False
        self.si_indices_calculed = False

        self.menuBar.Enable( 12, False )
        self.menuBar.Enable( 14, False )
        self.menuBar.Enable( 15, False )
        self.menuBar.Enable( 21, True )
        self.menuBar.Enable( 22, False )
        self.menuBar.Enable( 31, False )
        ActivarIndicesTipo ( self, False )

    #===============================================================================
    #    Metodo opcion file/make copy of original sequences
    #===============================================================================
    def OnMakeCopyOrigen( self, event ):
        self.output_copyorigen_path = ''
        self.output_copyorigen_filename = ''
        self.outputfcopyorigen = ''

        self.copyorigen_wildcard = "Text files (*.txt)|*.txt"
        self.copyorigen_style = [wx.SAVE | wx.OVERWRITE_PROMPT | wx.CHANGE_DIR]

        self.copyorigen_dialog = wx.FileDialog( None, "Make a copy of the original sequences as ...", os.getcwd(), "",
                                         self.copyorigen_wildcard ,
                                         self.copyorigen_style[0], )

        if self.copyorigen_dialog.ShowModal() == wx.ID_OK:
            self.output_copyorigen_path = self.copyorigen_dialog.GetPath()
            self.output_copyorigen_filename = self.copyorigen_dialog.GetFilename()

        
        try:
            self.outputfcopyorigen = open( self.output_copyorigen_path, "w" ) # abrir el fichero selecionado en modo solo lectura
        except IOError, ( errno ): # captura un error de input/output y el numero asociado a este
                if errno == 2 : # error 2, ocurre cuando se cierra la ventana openfile sin seleccionar ningun fichero
                    pass
                return
        except UnicodeDecodeError, error: # captura error relacionado con letras no legibles. CREO QUE EN ESTE CONTEXTO NO FUNCIONA
            self.errorfiledlg = wx.MessageDialog( self, 'The file ' + path + 
                                                  ' contains at least one non-unicode characther. Please check your file and try again.'
                                                  + str( error ), 'Unicode Error', wx.OK | wx.ICON_ERROR )
            self.errorfiledlg.ShowModal()
            return
        else: # si no tiene lugar ningun error, se abre el fichero y para leer las secuencias
            self.outputfcopyorigen = open( self.output_copyorigen_path, "w" ) # abrir fichero en modo lectura par tomar los codes
            self.AvanGauge( self )
            for name, seq in zip( self.lista_casos_names_orig, self.lista_casos_sequences_orig ):
                self.AvanGauge( self )
                self.outputfcopyorigen.write( name.replace( ' ', '' ) + ' ' + seq.replace( ' ', '' ) + '\n' )
            self.outputfcopyorigen.close()

        self.StatusBar.SetStatusText( ' ', 1 )
        self.StatusBar.SetStatusText( ' ', 2 )

    #===============================================================================
    #    Metodo opcion file/make copy of studied sequences
    #===============================================================================
    def OnMakeCopyStudied( self, event ):
        self.output_copystudied_path = ''
        self.output_copystudied_filename = ''
        self.outputfcopystudied = ''

        self.copystudied_wildcard = "Text files (*.txt)|*.txt"
        self.copystudied_style = [wx.SAVE | wx.OVERWRITE_PROMPT | wx.CHANGE_DIR]

        self.copystudied_dialog = wx.FileDialog( None, "Make a copy of the studied sequences as ...", os.getcwd(), "",
                                         self.copystudied_wildcard ,
                                         self.copystudied_style[0], )

        if self.copystudied_dialog.ShowModal() == wx.ID_OK:
            self.output_copystudied_path = self.copystudied_dialog.GetPath()
            self.output_copystudied_filename = self.copystudied_dialog.GetFilename()

        
        try:
            self.outputfcopystudied = open( self.output_copystudied_path, "w" ) # abrir el fichero selecionado en modo solo lectura
        except IOError, ( errno ): # captura un error de input/output y el numero asociado a este
                if errno == 2 : # error 2, ocurre cuando se cierra la ventana openfile sin seleccionar ningun fichero
                    pass
                return
        except UnicodeDecodeError, error: # captura error relacionado con letras no legibles. CREO QUE EN ESTE CONTEXTO NO FUNCIONA
            self.errorfiledlg = wx.MessageDialog( self, 'The file ' + path + 
                                                  ' contains at least one non-unicode characther. Please check your file and try again.'
                                                  + str( error ), 'Unicode Error', wx.OK | wx.ICON_ERROR )
            self.errorfiledlg.ShowModal()
            return
        else: # si no tiene lugar ningun error, se abre el fichero y para leer las secuencias
            self.outputfcopystudied = open( self.output_copystudied_path, "w" ) # abrir fichero en modo lectura par tomar los codes
            self.AvanGauge( self )
            for name, seq in zip( self.lista_casos_names, self.lista_casos_sequences ):
                self.AvanGauge( self )
                self.outputfcopystudied.write( name.replace( ' ', '' ) + ' ' + seq.replace( ' ', '' ) + '\n' )
            self.outputfcopystudied.close()

        self.StatusBar.SetStatusText( ' ', 1 )
        self.StatusBar.SetStatusText( ' ', 2 )

    #===============================================================================
    #    Metodo opcion file/export spiral as ct files
    #===============================================================================
    def OnExportSpiralCt( self, event ):
        self.output_spiral_paths = ''
        self.outputfspi = ''

        dialog_export_spiral = wx.DirDialog( None, "Choose a directory:",
                              style = wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON )
        if dialog_export_spiral.ShowModal() == wx.ID_OK:
            self.output_spiral_paths = dialog_export_spiral.GetPath()
        dialog_export_spiral.Destroy()
        for ( caso, nombre ) in enumerate( self.lista_casos_names ):
            self.outputfspi = open( self.output_spiral_paths + '\\' + nombre.replace( '|', ' ' ) + '.ct', 'w' )
            self.outputfspi.write ( self.ct_linea1[caso] + '\n' )
            self.outputfspi.write ( str( self.ct_linea2[caso][0] ) + ' ' + str( self.ct_linea2[caso][1] ) + '\n' )
            
            for i in range( len( self.lista_casos_sequences[caso] ) ):
                self.AvanGauge( self )
                self.outputfspi.write( '%9.4f' % self.ct_bloque_coord_atom[caso][i][0] + ' ' + 
                                       '%9.4f' % self.ct_bloque_coord_atom[caso][i][1] + ' ' + 
                                       '%9.4f' % self.ct_bloque_coord_atom[caso][i][2] + ' ' + 
                                       '%s' % self.ct_bloque_coord_atom[caso][i][3] + '\n' )
            
            for i in range( self.ct_linea2[caso][1] ):
                self.AvanGauge( self )
                self.outputfspi.write ( str( self.ct_bloque_conectivity[caso][i][0] ) + ' ' + 
                                        str( self.ct_bloque_conectivity[caso][i][1] ) + ' ' + 
                                        str( self.ct_bloque_conectivity[caso][i][2] ) + ' ' + 
                                        str( self.ct_bloque_conectivity[caso][i][3] ) + '\n' )
            self.outputfspi.close()

        self.StatusBar.SetStatusText( ' ', 1 )
        self.StatusBar.SetStatusText( ' ', 2 )

    #===============================================================================
    #    Metodo opcion file/export spiral as net files
    #===============================================================================
    def OnExportSpiralNet( self, event ):
        self.output_spiral_paths = ''
        self.outputfspi = ''

        dialog_export_spiral = wx.DirDialog( None, "Choose a directory:",
                              style = wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON )
        if dialog_export_spiral.ShowModal() == wx.ID_OK:
            self.output_spiral_paths = dialog_export_spiral.GetPath()
        dialog_export_spiral.Destroy()
        for ( caso, nombre ) in enumerate( self.lista_casos_names ):
            self.outputfspi = open( self.output_spiral_paths + '\\' + nombre.replace( '|', ' ' ) + '.net', 'w' )
            self.outputfspi.write ( '*Vertices' + '\t' + str( self.ct_linea2[caso][0] ) + '\n' )
            
            for i in range( self.ct_linea2[caso][0] ):
                self.AvanGauge( self )
                self.outputfspi.write( str( i + 1 ) + '\t' + '"' + str( i + 1 ) + '"' + '\n' )
            
            self.outputfspi.write( '*Edges' + '\n' )
            for i in range( self.ct_linea2[caso][1] ):
                self.AvanGauge( self )
                self.outputfspi.write ( str( self.ct_bloque_conectivity[caso][i][0] ) + '\t' + 
                                        str( self.ct_bloque_conectivity[caso][i][1] ) + '\n' )
            self.outputfspi.close()

        self.StatusBar.SetStatusText( ' ', 1 )
        self.StatusBar.SetStatusText( ' ', 2 )

    #===============================================================================
    #    Metodo opcion file/save indices
    #===============================================================================
    def OnSaveFilesIndices( self, event ):
        self.output_ind_path = ''
        self.output_ind_filename = ''
        self.output_ind_filetype = ''
        self.outputfind = ''

        self.saveind_wildcard = "Text files (*.txt)|*.txt|CSV files (*.csv)|*.csv"
        self.saveind_style = [wx.SAVE | wx.OVERWRITE_PROMPT | wx.CHANGE_DIR]

        self.saveind_dialog = wx.FileDialog( None, "Save Indices As ...", os.getcwd(), "",
                                         self.saveind_wildcard ,
                                         self.saveind_style[0], )

        if self.saveind_dialog.ShowModal() == wx.ID_OK:
            self.output_ind_path = self.saveind_dialog.GetPath()
            self.output_ind_filename = self.saveind_dialog.GetFilename()
            self.output_ind_filetype = self.saveind_dialog.GetFilterIndex()

        
        try:
            self.outputfind = open( self.output_ind_path, "w" ) # abrir el fichero selecionado en modo solo lectura
        except IOError, ( errno ): # captura un error de input/output y el numero asociado a este
                if errno == 2 : # error 2, ocurre cuando se cierra la ventana openfile sin seleccionar ningun fichero
                    pass
                return
        except UnicodeDecodeError, error: # captura error relacionado con letras no legibles. CREO QUE EN ESTE CONTEXTO NO FUNCIONA
            self.errorfiledlg = wx.MessageDialog( self, 'The file ' + path + 
                                                  ' contains at least one non-unicode characther. Please check your file and try again.'
                                                  + str( error ), 'Unicode Error', wx.OK | wx.ICON_ERROR )
            self.errorfiledlg.ShowModal()
            return
        else: # si no tiene lugar ningun error, se abre el fichero y para leer las secuencias
            self.outputfind = open( self.output_ind_path, "w" ) # abrir fichero en modo lectura par tomar los codes
            self.AvanGauge( self )
            
            if not self.output_ind_filetype: # indices salvados en fichero txt

                self.outputfind.write( 'Case' + ' ' * ( len( self.rowLabels[0] ) - 2 ) ),
                for label in self.colLabels:
                    if self.indices_tipo:
                        self.outputfind.write( '   \t' + label.center( 10 ) ),
                    else:
                        self.outputfind.write( '  \t' + label.center( 10 ) ),
                self.outputfind.write( '\n' )
                for i, label in enumerate( self.rowLabels ):
                    self.outputfind.write ( label ),
                    for colv in self.data_indices[i]:
                        self.outputfind.write ( '  \t' + colv ),
                    self.outputfind.write ( '\n' )

            else: # indices salvados en fichero csv

                self.outputfind.write( 'Case'.center( 6 ) ),
                for label in self.colLabels:
                    self.outputfind.write( ',' + label.center( 9 ) ),
                self.outputfind.write( '\n' )
                for i, label in enumerate( self.rowLabels ):
                    self.outputfind.write ( label ),
                    for colv in self.data_indices[i]:
                        self.outputfind.write ( ',' + colv ),
                    self.outputfind.write ( '\n' )
                
            self.outputfind.close ()

        self.StatusBar.SetStatusText( ' ', 1 )
        self.StatusBar.SetStatusText( ' ', 2 )

    #===============================================================================
    #    Metodo opcion help/about
    #===============================================================================
    def OnAbout( self, event ):
        self.about = About_v_1_0_imp.MyHtmlFrame( None, "About CULSPIN 1.0", self.raiz_images )
        self.about.SetIcon( wx.Icon( self.raiz_images + 'images/about.ico', wx.BITMAP_TYPE_ICO ) )
        self.about.Center()
        self.about.Show()

    #===============================================================================
    #    Metodo opcion help/help
    #===============================================================================
    def OnHelp( self, event ):
        self.help = HelpHtml_v_1_0_imp.MyHtmlFrame( None, 'CULSPIN Help', 'page4', self.raiz_images )
        self.help.SetIcon( wx.Icon( self.raiz_images + 'images/help.ico', wx.BITMAP_TYPE_ICO ) )
        self.help.Center()
        self.help.Show()

#===============================================================================
# Metodos o acciones grupo formato
#===============================================================================
    #===============================================================================
    #    Metodo radiobutton by row
    #===============================================================================
    def OnClickradiobyrow ( self, event ):
        self.comboBox_byrow.Enable( True )
        self.comboBox_bycol.Enable( False )
        self.checkbox_fastaprotein.Enable( False )
        self.si_fastaprotein = False
        self.formato_inputf = 0
        self.formato_sequences = self.lista_formatos_sequences_byrow.index( self.comboBox_byrow.GetValue() )
        ActivarGrupoClases ( self )

    #===============================================================================
    #    Metodo combobox by row
    #===============================================================================
    def OnClickcboxbyrow ( self, event ):
        self.formato_inputf = 0
        self.formato_sequences = self.lista_formatos_sequences_byrow.index( self.comboBox_byrow.GetValue() )
        ActivarGrupoClases ( self )

    #===============================================================================
    #    Metodo radiobutton by col
    #===============================================================================
    def OnClickradiobycol ( self, event ):
        self.comboBox_bycol.Enable( True )
        self.comboBox_byrow.Enable( False )
        self.checkbox_fastaprotein.Enable( False )
        self.si_fastaprotein = False
        self.formato_inputf = 1
        self.formato_sequences = self.lista_formatos_sequences_bycol.index( self.comboBox_bycol.GetValue() )
        ActivarGrupoClases ( self )

    #===============================================================================
    #    Metodo combobox by row
    #===============================================================================
    def OnClickcboxbycol ( self, event ):
        self.formato_inputf = 1
        self.formato_sequences = self.lista_formatos_sequences_bycol.index( self.comboBox_bycol.GetValue() )
        ActivarGrupoClases ( self )

    #===============================================================================
    #    Metodo radiobutton fasta
    #===============================================================================
    def OnClickradiofasta ( self, event ):
        self.comboBox_byrow.Enable( False )
        self.comboBox_bycol.Enable( False )
        self.checkbox_fastaprotein.Enable( True )
        self.formato_inputf = 2
        self.formato_sequences = 2
        if self.checkbox_fastaprotein.IsChecked():
            self.si_fastaprotein = True
        else:
            self.si_fastaprotein = False
        ActivarGrupoClases ( self )

    #===============================================================================
    #    Metodo checkbox fasta protein
    #===============================================================================
    def OnSelectFastaProtein ( self, event ):
        if self.checkbox_fastaprotein.IsChecked(): # si el checkbox se ha activado
            self.si_fastaprotein = True
        else: # si se ha desactivado el checkbox
            self.si_fastaprotein = False

    #===============================================================================
    #    Metodo radiobutton ms
    #===============================================================================
    def OnClickradioms ( self, event ):
        self.comboBox_byrow.Enable( False )
        self.comboBox_bycol.Enable( False )
        self.checkbox_fastaprotein.Enable( False )
        self.si_fastaprotein = False
        self.formato_inputf = 3
        self.formato_sequences = 1
        ActivarGrupoClases ( self )

    #===============================================================================
    #    Metodo boton ayuda de formato
    #===============================================================================
    def OnClickformatohelp ( self, event ):
        self.helpformato = HelpHtml_v_1_0_imp.MyHtmlFrame( None, 'Quick Help about input format', 'page1', self.raiz_images )
        self.helpformato.SetIcon( wx.Icon( self.raiz_images + 'images/help.ico', wx.BITMAP_TYPE_ICO ) )
        self.helpformato.Center()
        self.helpformato.Show()

#===============================================================================
# Metodos o acciones grupos numero de clases para secuencias numericas
#===============================================================================
    #===============================================================================
    # Metodo radiobutton clases regular
    #===============================================================================
    def OnClickradioregular ( self, event ):
        self.spin_regular_clases.Enable( True )
        self.spin_sigma_clases.Enable( False )
        self.clases_numericas_tipo = 0
        self.clases_n = ''
        self.clases_n = self.spin_regular_clases.GetValue()

    #===============================================================================
    # Metodo spincontrol clases regular
    #===============================================================================
    def OnClickspinregular ( self, event ):
        self.clases_numericas_tipo = 0
        self.clases_n = ''
        self.clases_n = self.spin_regular_clases.GetValue()

    #===============================================================================
    # Metodo radiobutton clases sigma
    #===============================================================================
    def OnClickradiosigma ( self, event ):
        self.spin_sigma_clases.Enable( True )
        self.spin_regular_clases.Enable( False )
        self.clases_numericas_tipo = 1
        self.clases_n = ''
        self.clases_n = self.spin_sigma_clases.GetValue()

    #===============================================================================
    # Metodo spincontrol clases sigma
    #===============================================================================
    def OnClickspinsigma ( self, event ):
        self.clases_numericas_tipo = 1
        self.clases_n = ''
        self.clases_n = self.spin_sigma_clases.GetValue()

    #===============================================================================
    # Metodo boton ayuda de clases
    #===============================================================================
    def OnClickclaseshelp ( self, event ):
        self.helpclases = HelpHtml_v_1_0_imp.MyHtmlFrame( None, 'Quick Help about Classes', 'page2', self.raiz_images )
        self.helpclases.SetIcon( wx.Icon( self.raiz_images + 'images/help.ico', wx.BITMAP_TYPE_ICO ) )
        self.helpclases.Center()
        self.helpclases.Show()


#===============================================================================
# Metodos o acciones grupo tipo de indices
#===============================================================================
    #===============================================================================
    #    Metodo radiobutton clases regular
    #===============================================================================
    def OnClickradioindclassgno ( self, event ):
        self.indices_tipo = 0

    #===============================================================================
    # Metodo spincontrol clases regular
    #===============================================================================
    def OnClickradioindclassglob ( self, event ):
        self.indices_tipo = 1

    #===============================================================================
    #    Metodo radiobutton clases sigma
    #===============================================================================
    def OnClickradioindgno ( self, event ):
        self.indices_tipo = 2

    #===============================================================================
    # Metodo boton ayuda de clases
    #===============================================================================
    def OnClickindiceshelp ( self, event ):
        self.helpindices = HelpHtml_v_1_0_imp.MyHtmlFrame( None, 'Quick Help about Indices levels', 'page3', self.raiz_images )
        self.helpindices.SetIcon( wx.Icon( self.raiz_images + 'images/help.ico', wx.BITMAP_TYPE_ICO ) )
        self.helpindices.Center()
        self.helpindices.Show()

#===============================================================================
# Metodos o acciones list box y check box select all
#===============================================================================
    #===============================================================================
    #    Metodo list box
    #===============================================================================
    def OnSelectItem ( self, event ):
        if self.checkbox_selectall.IsEnabled(): # si el checkbox esta seleccionado
            self.checkbox_selectall.SetValue( False ) # desmarcar el checkbox, se va a marcar uno a uno o por grupo
        self.lista_names_selected = []
        self.lista_sequences_selected = []
        self.lista_casos_selected = []
        self.lista_clases_selected = []
        self.lista_items_selected = []
        self.lista_items_selected[:] = self.list_box.GetSelections() # lista con los indices de los codes seleccionados
        for index in self.lista_items_selected:
            self.lista_names_selected.append( self.lista_casos_names[index] )
            self.lista_sequences_selected.append( self.lista_casos_sequences[index] ) # se ponen en una lista los codes seleccionados
            self.lista_casos_selected.append( self.lista_casos[index] )
            self.lista_clases_selected.append( self.lista_casos_clases[index] )
        if self.si_graph_build:
            self.menuBar.Enable( 21, False )
            self.menuBar.Enable( 22, True )
            self.menuBar.Enable( 31, True )
            ActivarIndicesTipo ( self, True )
        else:
            self.menuBar.Enable( 21, True )
            self.menuBar.Enable( 22, False )
            self.menuBar.Enable( 31, False )
            ActivarIndicesTipo ( self, False )

    #===============================================================================
    # Metodo checkbox selectall
    #===============================================================================
    def OnSelectAllItem ( self, event ):
        if self.checkbox_selectall.IsChecked(): # si el checkbox se ha activado
            self.lista_names_selected = []
            self.lista_sequences_selected = []
            self.lista_clases_selected = []
            self.lista_items_selected = []
            for index in range( self.list_box.GetCount() ): # el .GetCount() da el total de items de la listbox
                self.list_box.SetSelection( index, True ) # marca todos los items de la listbox uno a uno
                self.lista_names_selected.append( self.lista_casos_names[index] )
                self.lista_sequences_selected.append( self.lista_casos_sequences[index] ) # pone todos los codes uno a uno en una lista
                self.lista_casos_selected.append( self.lista_casos[index] )
                self.lista_clases_selected.append( self.lista_casos_clases[index] )
            self.lista_items_selected[:] = range( self.list_box.GetCount() ) # Crea una lista de los indices de cada code
            if self.si_graph_build:
                self.menuBar.Enable( 21, False )
                self.menuBar.Enable( 22, True )
                self.menuBar.Enable( 31, True )
                ActivarIndicesTipo ( self, True )
            else:
                self.menuBar.Enable( 21, True )
                self.menuBar.Enable( 22, False )
                self.menuBar.Enable( 31, False )
                ActivarIndicesTipo ( self, False )
                
        else: # si se ha desactivado el checkbox
            for index in range( self.list_box.GetCount() ):
                self.list_box.SetSelection( index, False ) # se desmarcan todos los items de la listbox uno a uno
                self.lista_names_selected = []
                self.lista_sequences_selected = []
                self.lista_casos_selected = []
                self.lista_clases_selected = []
                self.lista_items_selected = []
            self.menuBar.Enable( 21, False )
            self.menuBar.Enable( 22, False )
            self.menuBar.Enable( 31, False )
            ActivarIndicesTipo ( self, False )

#===============================================================================
# Metodo para mensaje de alerta por problemas de formato o falta de datos
#===============================================================================
    def Alerta( self, texto, nombre ):
        dlg_no_codes = wx.MessageDialog( None, texto, nombre, wx.OK | wx.ICON_ERROR )
        dlg_no_codes.ShowModal()
        dlg_no_codes.Destroy()
        return

#===============================================================================
# Metodo barra de avance en la barra de estado
#===============================================================================
    def AvanGauge( self, event ):
        self.countgauge += 1
        if self.countgauge >= 60:
                self.countgauge = 0
        self.StatusBar.SetStatusText( 'Progress :', 1 )
        self.StatusBar.SetStatusText( '|'*self.countgauge, 2 )


#===============================================================================


#===============================================================================
# Funciones generales fuera de la Clase MyMenu
#===============================================================================

#===============================================================================
# Funcion para activar el grupo tipo de indices 
#===============================================================================
def ActivarIndicesTipo ( self, accion ):
    self.rbindices_classgnomones.Enable( accion )
    self.rbindices_classglobal.Enable( accion )
    self.rbindices_gnomones.Enable( accion )
    self.bitmapButton_indices_help.Enable( accion )

#===============================================================================
# Funcion para activar el grupo de numero de clases numericas
#===============================================================================
def ActivarGrupoClases ( self ):
    if self.formato_sequences == 1:
        self.format_numclass_staticbox.Enable( True )
        self.rbnumclases_regular.Enable( True )
        self.rbnumclases_regular_continua.Enable( True )
        self.spin_regular_clases.Enable( True )
        self.rbnumclases_sigma.Enable( True )
        self.rbnumclases_sigma_continua.Enable( True )
        self.spin_regular_clases.Enable( True )
        self.bitmapButton_clases_help.Enable( True )
    else:
        self.format_numclass_staticbox.Enable( False )
        self.rbnumclases_regular.Enable( False )
        self.rbnumclases_regular_continua.Enable( False )
        self.spin_regular_clases.Enable( False )
        self.rbnumclases_sigma.Enable( False )
        self.rbnumclases_sigma_continua.Enable( False )
        self.spin_regular_clases.Enable( False )
        self.bitmapButton_clases_help.Enable( False )


#===============================================================================


#===============================================================================
#    Clase Principal de la aplicacion
#===============================================================================
class MyApp( wx.App ):
    """Application class."""
    def OnInit( self ):
        frame = MyMenu( None, -1, 'CULSPIN' )
        frame.SetIcon( wx.Icon( orig_dir + 'images/icon.ico', wx.BITMAP_TYPE_ICO ) )
        frame.Centre()
        frame.Show()
        MySplash( frame, duration = 3000 )
        return True


#===============================================================================


#===============================================================================
# Funcion main
#===============================================================================
def main():
    app = MyApp()
    app.MainLoop()



#===============================================================================

if __name__ == '__main__':
    main()

