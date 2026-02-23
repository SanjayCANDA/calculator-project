# TestSimpleCalculator_2026_SC

## Description
Ce projet est un **package Python simple** appelé `calculator`, qui permet de réaliser des opérations arithmétiques basiques (addition, soustraction, multiplication, division) sur deux entiers.  
Il est conçu comme un **exemple de packaging Python**, avec un environnement virtuel (venv) et des tests automatisés.  

---

## Contenu du projet

<pre>
calculator-project/
├── pyproject.toml   # Déclaration du package et dépendances
├── README.md        # Ce fichier
├── LICENSE          # Licence Unlicense
├── src/
│ └── calculator/
│ ├── init.py # Indique que c'est un package Python
│ └── simple_calculator.py       # Code source de la calculatrice
└── tests/
└── test_simple_calculator.py    # Tests unitaires et calcul du pourcentage de réussite
</pre>

## Fichiers principaux

### Fichier calculator

- `src/calculator/simple_calculator.py`  
  Contient la classe `Calculator` avec les méthodes :  
  - `fsum(a,b)` → addition  
  - `substract(a,b)` → soustraction  
  - `multiply(a,b)` → multiplication  
  - `divide(a,b)` → division  
  Chaque méthode vérifie que les entrées sont des entiers et lève une exception (`TypeError` ou `ZeroDivisionError`) si nécessaire.  

  1. Méthode `_verifier_entiers`
C'est un filtre préalable : il renvoie True uniquement si les deux nombres sont des entiers. Il sert de fondation à toutes les autres méthodes.

  2. Méthodes `fsum`, `substract`, `multiply`
Elles suivent toutes ce schéma en 2 étapes :
Vérification : Si les entrées ne sont pas des entiers → déclenchement d'une erreur (TypeError).
Calcul : Sinon → exécution de l'opération (+, −, ou ×).

  3. Méthode `divide`
Elle possède une double protection :
Type : Doit être un entier (sinon TypeError).
Valeur : Le diviseur ne doit pas être 0 (sinon ZeroDivisionError).

### Fichier test
- `tests/test_simple_calculator.py`  
  Teste toutes les méthodes de `Calculator` et calcule un **pourcentage de réussite** pour chaque opération et global.  
  Les tests utilisent `try/except` pour capturer les erreurs attendues et valider les calculs corrects.  

Synthèse Globale des Tests :
Le script réalise un audit de fiabilité sur quatre opérations (Somme, Soustraction, Multiplication, Division) à travers trois axes principaux :

1. La Précision Arithmétique

C'est le test de base. On vérifie que pour des entrées valides et simples, le résultat est mathématiquement correct.
Exemple : Est-ce que 5×5 donne bien 25 ?

2. Le Contrôle des Types

C'est l'aspect le plus rigoureux de votre script. Vous testez la réaction de la calculatrice face à des données "interdites" :
Rejet des chaînes de caractères (Strings) : On vérifie que le programme ne plante pas si on essaie de calculer avec des lettres (ex: 5+"a").
Restriction aux Entiers (Integers) : Le script considère l'utilisation de nombres à virgule (float) comme une erreur. Il vérifie que la calculatrice bloque les calculs dès qu'un chiffre n'est pas un entier pur.

3. La Gestion des Cas Critiques 

Spécifiquement pour la division, le script teste les limites logiques :
Le Zéro numérateur : Vérifier que 0/5 est géré sans erreur.
L'Interdiction fatale : Vérifier que la division par zéro est interceptée et ne fait pas crasher l'application.

- `pyproject.toml`  
  Définit le package pour `setuptools` et liste les dépendances optionnelles pour les tests (`pytest`, etc.).  

---



## Installation et utilisation

Afin d’isoler les dépendances du projet et de transformer ce projet en un véritable package Python, un environnement virtuel (`venv`) a été mis en place.

Cette étape permet :
- d’utiliser une version propre de Python,
- d’installer les dépendances du projet sans affecter le système,
- de tester le package comme s’il était installé via `pip`.

---

### 1. Création de l’environnement virtuel

Depuis la racine du projet :
(Sur bash)
'python3 -m venv venv'

### 2. Activation de l’environnement virtuel
- macOS / Linux :
'source venv/bin/activate'

### 3. Installation du projet comme package

- Une fois le venv activé, le projet est installé en mode editable :
    'pip install -e .'
- Pour installer les dépendances de test :
    'pip install -e .[test]'

### 4. Vérification de l’installation du package

Dans un interpréteur Python :
python3
>>> from calculator.simple_calculator import Calculator
>>> calc = Calculator()
>>> calc.fsum(5, 5)
10