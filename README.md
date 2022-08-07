# Centralisation

Le site Web Centralisation sert d'aggrégateur de lien pour les Centraliens : sur cette même page sont centralisés les liens vers les sites et outils utiles dont peut avoir besoin chaque étudiants.

La motivation pour la création de cette page vient de la multitude de site que l'école possèdent qui induit une difficulté à s'y retrouver. In fine, de nombreux étudiants n'ont pas connaissances de certains services. Au site insitutionnels, s'ajoutent les les sites et services des associations. Centralisation tente de remettre un peu d'ordre.

Il est recommandé d'ajouter Centralisation à ses favoris ou de configurer son navigateur pour en faire sa page d'accueil.

## Le projet

La page principale est générée automatiquement par un script `Python` (3.9) et utilise la librairie `Jinja2` pour automatiser l'écriture du `html`. Une documentation complète de la librairie est disponible sur le site officiel. Cependant, notre projet emploie uniquement les fonctionnalités de base.

Le choix d'une génération automatique s'explique par la redondance du code HTML de la page et dans l'ambition de faire un projet clair, facilement compréhensible et modificable. 

Pour faire bref : 
- Les différents liens, leurs noms et descriptions sont écrits aux format `JSON` dans le fichier [links.json](./links.json).
- Le script Python `build.py` lit le fichier JSON et construit la page HTML à partir de celui-ci.
- Le fichier final est enregistrée dans le dossier `./dist` aux cotés des feuilles de styles CSS.

La conception du site à également suivi une volonté de choisir un design simple et et *responsive*. Plusieurs feuilles de styles sont associées à des tailles d'écran différents. Les couleurs de la page suit les couleurs des sites insitutionnels et deux versions existent : une mode clair et un mode sombre.

## build

Pour mettre à jours le site, clonez le projet sur votre PC.

```bash
git clone ...
```

Déplacez vous dans le dossier du projet

```bash
cd ./centralisation
```

Modifiez le fichier `links.json` à votre guise.

Pour construire la page il faut exécuter le script Python. Assurez vous d'avoir `Python3.9` installé avec la librairie `Jinja2`. L'utilisation d'un environnement virtuel avec [Poetry](https://python-poetry.org/).

Avec Poetry :

```bash
poetry run python ./build.py
```

Sinon simplement, 

```bash
python ./build.py
```

Récupérer le résultat dans le dossier `./dist`

## Docker

Pour faciliter le déploiement, une image docker est founie. Pour créer l'image :  `docker build -t centralisation .` et créer le coneneur `docker run -it -d -p 80:80 centralisation`.

Un fichier `docker-compose.yml` peut être édité :

```yml
version: '3'
services:
  web:
    image: centralisation
    build: .
    container_name: centralisation
    restart: always
    ports:
      - "8080:80"
```

## TODO :
- Ajouter les icones pour chaque liens
- Vérifier et corriger les fautes d'orthographe