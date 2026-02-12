"""
    Docstring pour calculator.simple_calculator
Auteur : Sanjay CANDA
Date : 12/02/2026
Objectif : Classe contenant des fonctions de calcule treès simple
"""


class Calculator:
    """
    Classe Calculatrice permettant d'effectuer des opérations arithmétiques
    simples (addition, soustraction, multiplication, division) entre deux entiers.

    Chaque méthode vérifie que les paramètres fournis sont des entiers avant
    d'effectuer le calcul.
    """

    def _verifier_entiers(self, a, b):
        """
        Vérifie que les deux paramètres sont des entiers.
        a: premier nombre à vérifier - type a: int
        b: deuxième nombre à vérifier - type b: int
        return: True si a et b sont des entiers, False sinon - rtype: bool
        """
        return isinstance(a, int) and isinstance(b, int)

    # Somme
    def fsum(self, a, b):
        """
        Calcule la somme de deux entiers.
        Entrée : deux entiers
        Sortie : un entier
        """
        if not self._verifier_entiers(a, b):
            print("Entrer des entiers")
        else:
            print("Le résultat est :", a + b)

    # Soustraction
    def substract(self, a, b):
        """
        Calcule la soustraction de deux entiers.
        Entrée : deux entiers
        Sortie : un entier
        """
        if not self._verifier_entiers(a, b):
            print("Entrer des entiers")
        else:
            print("Le résultat est :", a - b)

    # Multiplication
    def multiply(self, a, b):
        """
        Calcule la multiplication de deux entiers.
        Entrée : deux entiers
        Sortie : un entier
        """
        if not self._verifier_entiers(a, b):
            print("Entrer des entiers")
        else:
            print("Le résultat est :", a * b)

    # Division
    def divide(self, a, b):
        """
        Calcule la division de deux entiers.
        Entrée : deux entiers
        Sortie : un float
        """
        if not self._verifier_entiers(a, b):
            print("Entrer des entiers")
        elif b == 0:
            print("ZeroDivisionError")
        else:
            print("Le résultat est :", a / b)



#mini test
calc = Calculator()

calc.fsum(5, 5)
calc.substract(5, 5)
calc.multiply(5, 5)
calc.divide(5, 5)