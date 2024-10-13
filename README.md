# HoriBOT - Assistant IA Interactif

HoriBOT est un assistant IA interactif en ligne de commande, conçu pour répondre à une variété de questions en utilisant une combinaison de connaissances locales et l'API AI21 Labs. Ce projet démontre l'intégration d'une IA avancée dans une application Python simple et extensible.

## Fonctionnalités

- **Base de connaissances locale** : Stocke et récupère des informations personnalisées.
- **Intégration AI21 Labs** : Utilise l'API AI21 Labs pour répondre aux questions hors de la base de connaissances locale.
- **Apprentissage interactif** : Permet d'ajouter de nouvelles connaissances pendant l'exécution.
- **Configuration flexible** : Utilise un fichier de configuration séparé pour une gestion facile des paramètres.
- **Sauvegarde des connaissances** : Enregistre la base de connaissances locale dans un fichier JSON.

## Structure du projet

- `ia.py` : Script principal contenant la logique de l'assistant IA.
- `config.py` : Fichier de configuration contenant les paramètres de l'API et autres variables globales.
- `connaissances_avancees.json` : Fichier de sauvegarde pour la base de connaissances locale.

## Prérequis

- Python 3.6+
- Bibliothèque `requests`

## Installation

1. Clonez ce dépôt :
   ```
   git clone https://github.com/votre-nom-utilisateur/Horibot.git
   cd Horibot
   ```

2. Installez les dépendances :
   ```
   pip install requests
   ```

3. Configurez votre clé API AI21 Labs dans `config.py`.

## Utilisation

1. Lancez l'assistant :
   ```
   python ia.py
   ```

2. Interagissez avec HoriBOT :
   - Posez des questions directement.
   - Utilisez la commande 'apprendre' pour ajouter de nouvelles connaissances.
   - Utilisez la commande 'quitter' pour terminer la session.

## Personnalisation

- Modifiez `config.py` pour ajuster les paramètres de l'API et autres configurations globales.
- Étendez la classe `IAAvancee` dans `ia.py` pour ajouter de nouvelles fonctionnalités.

## Contribution

Les contributions sont les bienvenues ! N'hésitez pas à ouvrir une issue ou à soumettre une pull request.

## Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.

## Avertissement

Ce projet utilise l'API AI21 Labs, qui peut engendrer des coûts. Assurez-vous de comprendre la tarification de l'API avant une utilisation intensive.
