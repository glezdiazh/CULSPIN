#!/usr/bin/env python
# -*- coding: cp1252 -*- 
# main window


import numpy
import math
import os, sys


'''
Created on 06/05/2009

@author: Chachy
'''

#===============================================================================
# Descripcion:
# Funciones para fitrar los datos leidos de los ficheros (evaluan si su formato
# concuerda con el seleccionado). Hacen las transformaciones necesarias para
# entregar los datos en una lista "self.data" que contiene las secuencias en el
# formato "nameCase Sequence"
#===============================================================================

#===============================================================================
# Filtro para el formato de datos by rows letras
#===============================================================================
def filtroByRowsLett( self ):
    linea = ""
    caso = 0

    for linea in self.data[0]:
        self.AvanGauge( self )
        if linea.count( ' ' ) > 1: # Si hay mas de un espacio en alguna de las lineas del fichero
            many_spaces_txt = """
            Incorrect format, some line has too many spaces. In the
            opcion selected the data-format has to be:
            name<space>letter sequence whithout white space."""
            self.Alerta(many_spaces_txt, 'Format Problem')
            return
        elif not linea.count( ' ' ): # Si no hay espacio en blanco en alguna de las lineas del fichero
            missing_spaces_txt = """
            Incorrect format, some sequence has not name or you forgot
            to put a space as separator. In the opcion selected the
            data-format has to be:
            name<space>letter sequence whithout white space."""
            self.Alerta(missing_spaces_txt, 'Format Problem')
            return
        else:  # Si hay en un solo espacio en blanco en cada linea
            if not ''.join( linea[linea.index( ' ' ) + 1:-1].split() ).isalpha():
                columnas_txt = """
                Incorrect format, some sequence has not alphabetical
                code."""
                self.Alerta( columnas_txt, 'Format Problem' )
                return
            self.lista_casos_names.append( linea[:linea.find( ' ' )] )
            self.lista_casos_sequences.append( linea[linea.find( ' ' ) + 1:-1] ) # Utilizo index inf +1 para no coger el ' '
            self.lista_casos.append( self.lista_casos_names[caso] + ' ' * 3 + self.lista_casos_sequences[caso] ) # Utilizo -1 para quitar los \n
            caso += 1

    for seq in self.lista_casos_sequences:
        self.AvanGauge( self )
        clases = []
        for letra in seq:
            if not letra in clases:
                clases.append( letra )
        self.lista_casos_clases.append( clases )

    return

#===============================================================================
# Filtro para el formato de datos by rows number. Codifica numeros con letras
#===============================================================================
def filtroByRowsNum( self ):
    linea = ""

    for linea in self.data[0]:
        self.AvanGauge( self )
        if linea.count( ' ' ) < 2: # Si no hay espacio en blanco en alguna de las lineas del fichero
            missing_spaces_txt = """
            Incorrect format, some sequence in datafile has not name,
            is a one-element sequence or you forgot to put a space as
            separator. In the opcion selected the data-format has to be:
            name<space>numeric sequence separated by white spaces."""
            self.Alerta( missing_spaces_txt, 'Format Problem')
            return
        else:
            if not linea[linea.find( ' ' ) + 1:-1].replace( ' ', '' ).replace( '.', '' ).replace( 'e', '' ).replace( 'E', '' ).replace( '-', '' ).replace( '+', '' ).isdigit():
                char_no_deseados_txt = """
                Incorrect format, some sequence in datafile has some
                undesired caracters. In the opcion selected the data-
                format has to be:
                name<space>numeric sequence separated by speces."""
                self.Alerta( char_no_deseados_txt, 'Format Problem' )
                return
            else:
                self.lista_casos_names.append( linea[:linea.find( ' ' )] )
                self.data_numerica.append( [float( val ) for val in linea[linea.find( ' ' ) + 1:].split()] )

    Asignar_Letras_A_Seq_Num ( self )
    return

#===============================================================================
# Filtro para formato datos by col letras. Traspone la data depues de filtrarla
#===============================================================================
def filtroByColLett( self ):
    linea = ""

    if len( self.data[0][0].split() ) < len( self.data[0][0].split( ' ' ) ):
        columnas_txt = """
        Incorrect format, some sequences in datafile has not name."""
        self.Alerta( columnas_txt, 'Format Problem' )
        return

    for linea in self.data[0][1:]:
        self.AvanGauge( self )
        if len( linea.split( ' ' ) ) < len( self.data[0][0].split( ' ' ) ):
            columnas_txt = """
            Incorrect format, unexpected return in some line."""
            self.Alerta( columnas_txt, 'Format Problem' )
            return

        if len( linea.split( ' ' ) ) > len( self.data[0][0].split( ' ' ) ):
            columnas_txt = """
            Incorrect format, unexpected fragment of column in
            some line."""
            self.Alerta( columnas_txt, 'Format Problem' )
            return

        for col in range( len( self.data[0][0].split( ' ' ) ) ):
            if len( linea[:-1].split( ' ' )[col] ) > 1:
                letras_txt = """
                Incorrect format, some line has more than one
                code letter."""
                self.Alerta( letras_txt, 'Format Problem' )
                return

            if not ''.join( linea[:-1].split() ).isalpha():
                noletra_txt = """
                Incorrect format, some line has not alphabetical
                code."""
                self.Alerta( noletra_txt, 'Format Problem' )
                return

    for name in self.data[0][0][:-1].split( ' ' ):
        self.lista_casos_names.append( name )

    for caso in range( len( self.lista_casos_names ) ):
        self.AvanGauge( self )
        seq = ''
        for linea in self.data[0][1:]:
            letras = linea[:-1].split( ' ' )
            if letras[caso]:
                seq += letras[caso]
        self.lista_casos_sequences.append( seq )
        self.lista_casos.append( self.lista_casos_names[caso] + ' ' * 3 + self.lista_casos_sequences[caso] )

    for seq in self.lista_casos_sequences:
        self.AvanGauge( self )
        clases = []
        for letra in seq:
            if not letra in clases:
                clases.append( letra )
        self.lista_casos_clases.append( clases )

    return

#===============================================================================
# Filtro para formato datos by col numeros. Codifica numeros con letras y traspone la data
#===============================================================================
def filtroByColNum( self ):
    linea = ""
    if len( self.data[0][0].split() ) < len( self.data[0][0].split( ' ' ) ):
        nombres_txt = """
        Incorrect format, some sequences in datafile has not name."""
        self.Alerta( nombres_txt, 'Format Problem' )
        return

    for linea in self.data[0][1:]:
        self.AvanGauge( self )
        if len( linea.split( ' ' ) ) < len( self.data[0][0].split( ' ' ) ):
            retorno_txt = """
            Incorrect format, unexpected return in some line."""
            self.Alerta( retorno_txt, 'Format Problem', )
            return

        if len( linea.split( ' ' ) ) > len( self.data[0][0].split( ' ' ) ):
            columnas_txt = """
            Incorrect format, unexpected fragment of column in
            some line."""
            self.Alerta( columnas_txt, 'Format Problem' )
            return

        for col in range( len( linea.split( ' ' ) ) ):
            if linea.split( ' ' )[col] and linea.split( ' ' )[col] != '\n':
                if not linea.split( ' ' )[col].replace( ' ', '' ).replace( '\n', '' ).replace( '.', '' ).replace( 'e', '' ).replace( 'E', '' ).replace( '-', '' ).replace( '+', '' ).isdigit():
                    char_no_deseados_txt = """
                    Incorrect format, some sequence in datafile has not
                    numeric caracters."""
                    self.Alerta( char_no_deseados_txt, 'Format Problem' )
                    return

    data_v = []
    self.lista_casos_names = self.data[0][0][:-1].split( ' ' )

    for linea in self.data[0][1:]:
        data_v.append( linea.split( ' ' ) )

    for col in range( len( data_v[0] ) ):
        data_h = []
        for lin in range( len( data_v ) ):
            if data_v[lin][col] and data_v[lin][col] != '\n':
                data_h.append( data_v[lin][col] )
        self.data_numerica.append( [float( val ) for val in data_h] )

    Asignar_Letras_A_Seq_Num ( self )
    return

#===============================================================================
# Filtro formato datos fasta. Ademas codifica en 5 clases y se selecciona checbox protein
#===============================================================================
def filtroFasta( self ):
    ini=[]
    fin=[]
    datatemp = []
    
    for i,linea in enumerate(self.data[0]):
        self.AvanGauge( self )
        if linea[0] == '>':
            ini.append(i)
        if linea =='\n':
            fin.append(i)

    if not len(ini):
        noFasta_txt = """
        Incorrect format, it is not a FASTA file."""
        self.Alerta( noFasta_txt, 'Format Problem' )
        return

    if len(ini)>len(fin):
        for i,f in zip(ini[:-1],fin):
            datatemp.append(self.data[0][i:f])
        datatemp.append(self.data[0][ini[-1]:])
    elif len(ini)<len(fin):
        a=len(ini)
        for i,f in zip(ini,fin[:a]):
            datatemp.append(self.data[0][i:f])
    else:
        for i,f in zip(ini,fin):
            datatemp.append(self.data[0][i:f])

    for d in datatemp:
        self.AvanGauge( self )
        if d[0].count('|')<2 or not d[0][d[0].find( '|' ) + 1:d[0].find( '|', d[0].find( '|' ) + 1 )].isdigit():
            noFasta_txt = """
            Incorrect format, it is not a FASTA file or
            has some corrupt name-sequence."""
            self.Alerta( noFasta_txt, 'Format Problem' )
            return
        self.lista_casos_names.append( d[0][1:d[0].find( '|', d[0].find( '|' ) + 1 )].replace('|',' ').replace(' ',''))
        
        if ''.join(''.join(d[1:]).split('\n')).count(' '):
            many_spaces_txt = """
            Incorrect format, some sequence has undesired white spaces."""
            self.Alerta( many_spaces_txt, 'Format Problem' )
            return

        if not self.si_fastaprotein:
            # Reducir a un maximo de 21 clases las secuencias con aa desconocidos a los que ponen otras letras como X
            reducea21 = ''
            original = ''
            original = ''.join(''.join(d[1:]).split('\n'))
            for let in original:
                if let in self.codes_letras:
                    reducea21 += let
                else:
                    reducea21 += 'X'
            self.lista_casos_sequences.append( reducea21 )
            
        else:
            encode = ''
            original = ''
            original = ''.join(''.join(d[1:]).split('\n'))
            for let in original:
                if let in self.codes_forfastaprot:
                    encode += self.codes_forfastaprot[let]
                else:
                    encode += 'X'
            self.lista_casos_sequences.append( encode )

    for name, seq in zip(self.lista_casos_names, self.lista_casos_sequences):
        self.lista_casos.append( name + ' ' * 3 + seq )

    self.data[0][:] = datatemp

    for seq in self.lista_casos_sequences:
        self.AvanGauge( self )
        clases = []
        for letra in seq:
            if not letra in clases:
                clases.append( letra )
        self.lista_casos_clases.append( clases )

    return

#===============================================================================
# Filtro formato datos ms. Transforma data en serie numerica multiplicando m/s por
# intensidad. Codifica esta serie numerica con letras y la traspone.
#===============================================================================
def filtroMs( self ):

    self.data_numerica = []

    if self.input_file_csv:
        sep = ','
    else:
        sep = '\t'
    for file in range( len( self.input_file_names ) ):
        linea = ""
        if not self.data[file][0].replace( sep, '' ).replace( '\n', '' ).replace( '.', '' ).replace( 'e', '' ).replace( 'E', '' ).replace( '-', '' ).replace( '+', '' ).isdigit():
            inicio = 1
        else:
            inicio = 0
        for linea in self.data[file][inicio:]:
            self.AvanGauge( self )
            if len( linea.split( sep ) ) < 2 :
                columnas_txt = """
                Incorrect format, unexpected return in some line.
                Incomplet m/z, intensity or incorrect separator."""
                self.Alerta( columnas_txt, 'Format Problem' )
                return

            if len( linea.split( sep ) ) > 2:
                columnas_txt = """
                Incorrect format, unexpected fragment of column in
                some line."""
                dlg_missing_spaces = wx.MessageDialog( columnas_txt, 'Format Problem' )
                return

            for col in range( 2 ):
                if linea.split( sep )[col]:
                    self.AvanGauge( self )
                    if not linea.split( sep )[col].replace( ' ', '' ).replace( '\n', '' ).replace( '.', '' ).replace( 'e', '' ).replace( 'E', '' ).replace( '-', '' ).replace( '+', '' ).isdigit():
                        char_no_deseados_txt = """
                        Incorrect format, some sequence in datafile has not
                        numerics caracters."""
                        self.Alerta( char_no_deseados_txt, 'Format Problem' )
                        return

        self.data_numerica.append( [float( linea.split( sep )[0] ) * float( linea.split( sep )[1][:-1] ) for linea in self.data[file][inicio:]] )

    for file in self.input_file_names:
        self.lista_casos_names.append( file[:file.find( '.' )] )

    Asignar_Letras_A_Seq_Num ( self )
    return

#===============================================================================
# Funcion de uso comun cuando se necesita asignar codigos de letra a las secuencias numericas
#===============================================================================
def Asignar_Letras_A_Seq_Num ( self ):
    
    serie = ''
    for serie in self.data_numerica:
        if self.clases_numericas_tipo == 0:
            minimo = min( serie )
            maximo = max( serie )
            intervalo = ( maximo - minimo ) / float( self.clases_n )
            rangos_clases = []
            seq = ''
            for n in range( int( self.clases_n ) ):
                inferior = minimo + n * intervalo
                superior = inferior + intervalo
                rangos_clases.append( [inferior, superior] )
            for signal in serie:
                for rango in range( len( rangos_clases ) ):
                    self.AvanGauge( self )
                    if rangos_clases[rango][0] <= signal <= rangos_clases[rango][1]:
                        letra = self.codes_letras[rango]
                seq += letra
            self.lista_casos_sequences.append( seq )

        if self.clases_numericas_tipo == 1:
            media = numpy.mean( serie )
            sdesv = numpy.std( serie )
            rangos_clases = []
            seq = ''
            for n in range( -int( self.clases_n ) , int( self.clases_n ) ):
                inferior = media + n * sdesv / 2
                superior = inferior + sdesv / 2
                rangos_clases.append( [inferior, superior] )
            for signal in serie:
                letra = ''
                for rango in range( len( rangos_clases ) ):
                    self.AvanGauge( self )
                    if rangos_clases[rango][0] <= signal <= rangos_clases[rango][1]:
                        letra = self.codes_letras[rango]
                if not letra:
                    if signal < media:
                        letra = self.codes_letras[len( rangos_clases )]
                    else:
                        letra = self.codes_letras[len( rangos_clases ) + 1]
                seq += letra
            self.lista_casos_sequences.append( seq )

    for name, secu in zip( self.lista_casos_names, self.lista_casos_sequences ):
        self.lista_casos.append( name + ' ' * 3 + secu )

    for seq in self.lista_casos_sequences:
        self.AvanGauge( self )
        clases = []
        for letra in seq:
            if not letra in clases:
                clases.append( letra )
        self.lista_casos_clases.append( clases )

    return


