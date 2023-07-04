<img src="./logo.png" alt="Classifier AI Logo" height="200" width="200" />

# classifier-ai

Email classification program powered by machine learning.

Report linked to this project: [TER - Rapport Final - Maxime Princelle.pdf](https://github.com/ThePrincelle/classifier-ai/files/11948670/TER.-.Rapport.Final.-.Maxime.Princelle.pdf).


By [Maxime Princelle](https://contact.princelle.org).

<br/>

**Table des matères :**

[[_TOC_]]

## Installation

Un fichier [requirements.txt](./requirements.txt) est mis à disposition et contient toutes les librairies nécessaires au bon fonctionnement du programme.

Le programme fonctionne avec Python 3.


## Utilisation

### Ligne de commande

Exécutez le programme principal: 

```bash
python3 main.py
```

et suivez les instrucutions.

#### Utilisation du .env

Pour utiliser le fichier d'environnement, copiez le fichier [.env.example](./.env.example) en `.env` et remplissez ce dernier avec vos informations de connexion.

Quand un fichier `.env` est présent à la racine du projet avec les bonnes valeurs, aucune intervention n'est requise sur l'interface en ligne de commande.

#### Export/Import

Lors des tests, le téléchargement des données peut être long, pour remédier à cela, il est possible d'exporter/importer les données.

Pour exporter les données, rajoutez l'option `-e` à l'appel du programme principal : 

```bash
python3 main.py -e
```

Après téléchargement, vous obtiendrez un fichier `.pickle` (format pour DataFrame Pandas) avec le nom suivant : `export_{email_address}.pickle`.

Pour réutiliser cet export et éviter le téléchargement des données, utilisez l'option `-i` : 

```bash
python3 main.py -i
```

cette option va utiliser l'adresse mail indiquée dans le fichier `.env` ou donnée dans les instructions au démarrage du programme. 

PS: Bien que les données soient déjà présentes, toutes les informations de connexion doivent être présentes au lancement du programme.

### Implémentation dans un autre programme

Importez la fonction `main` de [main.py](./main.py`. 

```python
from classifier-ai.main import main as classfier

login_info = {
    'email': "mail-classfier@master-sil.fr"
    'password': "VerySecurePassword"
    'server': "partage.unistra.fr"
}

categorized_mails = classifier(login_info)
```

Vous trouverez dans "categorized_mails", un tableau pour chaque catégorie associée de la liste de mail avec les attributs suivants (UID (fournie par la librairie IMAP), TO, FROM, Date, Sujet, Texte brut du mail).




