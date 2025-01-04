# Centralisation

Le site Web Centralisation sert d’agrégateur de lien pour les Centraliens : sur cette même page sont centralisés les liens vers les sites et outils utiles dont peut avoir besoin chaque étudiant.

La motivation pour la création de cette page vient de la multitude de sites que l'école et son écosystème possèdent qui induit une difficulté à s'y retrouver. In fine, de nombreux étudiants n'ont pas connaissances de certains services. Aux sites institutionnels, s'ajoutent les sites et services des associations. Centralisation tente de remettre un peu d'ordre !

Il est recommandé d'ajouter Centralisation à ses favoris ou de configurer son navigateur pour en faire sa page d'accueil.

## Le projet

La page principale est générée automatiquement par un script `Python` (3.9) et utilise la librairie `Jinja2` pour automatiser l'écriture du `html`. Une documentation complète de la librairie est disponible sur le site officiel. Cependant, notre projet emploie uniquement les fonctionnalités de base.

Le choix d'une génération automatique s'explique par la redondance du code HTML de la page et dans l'ambition de faire un projet clair, facilement compréhensible et modifiable.

Pour faire bref :

- Les différents liens, leurs noms et descriptions sont écrits au format `YAML` dans le fichier [links.yaml](./links.yaml).
- Le script Python `build.py` lit le fichier YAML et construit la page HTML à partir de celui-ci.
- Le fichier final est enregistré dans le dossier `./dist` aux côtés des feuilles de styles CSS et des images.

Afin de faciliter la gestion l'adaptabilité de la page en fonction des thèmes et des différentes résolutions d'écrans, la feuille de style de la page est générée avec `tailwind`. 

Les logos non associés à des associations, logiciels ou à l'école sont issus du site [Font Awesome](https://fontawesome.com/search).

## Environnement de compilation

Pour mettre à jours le site, clonez le projet sur votre PC.

```bash
git clone https://github.com/aeecleclair/Centralisation.git
```

Déplacez-vous dans le dossier du projet

```bash
cd ./centralisation
```

Modifiez le fichier `links.yaml` à votre guise.

Pour construire la page il faut exécuter le script Python. Assurez-vous d'avoir `Python3.9` où supérieur installé avec la librairie `Jinja2` et `PyYAML`. L'utilisation d'un environnement virtuel avec [Poetry](https://python-poetry.org/) permet d'installer ces éléments.

Pour modifier le style de la page, placez le dossier `./src` dans un nouveau projet `tailwind` et modifier les différents éléments avant de [générer une nouvelle feuille de style](https://tailwindcss.com/docs/installation) pour remplacer la précédente.

## Compilation

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

Pour faciliter le déploiement, une image docker est fournie. Pour créer l'image : `docker build -t centralisation .` et créer le conteneur `docker run -it -d -p 80:80 centralisation`.

Un fichier `docker-compose.yml` peut être édité :

```yml
version: "3"
services:
  web:
    image: centralisation
    container_name: centralisation
    restart: unless-stopped
    ports:
      - "80:80"
```
