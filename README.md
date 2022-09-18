# Dash API

Dash API is a Django REST API providing a way to manage multiple collections of flash cards locally.

## Installation

### Cloning the repository

Start by cloning the repository to get the files on your machine.

```bash
git clone git@github.com:AlexisMoins/dash-api.git ~/somewhere-on-your-machine
```

### Fetching the dependencies

**Note:** This repository uses [poetry](https://python-poetry.org) as a dependency manager but also provides a `requirements.txt` file to use with **pip**. Consider creating a virtual environment in case you're using **pip**.

- if you're using **poetry** :
```bash
poetry install
```

- if you're using **pip**:
```bash
pip install -r requirements.txt
```

If everything goes well, you should now have all the required dependencies installed on your machine.

## Setting up

For the django server to work, you now need to generate your very own `SECRET_KEY` (not to mention that once generated, you should not make it available publically). To do so, activate your virtual environment first and execute the following command :
```bash
./generate_secret_key
```

Then copy / paste the result into a file called `.env`, located at the root of the project, while following the template below :
```
SECRET_KEY = paste-your-key-here
```

## Launching the server

You can now start the django server using the command :
```bash
python manage.py runserver
```
