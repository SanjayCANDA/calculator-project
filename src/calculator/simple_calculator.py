"""
    Docstring pour calculator.simple_calculator
Auteur : Sanjay CANDA
Date : 12/02/2026
Objectif : Fiche contenant des fonctions de calcule treès simple
"""

import numpy

# Somme
def fsum(a,b):
    if not (isinstance(a, int) and isinstance(b, int)):
        print("entrer des entiers")
        fsum(a,b)
    else :
        print("Le résultat est : ", a+b)


# Soustraction
def substract(a,b):
    if not (isinstance(a, int) and isinstance(b, int)):
        print("entrer des entiers")
        substract(a,b)
    else :
        print("Le résultat est : ", a-b)

# Multiplication
def multiply(a,b):
    if not (isinstance(a, int) and isinstance(b, int)):
        print("entrer des entiers")
        multiply(a,b)
    else :
        print("Le résultat est : ", a*b)

# Division
def divide(a,b):
    if a == 0 :
        print("Le résultat est : 0.0")
    if b ==0 :
        print("ZeroDivisionError")
    elif not (isinstance(a, int) and isinstance(b, int)):
        print("entrer des entiers")
        divide(a,b)
    else :
        print("Le résultat est : ", a/b)