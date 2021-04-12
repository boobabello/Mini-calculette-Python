# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 00:51:05 2021

@author: manager
"""

#Definition de mes differentes fonctions
def addition(nb1, nb2):
    return nb1+nb2

def soustraction(nb1, nb2):
    return nb1-nb2

def multiplication(nb1, nb2):
    return nb1*nb2

def division(nb1, nb2):
    if(nb2 != 0):
        return nb1/nb2
    else:
        print("Division par 0 impossible.\n")

def pause():
    return input ("Appuyez sur Entrée pour continuer ...")