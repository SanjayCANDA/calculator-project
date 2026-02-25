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

## Fonctionnalité du projet 

## 1. Description du Code
Le module `simple_calculator.py` fournit une classe `Calculator` conçue pour effectuer des opérations arithmétiques de base. Sa particularité réside dans son approche **défensive** : elle valide strictement les types de données avant toute opération pour garantir l'intégrité des calculs.

## 2. Analyse des Fonctionnalités

| Méthode | Action | Entrée (Types) | Sortie (Types) |
| :--- | :--- | :--- | :--- |
| `_verifier_entiers` | Vérification entier | `(any, any)` | `bool` |
| `fsum` | Addition | `(int, int)` | `int` |
| `substract` | Soustraction | `(int, int)` | `int` |
| `multiply` | Multiplication | `(int, int)` | `int` |
| `divide` | Division | `(int, int)` | `float` |



## 3. Exemples d'Utilisation par Méthode

Voici comment instancier la classe et utiliser ses méthodes :

```python
from calculator.simple_calculator import Calculator

calc = Calculator()

# --- SOMME ---
# Additionne deux entiers
res_sum = calc.fsum(10, 5)  # Résultat : 15

# --- SOUSTRACTION ---
# Soustrait le deuxième nombre du premier
res_sub = calc.substract(10, 5)  # Résultat : 5

# --- MULTIPLICATION ---
# Multiplie deux entiers
res_mult = calc.multiply(10, 5)  # Résultat : 50

# --- DIVISION ---
# Divise le premier par le second (renvoie un float)
res_div = calc.divide(10, 4)  # Résultat : 2.5
```
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


====================================================================



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
<pre>
python3
>>> from calculator.simple_calculator import Calculator
>>> calc = Calculator()
>>> calc.fsum(5, 5)
10
</pre>

=========================================================================



##  Architecture CI/CD (GitHub Actions)

Le fichier `.github/workflows/main.yml` orchestre automatiquement les étapes suivantes à chaque `push` sur la branche `main` sur GitHub :

1. **Linting & Formatting** : Vérification du style avec `Black` et `Flake8`.
2. **Unit Tests** : Exécution des tests via `Pytest` sur plusieurs versions de Python (3.10, 3.12).
3. **Metrics** : Analyse de la complexité cyclomatique avec `Radon`.
4. **Build** : Création des archives de distribution (`.tar.gz` et `.whl`).
5. **Continuous Deployment** : Publication automatique sur **TestPyPI**.

De même pour le fichier `.gitlab-ci.yml` qui permet d'automatiser les tests et vérification à charque `push` sur GitLab

## TestPyPI

1. Le problème : Le risque de vol d'identité

Pour publier ta calculatrice sur TestPyPI, tu as besoin d'une autorisation.
Si tu écris ton mot de passe ou ton Token en clair dans ton fichier main.yml, n'importe qui consultant ton projet sur GitHub peut le voler.

Une fois volé, quelqu'un pourrait publier du code malveillant à ta place sous le nom de ton projet.


2. La solution : Le Repository Secret

Un Secret est une variable d'environnement chiffrée.

Tu le déposes sur GitHub : Dans les paramètres de ton dépôt (Settings > Secrets and variables > Actions).

GitHub le masque : Une fois enregistré, plus personne ne peut le lire (même pas toi). Il apparaît sous forme d'astérisques *** dans les journaux (logs) du pipeline.

Le Workflow l'utilise : Ton fichier main.yml appelle le secret via la syntaxe ${{ secrets.TESTPYPI_TOKEN }} au moment précis du déploiement.


3. Le mécanisme avec TestPyPI (Le Token API)

Au lieu d'utiliser ton mot de passe personnel TestPyPI, on utilise un Token API. C'est une longue chaîne de caractères qui ressemble à pypi-AgENdGVzdC5weXBpLm9yZw....

Portée limitée : Tu peux créer un token qui n'a le droit de publier que sur un seul projet spécifique.

Révocation facile : Si tu penses que le token est compromis, tu peux le supprimer sur TestPyPI sans avoir à changer ton mot de passe principal.


4. Le flux de travail sécurisé

Voici ce qui se passe quand ton job deploy-testpypi se lance :

Récupération : GitHub Actions "déverrouille" le secret TESTPYPI_TOKEN et l'injecte dans une variable temporaire (TWINE_PASSWORD).

Authentification : L'outil Twine envoie le paquet à TestPyPI en utilisant ce token comme preuve d'identité.

Nettoyage : Dès que le job est fini, la variable est effacée de la mémoire du serveur GitHub.

#### En résumé
Les Repository Secrets permettent de séparer le code (qui est public ou partagé) de l'autorisation (qui reste privée). C'est le pilier de la sécurité en DevOps.