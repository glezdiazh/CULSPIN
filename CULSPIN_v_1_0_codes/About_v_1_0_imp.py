#!/usr/bin/env python
# -*- coding: cp1252 -*- 
# main window

'''
Created on 30/05/2009

@author: Chachy
'''
import wx
import wx.html
import os, sys


class MyHtmlFrame(wx.Frame):
    def __init__(self, parent, title,raiz_images= os.getcwd()+"\\"):
        wx.Frame.__init__( self, parent, -1, title, pos=(0,0), size=( 600, 640 ),
                           style = wx.CAPTION | wx.SYSTEM_MENU | wx.MINIMIZE_BOX | wx.CLOSE_BOX )
        os.chdir(raiz_images)
        panel= wx.Panel(self, -1,pos=(0,0),size=(600,640))
        panel.SetBackgroundColour(wx.Colour(160,160,255, 250))
        html = wx.html.HtmlWindow(panel,-1, pos=(0,0), size=(600,380))
        html.SetBackgroundColour(wx.Colour(160,160,255, 250))
        page = """
<html>
<head>
  <meta 
 content="text/html; charset=ISO-8859-1"
 http-equiv="content-type">
  <title>Help about Input file format</title>
</head>
<body BACKGROUND='images/MiAbout.jpg'>
</body>
</html>
"""
        html.SetPage(page)
        cpdev = cpde = wx.CollapsiblePane(panel, label='Developers', 
                                     pos=(180, 380),size = (580,40),
                                     style=wx.CP_DEFAULT_STYLE|wx.CP_NO_TLW_RESIZE)
        developers = """
- Lázaro Guillermo Pérez-Montoto, Department of Organic Chemistry, University 
  of Santiago de Compostela (USC), 15782, Santiago de   Compostela, Spain. 
  lgpm2002@yahoo.es.                   

- Francisco J. Prado-Prado, Ph.D, Department of Organic Chemistry, University 
  of Santiago de Compostela (USC), 15782 Santiago de Compostela, Spain.       

- Cristian R. Munteanu, Ph.D, Department of Information and Communications 
  Technologies, Computer Science   Faculty (UDC), University of A Coruña, A 
  Coruña, 15071, Spain.                      

- Humberto González-Díaz, Ph.D, Department of Microbiology and Parasitology, 
  Faculty of Pharmacy, University of Santiago de Compostela (USC), 15782, Spain.
  gonzalezdiazh@yahoo.es
"""
        cpdev_contenido = wx.StaticText(cpde.GetPane(), -1, developers)
        cpdev.Collapse(False)

        cplic = cpli = wx.CollapsiblePane(panel, label='License', 
                                     pos=(20, 380),size = (160,40),
                                     style=wx.CP_DEFAULT_STYLE|wx.CP_NO_TLW_RESIZE)
        licencia = """
        CULSPIN ver. 1.0 

              © 2009

Email : lgpm2002@yahoo.es
"""
        cplic_contenido = wx.StaticText(cpli.GetPane(), -1, licencia)
        cplic.Collapse(False)

#===============================================================================
# 
# app = wx.PySimpleApp()
# raiz_images = os.getcwd()+"\\"
# frm = MyHtmlFrame(None, "About CULSPIN 1.0",raiz_images= os.getcwd()+"\\")
# frm.SetIcon(wx.Icon(raiz_images + 'images/about.ico', wx.BITMAP_TYPE_ICO))
# frm.Center()
# frm.Show()
# app.MainLoop()
#===============================================================================
