#!/usr/bin/env python
# -*- coding: cp1252 -*- 
# main window


'''
Created on 06/05/2009

@author: Chachy
'''

#===============================================================================
# Descriptions:
# Functions that allows the calculation of indices based in the Ulam Spiral graph
# representation.
#===============================================================================

import math
from numpy.lib.scimath import log10


#===============================================================================
# Funcion para calcular los indices por gnomones
#===============================================================================
def IndicesGnomones (self, indices_clases_gnomones):
    gn = []
    gn_comp = []
    frec = []
    frec_comp = []
    sh_comp = []
    indices_gnomones = []
    
    for g in indices_clases_gnomones:
        self.AvanGauge(self)
        for c in g:
            self.AvanGauge(self)
            if not c[1] in gn:
                gn.append(c[1])
                frec.append(c[2])
            else:
                frec[gn.index(c[1])]+= c[2]

    for g in range(1,self.long_gnomon_mayor):
        self.AvanGauge(self)
        if not g in gn:
            gn_comp.append(g)
            frec_comp.append(0)
        else:
            gn_comp.append(g)
            frec_comp.append(frec[gn.index(g)])

    for f in frec_comp:
        self.AvanGauge(self)
        if f:
            sh_comp.append(-f*log10(f))
        else:
            sh_comp.append(0)
    
    indices_gnomones = [[g, f, sh] for g,f,sh in zip(gn_comp, frec_comp, sh_comp)]

    return indices_gnomones

#===============================================================================
# Funcion para calcular los indices clases globales
#===============================================================================
def IndicesClassGlobal (self, indices_clases_gnomones):
    cla = []
    cla_comp = []
    frec = []
    frec_comp = []
    sh_comp = []
    indices_globales = []
    for g in indices_clases_gnomones:
        self.AvanGauge(self)
        for c in g:
            self.AvanGauge(self)
            if not c[0] in cla:
                cla.append(c[0])
                frec.append(c[2])
            else:
                frec[cla.index(c[0])]+= c[2]

    for c in self.clases_total:
        self.AvanGauge(self)
        if not c in cla:
            cla_comp.append(c)
            frec_comp.append(0)
        else:
            cla_comp.append(c)
            frec_comp.append(frec[cla.index(c)])

    for f in frec_comp:
        self.AvanGauge(self)
        if f:
            sh_comp.append(-f*log10(f))
        else:
            sh_comp.append(0)
    
    indices_globales = [[c, f, sh] for c,f,sh in zip(cla_comp, frec_comp, sh_comp)]

    return indices_globales

#===============================================================================
# Funcion para calcular los indices clases gnomones. Base para calcular los otros.
#===============================================================================
def IndicesClassGnomon( self, gnom, grG ):
    clas_gnom = []
    clas_gnom_comp = []
    grados_clas_gnom= []
    grados_clas_gnom_comp = []
    indices_g = []
    g = gnom[0]
    nodos = gnom[2]
    n_grad_nodos = gnom[3]
    
    for i, c in enumerate( nodos ):
        self.AvanGauge(self)
        if c in clas_gnom:
            grados_clas_gnom[clas_gnom.index( c )] += n_grad_nodos[i]
        else:
            clas_gnom.append( c )
            grados_clas_gnom.append( n_grad_nodos[i] )
            
    for c in self.clases_total:
        self.AvanGauge(self)
        if not c in clas_gnom:
            clas_gnom_comp.append(c)
            grados_clas_gnom_comp.append(0)
        else:
            clas_gnom_comp.append(c)
            grados_clas_gnom_comp.append(grados_clas_gnom[clas_gnom.index(c)])
            
    for grad, c in zip(grados_clas_gnom_comp, clas_gnom_comp):
        self.AvanGauge(self)
        if grad:
            fcg = float(grad)/grG
            shcg = -fcg*log10(fcg)
        else:
            fcg = 0
            shcg = 0
        indices_g.append([c, g, fcg, shcg])
        
    return indices_g


#===============================================================================
# Funcion principal.Prepara el calculo de los indices. Es la que se llama cuando se importa este modulo
#===============================================================================
def myIndices (self):
    #===============================================================================
    #    Crear lista de las clases presentes en las secuencias
    #===============================================================================
    self.clases_total = []
    for clase in self.lista_clases_selected:
        self.AvanGauge(self)
        for c in clase:
            if not c in self.clases_total:
                self.clases_total.append(c)
    self.clases_total.sort()

    #===============================================================================
    #    Determiar la dimension del mayor gnomon y crear lista con las dimensiones de las spirales
    #===============================================================================
    self.lista_ntope = []
    ntop = []
    self.long_gnomon_mayor = ''
    for nsecu in range(len(self.lista_items_selected)):
        self.AvanGauge(self)
        t = len( self.lista_sequences_selected[nsecu].strip() )
        primero = 0 # Si se permita empesar por cualquier numero  entonces primero -= 1
        if math.sqrt( t ) == int( math.sqrt( t ) ): # si la raiz de tope es un entero
            nt = int( math.sqrt( t ) )
        else: # si la raiz de tope no es un entero
            nt = int( math.sqrt( t ) ) + 1
        self.lista_ntope.append(nt)
        ntop.append(nt)
    ntop.sort()
    self.long_gnomon_mayor = ntop[-1]

    #===============================================================================
    #    Calcular los indices por clases y gnomones, que sirven de base a los otros dos
    #===============================================================================
    
    self.indices_clases_gnomones_casos = []
    for nsecu in range(len(self.lista_items_selected)):
        indices_gnomones = []
        for g in range(self.long_gnomon_mayor):
            self.AvanGauge(self)
            if g in range(len(self.lista_gnomones_casos[nsecu])):
                gnom = self.lista_gnomones_casos[nsecu][g]
                indices_gnomones.append(IndicesClassGnomon(self, gnom, self.lista_grG_casos[nsecu]))
            else:
                completar = []
                for c in self.clases_total:
                    completar.append([c, g + 1, 0, 0])
                indices_gnomones.append(completar)
        self.indices_clases_gnomones_casos.append(indices_gnomones)

    #===============================================================================
    #    Calcula y almacena los valores del tipo de  indice seleccionado en la la variable self.indices_calculated 
    #===============================================================================
    self.indices_calculated = []

    if self.indices_tipo == 0: # Indices clases para gnomones son los indices base que se calcularon antes

        self.indices_calculated[:] = self.indices_clases_gnomones_casos

    elif self.indices_tipo == 1: # Indices clases globales (en todo el grafo)

        self.indices_clases_global_casos = []
        for indices_clases_gnomones in self.indices_clases_gnomones_casos:
            self.AvanGauge(self)
            self.indices_clases_global_casos.append(IndicesClassGlobal (self, indices_clases_gnomones))
        self.indices_calculated[:] = self.indices_clases_global_casos
    
    else: # Indices por gnomones

        self.indices_gnomones_casos = []
        for indices_clases_gnomones in self.indices_clases_gnomones_casos:
            self.AvanGauge(self)
            self.indices_gnomones_casos.append(IndicesGnomones (self, indices_clases_gnomones))
        self.indices_calculated[:] = self.indices_gnomones_casos

    return self.indices_calculated


