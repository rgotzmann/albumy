# Albumy

*Capture and share every wonderful moment.*

> Example application for *[Python Web Development with Flask](https://helloflask.com/en/book/1)* (《[Flask Web 开发实战](https://helloflask.com/book/1)》).

Demo: http://albumy.helloflask.com

![Screenshot](https://helloflask.com/screenshots/albumy.png)

## Installation

Note: This version of Albumy requires Python 3.9 due to compatibility with older dependencies. 
Python 3.10+ will not work without an update package rabbit hole. 

clone:
```
$ git clone https://github.com/greyli/albumy.git
$ cd albumy
```
create & activate virtual env then install dependency:

with venv/virtualenv + pip:
```
$ python3.9 -m venv env 
$ source env/bin/activate  # use `env\Scripts\activate` on Windows
$ pip install Pillow>=10.0.0 # upgrade Pillow and update requirements.txt
$ pip install -r requirements.txt
```
or with Pipenv:
```
$ pipenv install --dev
$ pipenv shell
```
Initialize database, generate fake data then run:
```
$ flask initdb
$ flask forge
$ flask run
* Running on http://127.0.0.1:5000/
```
Test account:
* email: `admin@helloflask.com`
* password: `helloflask`

## License

This project is licensed under the MIT License (see the
[LICENSE](LICENSE) file for details).
