![project-cabbage-logo](https://user-images.githubusercontent.com/38188604/59980445-34b0b480-95f6-11e9-8f69-51dd4373f3eb.png)

Le projet présente une maquette impliquant une plateforme communautaire de babysitting. Elle repose sur une base de données SQLite et l'intégralité du site est alimenté par une architecture serveur Django (Python).

Elle a pour but de montrer ce qu'il est possible de faire aujourd'hui avec un système en BackEnd sous Django. Aujourd'hui sur ce projet, il est possible de créer un compte, s'authentifier, changer son profil, monter un profil "babysitter", et enfin, le diffuser !

![Home](https://user-images.githubusercontent.com/38188604/59980378-58bfc600-95f5-11e9-9bbe-c9bcf8d3a234.png)
![SearchResults](https://user-images.githubusercontent.com/38188604/59980376-58bfc600-95f5-11e9-975b-220953ebd652.png)
![Profile](https://user-images.githubusercontent.com/38188604/59980379-59585c80-95f5-11e9-91ad-acfd9d8f977a.png)
![EditProfile](https://user-images.githubusercontent.com/38188604/59980377-58bfc600-95f5-11e9-977c-6ea7a59516a2.png)

### Pré-requis

`python` v.3.6.5

`django-admin` v.2.1

### Composants tiers

`django-money` v.0.14.3 - [GitHub](https://github.com/django-money/django-money)

`django-phonenumberfield` v.2.0.1 - [GitHub](https://github.com/stefanfoulis/django-phonenumber-field)

### Tester le projet

Dans le dossier racine du projet, exécuter les commandes suivantes.

Sous Windows : `python manage.py runserver`

Sous Linux, utiliser `python3`

Lancer ensuite le lien suivant : [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
