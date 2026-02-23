"""

Auteur : Sanjay CANDA
Date : 12/02/2026
Objectif : Fichier test pour calculator, permet de vérifier le bon fonctionnement de calculator
"""

import pytest
from calculator.simple_calculator import Calculator


@pytest.fixture
def calc():
    """Prépare une instance de Calculator pour chaque test."""
    return Calculator()


# =================================================================
# 1. LA PRÉCISION ARITHMÉTIQUE (HAPPY PATH)
# =================================================================
def test_precision_arithmetique(calc):
    assert calc.fsum(5, 5) == 10
    assert calc.substract(10, 5) == 5
    assert calc.multiply(5, 5) == 25
    assert calc.divide(10, 2) == 5.0


# =================================================================
# 2. LE CONTRÔLE DES TYPES (SÉCURITÉ)
# =================================================================


def test_rejet_strings(calc):
    """Vérifie que les chaînes de caractères lèvent une TypeError."""
    with pytest.raises(TypeError):
        calc.fsum(5, "a")
    with pytest.raises(TypeError):
        calc.substract(5, "b")
    with pytest.raises(TypeError):
        calc.multiply(5, "c")
    with pytest.raises(TypeError):
        calc.divide(5, "d")


def test_restriction_entiers(calc):
    """Vérifie que les nombres à virgule (float) sont refusés."""
    with pytest.raises(TypeError):
        calc.fsum(5, 1.1)
    with pytest.raises(TypeError):
        calc.substract(5, 1.5)
    with pytest.raises(TypeError):
        calc.multiply(5, 2.2)
    with pytest.raises(TypeError):
        calc.divide(5, 3.3)


# =================================================================
# 3. LA GESTION DES CAS CRITIQUES (DIVISION)
# =================================================================


def test_division_zero_numerateur(calc):
    """Vérifie que 0 divisé par un nombre fonctionne et renvoie 0."""
    assert calc.divide(0, 5) == 0


def test_division_par_zero_interdite(calc):
    """Vérifie que la division par zéro lève bien ZeroDivisionError."""
    with pytest.raises(ZeroDivisionError):
        calc.divide(5, 0)


"""
from calculator.simple_calculator import Calculator
calc = Calculator()

print("========= Tests somme ==========")
nb_test_som = 3
Som = 0

# Test résultat correct
try:
    if calc.fsum(5, 5) == 10:
        Som += 1
    else:
        print("Problème de calcul")
except Exception as e:
    print("Erreur inattendue :", e)

# Test entrée string
try:
    calc.fsum(5, "a")
except TypeError:
    Som += 1
else:
    print("Problème : donnée d'entrée est un string")

# Test entrée float
try:
    calc.fsum(5, 1.1)
except TypeError:
    Som += 1
else:
    print("Problème : donnée d'entrée est un float")


print("\n======== Tests soustraction =========")
nb_test_sous = 3
Sous = 0

try:
    if calc.substract(5, 5) == 0:
        Sous += 1
    else:
        print("Problème de calcul")
except Exception as e:
    print("Erreur inattendue :", e)

try:
    calc.substract(5, "a")
except TypeError:
    Sous += 1

try:
    calc.substract(5, 1.1)
except TypeError:
    Sous += 1


print("\n======= Tests multiplication ==========")
nb_test_mult = 3
Mult = 0

try:
    if calc.multiply(5, 5) == 25:
        Mult += 1
    else:
        print("Problème de calcul")
except Exception as e:
    print("Erreur inattendue :", e)

try:
    calc.multiply(5, "a")
except TypeError:
    Mult += 1

try:
    calc.multiply(5, 1.1)
except TypeError:
    Mult += 1


print("\n========= Tests division ========")
nb_test_div = 5
Div = 0

# Résultat correct
try:
    if calc.divide(5, 5) == 1:
        Div += 1
    else:
        print("Problème de calcul")
except Exception as e:
    print("Erreur inattendue :", e)

# Entrée string
try:
    calc.divide(5, "a")
except TypeError:
    Div += 1

# Entrée float
try:
    calc.divide(5, 1.1)
except TypeError:
    Div += 1

# Division 0/b
try:
    if calc.divide(0, 5) == 0:
        Div += 1
except Exception as e:
    print("Erreur inattendue :", e)

# Division par zéro
try:
    calc.divide(5, 0)
except ZeroDivisionError:
    Div += 1
else:
    print("Problème : division par 0 est impossible")


# Calcul des pourcentages
print("\n========= RESULTATS TESTS ========")
print("Test Somme : ", (Som / nb_test_som) * 100, "%")
print("Test Soustraction : ", (Sous / nb_test_sous) * 100, "%")
print("Test Multiplication : ", (Mult / nb_test_mult) * 100, "%")
print("Test Division : ", (Div / nb_test_div) * 100, "%")

total_success = Som + Sous + Mult + Div
total_tests = nb_test_som + nb_test_sous + nb_test_mult + nb_test_div
print("\nRésultat global : ", (total_success / total_tests) * 100, "%")
"""
