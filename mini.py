# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 13:38:34 2021

@author: manager
"""

import fonctions as f

#MINI CALCULETTE PYTHON
print("MINI CALCULETTE\n\n")

print("1- Addition\n")
print("2- Soustraction\n")
print("3- Multiplication\n")
print("4- Division\n\n")

entree = input("Veuillez selectionner l'operation que vous souhaitez executer : ")
choix = int(entree)

entree = input("\nVeuillez saisir le premier nombre : ")
nb1 = int(entree)

entree = input("\nVeuillez saisir le deuxieme nombre : ")
nb2 = int(entree)

if (choix == 1):
    print(nb1, " + ", nb2, " = ", f.addition(nb1, nb2))

elif(choix == 2):
    print(nb1, " - ", nb2, " = ", f.soustraction(nb1, nb2))

elif(choix == 3):
    print(nb1, " * ", nb2, " = ", f.multiplication(nb1, nb2))

elif(choix == 4):
    if(nb2 != 0):
        print(nb1, " / ", nb2, " = ", f.division(nb1, nb2))
    else:
         f.division(nb1, nb2)

f.pause()

