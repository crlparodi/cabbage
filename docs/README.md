# Cabbage - A Communautary Babysitting Website Mock-Up

This project shows a Communautary Babysitting Platform Mock-Up. This is a Django project based on PostgreSQL database.

This one shows what we can do with Django backend system. You can create an account, login, change your profile, set up a babysitter profile, then publish it !

## Requirements

Python 3.10.15 and later must be installed on your environment.

## Web Application Preview

### Login and Search

![login_and_search](https://user-images.githubusercontent.com/38188604/61128083-52649180-a4b1-11e9-8cf8-ec3990b0a2e5.gif)

### Account Profile Management

![profile_and_babysitter](https://user-images.githubusercontent.com/38188604/61128085-542e5500-a4b1-11e9-8ecf-73f11da30c9a.gif)

## Mock-Up Structure

- Authentication system
- Account profile management
- Babysitter subscription
- Navigation system (especially Babysitter search and display)
- Base API for Account and Babysitter Management with asynchronous requests (Celery - Redis)


## TODOs - Improvements

- The user must be able to add a profile picture on its account
- The babysitter should be able to publish a announcement
- The user should be able to filter and sort the results (Name, Cost, etc...)
- Staff section with support tickets management
- The babysitter must be reachable through the site via a private chat
- Probably more...

## Run the project - Installation


### Docker Compose

Before doing any operations, you must add the `.env` file to the root of this project. You can add it by copying the `.env.dist` file and rename it `.env`.

```
cd ./cabbage
cp .env.dist .env

# Edit the .env file
nano .env
```

Docker Compose file (`docker-compose.yml`) is already written. You just have to check you have the right version of cabbage in it, then launch the containers by typing the following:

```
docker compose up -d
```

Open this link : [http://127.0.0.1:8080/](http://127.0.0.1:8080/)

### Kubernetes

Get to k8s deployment folder ...

```
cd ./cabbage/k8s
```

... then copy the `env-configmap.dist.yaml` file and rename it to `env-configmap.yaml` and fill the empty fields:


```
cp .env-configmap.dist.yaml .env-configmap.yaml

# Edit the env-configmap file
nano env-configmap.yaml

# Fill the following fields:
- `DJANGO_SUPERUSER_EMAIL`
- `DJANGO_SUPERUSER_FULL_NAME`
- `DJANGO_SUPERUSER_PASSWORD`
- `POSTGRES_PASSWORD`
```

Then run the deploy.sh script to launch the deployment:

```
bash deploy.sh
```

Launch the following link: [http://<EXTERNAL_IP>:31280/](http://<EXTERNAL_IP>:31280/)
The external IP can be extracted by typing `kubectl get services -n cabbage`

### Local (for Debugging - Python 3.10 and later)

You must add the `.env` file to the root of this project. You can add it by copying the `.env.dist` file and rename it `.env`.

```
cd ./cabbage
cp .env.dist .env

# Edit the .env file
nano .env
```

You must make sure that you have a configured Postgres database.
Then, create a virtual environment and install the dependencies:

```
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

Then launch the local server:

`python manage.py runserver`

Then open the following link : [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
