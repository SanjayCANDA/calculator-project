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

### Fichiers principaux

- `src/calculator/simple_calculator.py`  
  Contient la classe `Calculator` avec les méthodes :  
  - `fsum(a,b)` → addition  
  - `substract(a,b)` → soustraction  
  - `multiply(a,b)` → multiplication  
  - `divide(a,b)` → division  
  Chaque méthode vérifie que les entrées sont des entiers et lève une exception (`TypeError` ou `ZeroDivisionError`) si nécessaire.  

- `tests/test_simple_calculator.py`  
  Teste toutes les méthodes de `Calculator` et calcule un **pourcentage de réussite** pour chaque opération et global.  
  Les tests utilisent `try/except` pour capturer les erreurs attendues et valider les calculs corrects.  

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