# Cabbage - A Communautary Babysitting Website Mock-Up

Le projet présente une maquette impliquant une plateforme communautaire de babysitting. Elle repose sur une base de données SQLite et l'intégralité du site est alimenté par une architecture serveur Django (Python).

Elle a pour but de montrer ce qu'il est possible de faire aujourd'hui avec un système en BackEnd sous Django. Aujourd'hui sur ce projet, il est possible de créer un compte, s'authentifier, changer son profil, monter un profil "babysitter", et enfin, le diffuser !

### Login et Recherche

![login_and_search](https://user-images.githubusercontent.com/38188604/61128083-52649180-a4b1-11e9-8cf8-ec3990b0a2e5.gif)

### Gestion du profil

![profile_and_babysitter](https://user-images.githubusercontent.com/38188604/61128085-542e5500-a4b1-11e9-8ecf-73f11da30c9a.gif)

### Anatomie de la structure

    • La structure serveur dispose désormais d'une base contenant à minima un système d'authentification, une gestion de profil avec possibilité de s'inscrire en tant que babysitter, et un système de navigation.
    • Les modèles d’utilisateurs sont en place.
    • Il est possible de s’authentifier.
    • Il est possible de rechercher un babysitter dans la base de données serveur.

### Pistes d'Amélioration

    • Possibilité pour l'utilisateur de publier une image de profil et une description.
    • Possibilité pour le babysitter de publier une annonce.
    • Système de Tri dans la Navigation (Nom, Tarifs, etc...).
    • Une section dédiée au staff avec une gestion de tickets support.
    • Possibilité de contacter le Babysitter directement sur le site.
    • Et bien d'autres...

### Pré-requis

`python` v.3.6.5

`django-admin` v.2.1

### Composants tiers

`django-money` v.0.14.3 - [GitHub](https://github.com/django-money/django-money)

`django-phonenumberfield` v.2.0.1 - [GitHub](https://github.com/stefanfoulis/django-phonenumber-field)

### Tester le projet

`python manage.py runserver`

Lancer ensuite le lien suivant : [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
