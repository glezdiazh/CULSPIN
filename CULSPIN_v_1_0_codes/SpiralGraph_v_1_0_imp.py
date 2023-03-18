#!/usr/bin/env python
# -*- coding: cp1252 -*- 
# main window


'''
Created on 06/05/2009

@author: Chachy
'''

#===============================================================================
# Descriptions:
# Modulo que dibuja y muestra el grafico de la spiral
#===============================================================================

import wx.lib.dragscroller
import math

class spiral_graph(wx.ScrolledWindow):
    def __init__(self, parent,ct_1,ct_2,ct_coord,ct_conect,dimen,l_r):
        wx.ScrolledWindow.__init__(self, parent)

        
        self.l_r = l_r # longitud del radio de los circulos que representan los nodos
        self.l_e = l_r*3 #longitud del enlace o arista que une los nodos
        self.dimen = dimen*self.l_e + self.l_e #dimenencion del grafico teniendo en cuenta l_e y num de col y filas

        #===============================================================================
        #    Establecer el punto central del grafico. Es la referencia para comienzar
        #    a dibubar la espiral
        #===============================================================================
        if dimen%2:
            self.xo = int(self.dimen/2)
            self.yo = int(self.dimen/2)+ self.l_e
        else:
            self.xo = int(self.dimen/2)+ self.l_e
            self.yo = int(self.dimen/2)+ self.l_e

        #===============================================================================
        #    Iniciacion de las variables con los datos de la espiral
        #===============================================================================
        self.nombre = ct_1
        self.nodos = ct_2[0]
        self.edges = ct_2[1]
        self.coordxy = ct_coord
        self.enlaces = ct_conect

        #===============================================================================
        #    Lista con colores para los nodos de difentes clases
        #===============================================================================
        self.colores = ['red','sky blue','plum','spring green','cyan','white','wheat','coral','gray','purple',
                        'medium goldenrod','orchid','pink','turquoise','lime green','khaki','tan','light blue',
                        'light gray','gold','magenta','cadet blue','green yellow','medium violet red','dim gray',
                        'orange','aquamarine','blue violet','yellow','medium orchid','violet red','green','goldenrod',
                        'orange red','medium blue','sea green','light steel blue','yellow green','medium turquoise',
                        'pale green','medium aquamarine','medium spring green','slate blue','medium sea green','steel blue',
                        'forest green','medium slate blue']

        #===============================================================================
        #    Eventos que redireccion a los metodos de pintar la espiral y de mover las barras
        #    de desplazamiento vertical y horizontal en el caso de espirales muy grandes
        #===============================================================================
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_RIGHT_DOWN, self.OnRightDown)
        self.Bind(wx.EVT_RIGHT_UP, self.OnRightUp)

        #===============================================================================
        #    Define region que sera gobernada por las barras de desplazamiento
        #===============================================================================
        self.SetScrollbars(1, 1, self.dimen, self.dimen , 0, 0)
        self.scroller = wx.lib.dragscroller.DragScroller(self)

    #===============================================================================
    #    Metodo que dibuja la espiral
    #===============================================================================
    def OnPaint(self, evt):
        dc = wx.PaintDC(self)
        self.DoPrepareDC(dc)

        #===============================================================================
        #    Define el color y grosor del trazado dependiendo del tamaño de la espiral
        #===============================================================================
        if self.l_r >= 6:
            dc.SetPen(wx.Pen("black", 2))
        else:
            dc.SetPen(wx.Pen("black", 1))

        #===============================================================================
        #    No colorear el interior de lo que se dibuje
        #===============================================================================
        dc.SetBrush(wx.TRANSPARENT_BRUSH)

        #===============================================================================
        #    Dibujar las aristas o enlaces entre los nodo x1,y1 y nodo x2,y2
        #===============================================================================
        for i in range(self.edges):
            x1 = self.coordxy[(self.enlaces[i][0])-1][0]
            y1 = self.coordxy[(self.enlaces[i][0])-1][1]
            x2 = self.coordxy[(self.enlaces[i][1])-1][0]
            y2 = self.coordxy[(self.enlaces[i][1])-1][1]

            dc.DrawLine(self.xo+x1*self.l_e,self.yo+y1*self.l_e,self.xo+x2*self.l_e,self.yo+y2*self.l_e)

        
        #===============================================================================
        #    Reduce el grosor del trazado que se utilizara para dibujar los circulos(nodos)
        #===============================================================================
        dc.SetPen(wx.Pen("black", 1))

        #===============================================================================
        #    Dibujar los nodos mediantes circulos con un color diferente para cada clase y 
        #    colocar la letra de la clase en el interior del circulo
        #===============================================================================
        letras = [] 
        for i in range(self.nodos):
            x = self.coordxy[i][0]
            y = self.coordxy[i][1]
            letra = self.coordxy[i][3]

            if letra not in letras:
                letras.append(letra)

            #===============================================================================
            #    Establece el color del circulo segun la clase correspondiente
            #===============================================================================
            color = self.colores[letras.index(letra)]
            dc.SetBrush(wx.Brush(color))

            #===============================================================================
            #    Dibuja el circulo
            #===============================================================================
            dc.DrawCircle(self.xo+x*self.l_e, self.yo+y*self.l_e, self.l_r)

        #===============================================================================
        #    Colocar en el centro de cada circulo la letra de la clase correspondiente, en espirales
        #    grandes no es factible en aras de poder representarlas
        #===============================================================================
        if self.l_r >= 6:
            dc.SetPen(wx.Pen("black", 1))
            dc.SetBrush(wx.TRANSPARENT_BRUSH)
            dc.SetFont(wx.Font(self.l_r,wx.ROMAN,wx.NORMAL,wx.BOLD))

            for i in range(self.nodos):
                x = self.coordxy[i][0]
                y = self.coordxy[i][1]
                letra = self.coordxy[i][3]

                (Lw,Lh) = dc.GetTextExtent(letra)

                dc.DrawText(letra, (self.xo+self.l_e*x)-Lw/2, (self.yo+self.l_e*y)-Lh/2)

    #===============================================================================
    #    Metodo barra desplazamiento en movimiento
    #===============================================================================
    def OnRightDown(self, event):
        self.scroller.Start(event.GetPosition())

    #===============================================================================
    #    Metodo detener desplazamiento
    #===============================================================================
    def OnRightUp(self, event):
        self.scroller.Stop()

#===============================================================================
# clase que crea la ventana de representacion
#===============================================================================
class SpiralFrame(wx.Frame):
    def __init__(self,ct_1,ct_2,ct_coord,ct_conect,dimen):

        #===============================================================================
        #    Define un factor para manejar el tamaño de la ventana, margenes, los
        #    circulos que representan los nodos, las lineas de las aristas, las 
        #    letras, etc, segun segun las dimensiones de la expiral.
        #===============================================================================
        if dimen >= 45: # espirales muy grandes
            l_r = 2
        elif 33 <= dimen < 45: # espirales grandes  
            l_r = 6
        elif 26 <= dimen < 33: # espirales medianas
            l_r = 8
        else: # espirales pequeñas
            l_r = 10

        extra = 100 # valor para manejar los margenes espiral borde la ventana

        wx.Frame.__init__(self, None, title = ct_1 +' in Ulam Spiral representation',
                          size=(dimen*3*l_r+3*l_r+extra,dimen*3*l_r+3*l_r+extra))

        self.SetBackgroundColour('white') # Asigna el color blanco al fondo de la ventana
        
        #===============================================================================
        #    Manda a dibujar la espiral en la ventana
        #===============================================================================
        self.plot = spiral_graph(self,ct_1,ct_2,ct_coord,ct_conect, dimen, l_r)


#===============================================================================
# clase principal
#===============================================================================
#===============================================================================
# class principal:
#    ct_1 = '11Hb[117]'
#    ct_2 = [116, 150]
#    ct_coord = [[0, 0, 0, 'G'], [1, 0, 0, 'D'], [1, -1, 0, 'D'], [0, -1, 0, 'G'], [-1, -1, 0, 'G'], [-1, 0, 0, 'D'], [-1, 1, 0, 'G'], [0, 1, 0, 'G'], [1, 1, 0, 'G'], [2, 1, 0, 'G'], [2, 0, 0, 'G'], [2, -1, 0, 'G'], [2, -2, 0, 'G'], [1, -2, 0, 'G'], [0, -2, 0, 'D'], [-1, -2, 0, 'G'], [-2, -2, 0, 'G'], [-2, -1, 0, 'G'], [-2, 0, 0, 'D'], [-2, 1, 0, 'G'], [-2, 2, 0, 'D'], [-1, 2, 0, 'D'], [0, 2, 0, 'G'], [1, 2, 0, 'G'], [2, 2, 0, 'G'], [3, 2, 0, 'D'], [3, 1, 0, 'G'], [3, 0, 0, 'G'], [3, -1, 0, 'G'], [3, -2, 0, 'D'], [3, -3, 0, 'G'], [2, -3, 0, 'D'], [1, -3, 0, 'G'], [0, -3, 0, 'G'], [-1, -3, 0, 'D'], [-2, -3, 0, 'G'], [-3, -3, 0, 'D'], [-3, -2, 0, 'D'], [-3, -1, 0, 'D'], [-3, 0, 0, 'D'], [-3, 1, 0, 'G'], [-3, 2, 0, 'G'], [-3, 3, 0, 'G'], [-2, 3, 0, 'G'], [-1, 3, 0, 'G'], [0, 3, 0, 'D'], [1, 3, 0, 'G'], [2, 3, 0, 'G'], [3, 3, 0, 'D'], [4, 3, 0, 'D'], [4, 2, 0, 'G'], [4, 1, 0, 'G'], [4, 0, 0, 'G'], [4, -1, 0, 'G'], [4, -2, 0, 'G'], [4, -3, 0, 'G'], [4, -4, 0, 'G'], [3, -4, 0, 'G'], [2, -4, 0, 'G'], [1, -4, 0, 'G'], [0, -4, 0, 'G'], [-1, -4, 0, 'G'], [-2, -4, 0, 'G'], [-3, -4, 0, 'G'], [-4, -4, 0, 'G'], [-4, -3, 0, 'G'], [-4, -2, 0, 'K'], [-4, -1, 0, 'K'], [-4, 0, 0, 'K'], [-4, 1, 0, 'K'], [-4, 2, 0, 'K'], [-4, 3, 0, 'A'], [-4, 4, 0, 'A'], [-3, 4, 0, 'A'], [-2, 4, 0, 'K'], [-1, 4, 0, 'K'], [0, 4, 0, 'A'], [1, 4, 0, 'K'], [2, 4, 0, 'K'], [3, 4, 0, 'K'], [4, 4, 0, 'K'], [5, 4, 0, 'K'], [5, 3, 0, 'K'], [5, 2, 0, 'A'], [5, 1, 0, 'A'], [5, 0, 0, 'A'], [5, -1, 0, 'K'], [5, -2, 0, 'K'], [5, -3, 0, 'K'], [5, -4, 0, 'K'], [5, -5, 0, 'A'], [4, -5, 0, 'K'], [3, -5, 0, 'K'], [2, -5, 0, 'K'], [1, -5, 0, 'K'], [0, -5, 0, 'K'], [-1, -5, 0, 'A'], [-2, -5, 0, 'A'], [-3, -5, 0, 'K'], [-4, -5, 0, 'K'], [-5, -5, 0, 'K'], [-5, -4, 0, 'K'], [-5, -3, 0, 'K'], [-5, -2, 0, 'K'], [-5, -1, 0, 'K'], [-5, 0, 0, 'K'], [-5, 1, 0, 'K'], [-5, 2, 0, 'A'], [-5, 3, 0, 'A'], [-5, 4, 0, 'K'], [-5, 5, 0, 'K'], [-4, 5, 0, 'A'], [-3, 5, 0, 'A'], [-2, 5, 0, 'A'], [-1, 5, 0, 'A'], [0, 5, 0, 'A']]
#    ct_conect = [[1, 2, 1, 1], [2, 3, 1, 1], [3, 4, 1, 1], [4, 5, 1, 1], [5, 6, 1, 1], [6, 7, 1, 1], [7, 8, 1, 1], [8, 9, 1, 1], [9, 10, 1, 1], [10, 11, 1, 1], [11, 12, 1, 1], [12, 13, 1, 1], [13, 14, 1, 1], [14, 15, 1, 1], [15, 16, 1, 1], [16, 17, 1, 1], [17, 18, 1, 1], [18, 19, 1, 1], [19, 20, 1, 1], [20, 21, 1, 1], [21, 22, 1, 1], [22, 23, 1, 1], [23, 24, 1, 1], [24, 25, 1, 1], [25, 26, 1, 1], [26, 27, 1, 1], [27, 28, 1, 1], [28, 29, 1, 1], [29, 30, 1, 1], [30, 31, 1, 1], [31, 32, 1, 1], [32, 33, 1, 1], [33, 34, 1, 1], [34, 35, 1, 1], [35, 36, 1, 1], [36, 37, 1, 1], [37, 38, 1, 1], [38, 39, 1, 1], [39, 40, 1, 1], [40, 41, 1, 1], [41, 42, 1, 1], [42, 43, 1, 1], [43, 44, 1, 1], [44, 45, 1, 1], [45, 46, 1, 1], [46, 47, 1, 1], [47, 48, 1, 1], [48, 49, 1, 1], [49, 50, 1, 1], [50, 51, 1, 1], [51, 52, 1, 1], [52, 53, 1, 1], [53, 54, 1, 1], [54, 55, 1, 1], [55, 56, 1, 1], [56, 57, 1, 1], [57, 58, 1, 1], [58, 59, 1, 1], [59, 60, 1, 1], [60, 61, 1, 1], [61, 62, 1, 1], [62, 63, 1, 1], [63, 64, 1, 1], [64, 65, 1, 1], [65, 66, 1, 1], [66, 67, 1, 1], [67, 68, 1, 1], [68, 69, 1, 1], [69, 70, 1, 1], [70, 71, 1, 1], [71, 72, 1, 1], [72, 73, 1, 1], [73, 74, 1, 1], [74, 75, 1, 1], [75, 76, 1, 1], [76, 77, 1, 1], [77, 78, 1, 1], [78, 79, 1, 1], [79, 80, 1, 1], [80, 81, 1, 1], [81, 82, 1, 1], [82, 83, 1, 1], [83, 84, 1, 1], [84, 85, 1, 1], [85, 86, 1, 1], [86, 87, 1, 1], [87, 88, 1, 1], [88, 89, 1, 1], [89, 90, 1, 1], [90, 91, 1, 1], [91, 92, 1, 1], [92, 93, 1, 1], [93, 94, 1, 1], [94, 95, 1, 1], [95, 96, 1, 1], [96, 97, 1, 1], [97, 98, 1, 1], [98, 99, 1, 1], [99, 100, 1, 1], [100, 101, 1, 1], [101, 102, 1, 1], [102, 103, 1, 1], [103, 104, 1, 1], [104, 105, 1, 1], [105, 106, 1, 1], [106, 107, 1, 1], [107, 108, 1, 1], [108, 109, 1, 1], [109, 110, 1, 1], [110, 111, 1, 1], [111, 112, 1, 1], [112, 113, 1, 1], [113, 114, 1, 1], [114, 115, 1, 1], [115, 116, 1, 1], [1, 4, 1, 1], [1, 8, 1, 1], [5, 16, 1, 1], [5, 18, 1, 1], [6, 19, 1, 1], [7, 20, 1, 1], [8, 23, 1, 1], [9, 24, 1, 1], [10, 25, 1, 1], [10, 27, 1, 1], [11, 28, 1, 1], [12, 29, 1, 1], [14, 33, 1, 1], [17, 36, 1, 1], [19, 40, 1, 1], [20, 41, 1, 1], [24, 47, 1, 1], [25, 48, 1, 1], [26, 49, 1, 1], [27, 52, 1, 1], [28, 53, 1, 1], [29, 54, 1, 1], [31, 58, 1, 1], [31, 56, 1, 1], [33, 60, 1, 1], [34, 61, 1, 1], [36, 63, 1, 1], [67, 104, 1, 1], [68, 105, 1, 1], [69, 106, 1, 1], [70, 107, 1, 1], [72, 109, 1, 1], [73, 112, 1, 1], [74, 113, 1, 1], [77, 116, 1, 1]]
#    if math.sqrt(ct_2[0]) == int(math.sqrt(ct_2[0])): # si es un entero
#        dimen = (int( math.sqrt( ct_2[0]))-1 )* 30 + 200
#    else: # si la raiz de tope no es un entero
#        dimen = (int( math.sqrt( ct_2[0])))* 30 + 200
#    app = wx.PySimpleApp()
#    dlg_spiral = wx.MessageDialog(None, 'Desea ver la Spiral','Graph Spiral', wx.OK | wx.CANCEL | wx.ICON_INFORMATION)
#    if dlg_spiral.ShowModal() == wx.ID_OK:
#        dlg_spiral.Destroy()
#        ventana = SpiralFrame (ct_1,ct_2,ct_coord,ct_conect,dimen)
#        ventana.Show()
#        app.MainLoop() 
# #------------------------------------------------------------------------------ 
# if __name__ == '__main__':
#    principal
#===============================================================================
