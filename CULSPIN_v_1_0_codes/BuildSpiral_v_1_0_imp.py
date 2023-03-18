#!/usr/bin/env python
# -*- coding: cp1252 -*- 
# main window

'''
Created on 06/05/2009

@author: Chachy
'''

#===============================================================================
# Descriptions:
# Functions that allows the representation of one or more sequences
# in the Ulam Spiral ordenation, determinate the conectivities among
# sequence elements in this representation.
#===============================================================================

import math

#===============================================================================
# Definicion de funciones
#===============================================================================
#===============================================================================
# Funcion que establece por donde se comienza a rellenar la matriz al crear la espiral.
#===============================================================================
def collin_inicial( ntope, col, lin, colini, linini ):
    if ntope % 2 == 0:  # Si el numero maximo en la matriz es par
        col = int( ntope / 2 )
        lin = int( ntope / 2 )
        colini = int( ntope / 2 )
        linini = int( ntope / 2 ) + 1
    else: # Si el numero maximo en la matriz es impar
        col = int( ntope / 2 ) + 1
        lin = int( ntope / 2 ) 
        colini = int( ntope / 2 ) + 1
        linini = int( ntope / 2 ) + 1
    return col - 1, lin - 1, colini - 1, linini - 1

#===============================================================================
# Funcion que cambia las coordenadas columna,linea segun el valor de v.
#===============================================================================
def collin_segun_v( v, col, lin ):
    if v == 0: col += 1
    if v == 1: lin -= 1
    if v == 2: col -= 1
    if v == 3: lin += 1
    return col, lin

#===============================================================================
# Funcion que varia el valor de v con el cual se maneja la direccion de la espiral
#===============================================================================
def incrementa_v( p, primero, n, v ):
    if ( p == primero + n * n + 1 ) or ( p == primero + n * n + n + 1 ):
        v += 1
        if v == 4: v = 0
    return v

#===============================================================================
# Funcion base donde se construye la espiral, se evalua conectividad y se prepara CT
#===============================================================================
def convtospiral ( self):
    
    items = []
    names = []
    sequences = []
    clases = []
    
    items [:] = self.lista_items_selected
    names [:] = self.lista_names_selected
    sequences [:] = self.lista_sequences_selected
    clases [:] = self.lista_clases_selected
        
    ct_linea1 = []
    ct_linea2 = []
    ct_bloque_coord_atom = []
    ct_bloque_conectivity = []
    ulam_casos = []
    clases_casos = []
    gnomones_casos = []
    grados_casos = []
    enlaces_casos = []
    grG_casos = []

    for nsecu in range( len( items ) ):
        self.AvanGauge(self)
        tope = 0
        ntope = 0
        #-----------------------------------------------------------------------
        # Calcular tope a partir del numero de letras en la secuencia y ntope a partir de tope
        tope = len( sequences[nsecu].strip() )
        primero = 0 # Si se permita empesar por cualquier numero  entonces primero -= 1
        if math.sqrt( tope ) == int( math.sqrt( tope ) ): # si la raiz de tope es un entero
            ntope = int( math.sqrt( tope ) )
        else: # si la raiz de tope no es un entero
            ntope = int( math.sqrt( tope ) ) + 1
        #------------------------------------------------------------------------
        # Creo una matriz de listas (lista_letra)donde voy a crear la espiral
        ulam = []
        coord_letra = []
        clases = []
        grados = []
        enlaces = []
        todas_conectivity = []
        
        for i in range( ntope ):
            ulam.append( ['']*ntope )
        for i in range( ntope ):
            for j in range( ntope ):
                ulam[i][j] = ['', '']    
        for i in range( tope ):
            coord_letra.append( ['', '', 0, ''] )
            grados.append( [] )
            enlaces.append( [] )
        gnomones = []
        indices_gnomones = []
        #-------------------------------------------------------------------------
        # Construir matriz Ulam Spiral
        col, lin, colini, linini = 0, 0, 0, 0
        col, lin, colini, linini = collin_inicial( ntope, col, lin, colini, linini )
        v = 3
        conex = 0
        grG = 0
        for n in range( ntope + 1 ):
            for p in range( primero + n * n + 1, primero + ( n + 1 ) ** 2 + 1 ):
                self.AvanGauge(self)
                col, lin = collin_segun_v( v, col, lin )
                if p <= tope:
                    ulam[lin][col] = [p, sequences[nsecu][p - 1]]
                    coord_letra[p - 1][0] = col - colini
                    coord_letra[p - 1][1] = lin - linini
                    coord_letra[p - 1][3] = sequences[nsecu][p - 1]
                    if not sequences[nsecu][p-1] in clases:
                        clases.append(sequences[nsecu][p-1])
                v = incrementa_v( p, primero, n, v )
                if p < tope:
                    if p == 1:
                        grados[p-1].append(p+1)
                        grG += 1
                    else:
                        grados[p-1].append(p-1)
                        grados[p-1].append(p+1)
                        grG += 2
                    enlaces[p - 1].append( p + 1 )
                    conex += 1
                if p == tope:
                    grados[p-1].append(p-1)
                    grG += 1
                    enlaces[p - 1].append( '' )
        #===============================================================================
        #    Analizar conectividades
        #===============================================================================
        col, lin, colini, linini = 0, 0, 0, 0
        col, lin, colini, linini = collin_inicial( ntope, col, lin, colini, linini )
        v = 3
        for n in range( ntope + 1 ):
            for p in range( primero + n * n + 1, primero + ( n + 1 ) ** 2 + 1 ):
                self.AvanGauge(self)
                col, lin = collin_segun_v( v, col, lin )
                if p <= tope:
                    if ( lin - 1 ) >= 0 and ulam[lin - 1][col] != ['', '']:
                        if coord_letra[p - 1][3] == ulam[lin - 1][col][1]:
                            if not ulam[lin - 1][col][0] in grados[p - 1]:
                                grados[p - 1].append( ulam[lin - 1][col][0] )
                                grG += 1
                            if not ulam[lin - 1][col][0] in enlaces[p - 1] and not p in enlaces[ulam[lin - 1][col][0] - 1]:
                                enlaces[p - 1].append( ulam[lin - 1][col][0] )
                                conex += 1
                    if ( lin + 1 ) < ntope and ulam[lin + 1][col] != ['', '']:
                        if coord_letra[p - 1][3] == ulam[lin + 1][col][1]:
                            if not ulam[lin + 1][col][0] in grados[p - 1]:
                                grados[p - 1].append( ulam[lin + 1][col][0] )
                                grG += 1
                            if not ulam[lin + 1][col][0] in enlaces[p - 1] and not p in enlaces[ulam[lin + 1][col][0] - 1]:
                                enlaces[p - 1].append( ulam[lin + 1][col][0] )
                                conex += 1
                    if ( col - 1 ) >= 0 and ulam[lin ][col - 1] != ['', '']:
                        if coord_letra[p - 1][3] == ulam[lin ][col - 1][1]:
                            if not ulam[lin][col- 1][0] in grados[p - 1]:
                                grados[p - 1].append( ulam[lin][col- 1][0] )
                                grG += 1
                            if not ulam[lin][col - 1][0] in enlaces[p - 1] and not p in enlaces[ulam[lin][col - 1][0] - 1]:
                                enlaces[p - 1].append( ulam[lin][col - 1][0] )
                                conex += 1
                    if ( col + 1 ) < ntope and ulam[lin ][col + 1] != ['', '']:
                        if coord_letra[p - 1][3] == ulam[lin ][col + 1][1]:
                            if not ulam[lin ][col+1][0] in grados[p - 1]:
                                grados[p - 1].append( ulam[lin ][col+1][0] )
                                grG += 1
                            if not ulam[lin][col + 1][0] in enlaces[p - 1] and not p in enlaces[ulam[lin][col + 1][0] - 1]:
                                enlaces[p - 1].append( ulam[lin][col + 1][0] )
                                conex += 1
                v = incrementa_v( p, primero, n, v )

        #===============================================================================
        # Variables para cada caso: ulam, clases, grados, enlaces
        #===============================================================================
        ulam_casos.append( ulam )

        clases_casos.append(clases)

        grados_casos.append( grados )
        grG_casos.append(grG)

        enlaces_casos.append( enlaces ) 

        for n in range(ntope):
            self.AvanGauge(self)
            gnomones.append( [n + 1, 2 * n + 2,
                             [sequences[nsecu][i - 1] for i in range( n ** 2 + n + 1, n ** 2 + 3 * n + 3 ) if i <= tope],
                             [len( grados[i - 1] ) for i in range( n ** 2 + n + 1, n ** 2 + 3 * n + 3 )if i <= tope]] )
            
        gnomones_casos.append( gnomones )

        #===============================================================================
        # Variables para los ficheros CT de casos
        #===============================================================================
        ct_linea1.append(names[nsecu])

        ct_linea2.append( [tope, conex] )

        ct_bloque_coord_atom.append([[coord_letra[i][0], coord_letra[i][1], coord_letra[i][2], coord_letra[i][3]] for i in range(tope)])

        todas_conectivity = [[i + 1, enlaces[i][0], 1, 1] for i in range(tope) if enlaces[i][0]]

        for i in range( tope ):
            self.AvanGauge(self)
            if len( enlaces[i] ) > 1:
                for j in range( 1, len( enlaces[i] ) ):
                    todas_conectivity.append([i + 1, enlaces[i][j], 1, 1] )

        ct_bloque_conectivity.append(todas_conectivity)

    return ct_linea1, ct_linea2, ct_bloque_coord_atom, ct_bloque_conectivity, ulam_casos, gnomones_casos, grG_casos

#===============================================================================
# 
# #===============================================================================
# # Clase principal que se llama cuando se importa este modulo
# #===============================================================================
# #===============================================================================
# class myconv:
#    def __init__(self, lista_items_selected, lista_names_selected, lista_sequences_selected, lista_clases_selected):
# #===============================================================================
# #        Variables necesarias para llamar la funcion principal
# #===============================================================================
#        self.lista_items_selected = lista_items_selected
#        self.lista_names_selected = lista_names_selected
#        self.lista_sequences_selected = lista_sequences_selected
#        self.lista_clases_selected = lista_clases_selected
# 
#    def AvanGauge(self,event): # Alternativa para cuando se corre este módulo independiente
#        pass
#        return
# 
# #===============================================================================
# # Necesario para que el modulo pueda funcionar de modo independiente
# #===============================================================================
# if __name__ == '__main__':
#    lista_items_selected = [0, 1]
#    lista_names_selected = ['Cha[01]', 'Cha[02]']
#    lista_sequences_selected = ['GDKGGDGAG',
#                                'DDGGDGGGGGGGGDGGGDGDDGGGDGGGDGDGGDGDDDDGGGGGDGGDDGGGGGGGGGGGGGGGGKKKKKAAAKKAKKKKKKAAAKKKKAKKKKKAAKKKKKKKKKAAKKAAAAAK']
#    lista_clases_selected = [['G', 'D', 'K', 'A'],['G', 'D', 'K', 'A']]
#    
# #===============================================================================
# #    lista_sequences_selected = ['GDDGGDGGGGGGGGDGGGDGDDGGGDGGGDGDGGDGDDDDGGGGGDGGDDGGGGGGGGGGGGGGGGKKKKKAAAKKAKKKKKKAAAKKKKAKKKKKAAKKKKKKKKKAAKKAAAAAK',
# #                                     'GDGGDGGGGGGGGDGGGDGDDGGGDGGGDGDGGDGDDDDGGGGGDGGDDGGGGGGGGGGGGGGGGKKKKKAAAKKAKKKKKKAAAKKKKAKKKKKAAKKKKKKKKKAAKKAAAAAK']
# #    lista_clases_selected = [['G', 'D', 'K', 'A'],['G', 'D', 'K', 'A']]
# #===============================================================================
#    #lista_items_selected = [0]
#    #lista_names_selected = ['Cha[02]']
#    #lista_sequences_selected=['ABCDEFGHI']
#    #lista_clases_selected = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
#    
#    #lista_items_selected = [0]
#    #lista_names_selected = ['Cha[02]']
#    #lista_sequences_selected = ['GDGGDGGGGGGGGDGGGDGDDGGGDGGGDGDGGDGDDDDGGGGGDGGDDGGGGGGGGGGGGGGGGKKKKKAAAKKAKKKKKKAAAKKKKAKKKKKAAKKKKKKKKKAAKKAAAAAK']
#    #lista_clases_selected = ['G', 'D', 'K', 'A']
# #===============================================================================
#    test = myconv(lista_items_selected, lista_names_selected, lista_sequences_selected, lista_clases_selected)
#    #------------------------------------------------------------------------------ 
#    # LLamada a la funcion principal y almacenamientos de las variables de retorno de la funcion
#    ct_linea1, ct_linea2, ct_bloque_coord_atom, ct_bloque_conectivity, lista_ulam_casos, lista_gnomones_casos, grG = convtospiral( test )  
# 
# 
# #===============================================================================
# #     Comprobacion. Imprime las CT de cada espiral, uno detras del otro cuando se llama este modulo independiente
# #===============================================================================
#    for nsecu in range( len( lista_items_selected ) ):
#        print ct_linea1[nsecu]
#        for i in range( len( lista_ulam_casos[nsecu] ) ):
#            print lista_ulam_casos[nsecu][i]
#        print
#        print ct_linea1[nsecu]
#        print ct_linea2[nsecu][0], ct_linea2[nsecu][1]
#        for i in range( len( lista_sequences_selected[nsecu] ) ):
#            print '%9.4f' % ct_bloque_coord_atom[nsecu][i][0], '%9.4f' % ct_bloque_coord_atom[nsecu][i][1], '%9.4f' % ct_bloque_coord_atom[nsecu][i][2], '%s' % ct_bloque_coord_atom[nsecu][i][3]
#        for i in range( ct_linea2[nsecu][1] ):
#            print ct_bloque_conectivity[nsecu][i][0], ct_bloque_conectivity[nsecu][i][1], ct_bloque_conectivity[nsecu][i][2], ct_bloque_conectivity[nsecu][i][3]    
#        print
# 
# #===============================================================================
# #     Comprobacion. Imprime gnomones cuando se llama este modulo independiente
# #===============================================================================
#        for gnomon in lista_gnomones_casos[nsecu]:
#            print gnomon
# 
#        print
#        print grG
#===============================================================================

