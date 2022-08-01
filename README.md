## Exigence pour le développement 

Pour travailler sur ce projet vous devez en premier installer :

``python (3.10+)`` et ``pip``

Et suivre les étapes suivantes 

#### 1 - Créer un environnement virtuel

Windows

```$ py -m venv geek_project```

Linux

```$ python3 -m venv geek_project```

Changer de répetoire

```$ cd geek_project```

#### 2 - Activer l'environnement

Windows

```$ Scripts\activate```

Linux

```$ source bin/activate```

#### 3 - Installation du projet

```bash
$ git clone https://github.com/TeraTra/geekTech.git

$ cd geekTech
```

#### 4 - Installation des dépendances

Windows

``$ pip install -r requirements.txt``

Linux

```bash
# Installer libpq-dev
$ sudo apt install libpq-dev

# Installer les dependances
$ pip3 install -r requirements.txt
```

#### 5 - Executer le serveur

Windows

```$ py manage.py runserver```

Linux

```$ python3 manage.py runserver```

Dans votre navigateur tapez : ``localhost:8000``
