#!/usr/bin/env python
# -*- coding: cp1252 -*- 
# main window


'''
Created on 06/05/2009

@author: Chachy
'''


#===============================================================================
# Descripcion:
# Modulo para colocar los indices calculados en un grid para mostrarselos al usuario.
# Ademas permite selecionar datos para copiarlos en el clipboard mediante ctrl+C para
# luego pegarlos en excel y trabajar con ellos.
#===============================================================================


import  wx
import  wx.grid as  gridlib


#===============================================================================
# Clase para rellenar una tabla con los indices y encabezados como base para el grid
#===============================================================================
class HugeTable(gridlib.PyGridTableBase):
    def __init__(self, log, colLabels, rowLabels, data_indices):
        gridlib.PyGridTableBase.__init__(self)

        self.colLabels = colLabels
        self.rowLabels = rowLabels
        self.data_indices = data_indices
        self.odd=gridlib.GridCellAttr()
        self.odd.SetBackgroundColour('white')
        self.even=gridlib.GridCellAttr()
        self.even.SetBackgroundColour(wx.Colour(201,219,255))

    def GetAttr(self, row, col, kind):
        attr = [self.even, self.odd][row % 2]
        attr.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.NORMAL))
        attr.IncRef()
        return attr

    def GetNumberRows(self):
        return len(self.data_indices)

    def GetNumberCols(self):
        return len(self.data_indices[0])

    def GetColLabelValue(self, col):
        if self.colLabels:
            return self.colLabels[col]

    def GetRowLabelValue(self, row):
        if self.rowLabels:
            return self.rowLabels[row]

    def IsEmptyCell(self, row, col):
        return False

    def GetValue(self, row, col):
        return self.data_indices[row][col]

    def SetValue(self, row, col, value):
        self.log.write(row,col,self.data_indices[row][col])
        pass

    
#===============================================================================
# Clase principal que es la que se llama cuadno se importa este modulo.
# Construye el grid como tal basandose en los datos de la tabla anterior permite
# almacenar datos en clipboard mediate ctrl+C para pegarlos en otra aplicacion.
#===============================================================================
class HugeTableGrid(gridlib.Grid):
    def __init__(self, parent, log, colLabels, rowLabels, data_indices):
        gridlib.Grid.__init__(self, parent, -1, size = (945,550))

        #===============================================================================
        #    Construye tabla base para el grid 
        #===============================================================================
        table = HugeTable(log, colLabels, rowLabels, data_indices)
        self.loglog = log
        self.SetTable(table, True)

        #===============================================================================
        #    Establecer formato de letra, background, fija tamaño algo mayor para
        #    la columna con nombres de casos. Inicializa varible para exportar datos
        #===============================================================================
        self.SetLabelFont(wx.Font(10,wx.ROMAN,wx.NORMAL,wx.BOLD))
        self.SetLabelBackgroundColour(wx.Colour(160,160,255, 250))
        self.SetRowLabelSize(self.GetRowLabelSize()+10)
        self.data_export = []

        #===============================================================================
        #    Eventos que redireccionan a los metodos ctrl+C, select cell or range
        #===============================================================================
        self.Bind(wx.EVT_KEY_DOWN, self.Key)
        self.Bind(gridlib.EVT_GRID_SELECT_CELL, self.OnSelectCell)
        self.Bind(gridlib.EVT_GRID_RANGE_SELECT, self.OnRangeSelect)

    #===============================================================================
    #    Metodo para guardar el contenido de la celda seleccionada en self.data_export
    #===============================================================================
    def OnSelectCell(self, evt):
        if evt.Selecting():
            self.data_export = []
            label_columnas = [self.GetColLabelValue(evt.GetCol())]
            label_columnas = ['\t']+label_columnas
            self.data_export.append(''.join(label_columnas)+'\n')
            fila = [str('%9.5f' % float(self.GetCellValue(evt.GetRow(),evt.GetCol())))]
            fila = [self.GetRowLabelValue(evt.GetRow())+'\t']+fila
            #print ''.join(fila)+'\n'
            self.data_export.append(''.join(fila)+'\n')
            #msg = 'Selected'
            #self.loglog.write("OnSelectCell: %s (%d,%d) %s\n" %
            #           (msg, evt.GetRow(), evt.GetCol(), evt.GetPosition()))
        else:
            pass
        
        evt.Skip()

    #===============================================================================
    #    Metodo para guardar el contenido del rango seleccionado en self.data_export
    #===============================================================================
    def OnRangeSelect(self, evt):
        if evt.Selecting():
            self.data_export = []
            if evt.GetTopLeftCoords()[0] == evt.GetBottomRightCoords()[0] and evt.GetTopLeftCoords()[1] != evt.GetBottomRightCoords()[1]: #el rango es una fila
                label_columnas = [self.GetColLabelValue(col)+'\t' for col in range(evt.GetTopLeftCoords()[1],evt.GetBottomRightCoords()[1]+1) ]
                label_columnas = ['\t']+label_columnas
                self.data_export.append(''.join(label_columnas)+'\n')
                fila = [ str('%9.5f' % float(self.GetCellValue(evt.GetTopLeftCoords()[0],col)))+'\t' for col in range(evt.GetTopLeftCoords()[1],evt.GetBottomRightCoords()[1]+1)]
                fila = [self.GetRowLabelValue(evt.GetTopLeftCoords()[0])+'\t']+fila
                #print ''.join(fila)+'\n'
                self.data_export.append(''.join(fila)+'\n')

            elif evt.GetTopLeftCoords()[0] != evt.GetBottomRightCoords()[0] and evt.GetTopLeftCoords()[1] == evt.GetBottomRightCoords()[1]: #el rango es una colmna
                label_columnas = [self.GetColLabelValue(evt.GetTopLeftCoords()[1])]
                label_columnas = ['\t']+label_columnas
                self.data_export.append(''.join(label_columnas)+'\n')
                for row in range(evt.GetTopLeftCoords()[0], evt.GetBottomRightCoords()[0]+1):
                    fila = [str('%9.5f' % float(self.GetCellValue(row,evt.GetTopLeftCoords()[1])))]
                    fila = [self.GetRowLabelValue(row)+'\t']+fila
                    #print ''.join(fila)+'\n'
                    self.data_export.append(''.join(fila)+'\n')

            elif evt.GetTopLeftCoords()[0] != evt.GetBottomRightCoords()[0] and evt.GetTopLeftCoords()[1] != evt.GetBottomRightCoords()[1]: #el rango varias filas y varias col
                label_columnas = [self.GetColLabelValue(col)+'\t' for col in range(evt.GetTopLeftCoords()[1],evt.GetBottomRightCoords()[1]+1) ]
                label_columnas = ['\t']+label_columnas
                self.data_export.append(''.join(label_columnas)+'\n')
                for row in range(evt.GetTopLeftCoords()[0], evt.GetBottomRightCoords()[0]+1):
                    fila = [ str('%9.5f' % float(self.GetCellValue(row,col)))+'\t' for col in range(evt.GetTopLeftCoords()[1],evt.GetBottomRightCoords()[1]+1)]
                    fila = [self.GetRowLabelValue(row)+'\t']+fila
                    #print ''.join(fila)+'\n'
                    self.data_export.append(''.join(fila)+'\n')

            else:
                pass
        else:
            pass
        
        evt.Skip()

    #===============================================================================
    #    Metodo para poner en el clipboard la informacion seleccionada y almacenada 
    #    en self.data_export cuando se presiona ctrl+C
    #===============================================================================
    def Key(self, event):
        if event.ControlDown() and event.GetKeyCode() == 67:
            if self.data_export:
                data = wx.TextDataObject()
                data.SetText(''.join(self.data_export))
                wx.TheClipboard.Open()
                wx.TheClipboard.SetData(data)
                wx.TheClipboard.Close()


#===============================================================================
# #===============================================================================
# # Clase que permite correr este modulo en modo independiente
# #===============================================================================
# class Frame(wx.Frame):
#    def __init__(self, parent, log):
#        wx.Frame.__init__(self, parent, -1, 'Connectivity indices based in Ulam Gnomons' , size=(640,480))
#        grid = HugeTableGrid(self, log)
#        grid.SetReadOnly(5,5, True)
# 
# #---------------------------------------------------------------------------
# if __name__ == '__main__':
#    import sys
#    app = wx.PySimpleApp()
#    frame = Frame(None, sys.stdout)
#    frame.Show(True)
#    app.MainLoop()
#===============================================================================