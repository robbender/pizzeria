# pizzeria

## Create virtual environment:

`$ pip install virtualenv`
## windows
`python -m venv <venv-name>`
## To activate
`$ .\env\scripts\activate.bat`

## mac
`$ virtualenv venv --python=/usr/local/bin/python3`<br />

### Or <br />

``$ virtualenv venv -p `which python3` `` <br />
## To activate
`$ source <venv-name>/bin/activate`

## To deactivate
`$ deactivate`

## Install all packages from requirements.txt: <br />

`$ python3 -m pip install -r requirements.txt`  <br />

## to run locally:<br />
`$ python manage.py makemigrations`<br />
`$ python manage.py migrate`<br />


## link to live demo<br />
[Live Demo for testing](http://robertbender.pythonanywhere.com/)<br />
