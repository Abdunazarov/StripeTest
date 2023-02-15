# Introduction
This project implements Stripe's Web APIs using python for making online payments

## Testing link
You can have a look and test the app [here in pythonanywhere](http://teststripe.pythonanywhere.com/)

## Installation & creating virtual env
Create a virtual env in order to install required libraries

```bash
python3 -m venv <virtual-env-path>.
```
afterwards, activate your virtual env and then run:
```bash
pip install -r requirements.txt
```

## Usage
Create a superuser to log in to the Django's admin site and then create some Item objects
```bash
python manage.py createsuperuser
```
and then run the following command to run the server
```bash
python manage.py runserver
```

## Walkthrough
There should be Item objects in the home page (`http://127.0.0.1:8000/`), click to an item, it redirects you to `http://127.0.0.1:8000/item/<id>` page. Here, you can press the `buy` button, which return the Stripe's checkout page, where you can fill the form details.
