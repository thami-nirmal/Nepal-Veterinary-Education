# How to install on windows
1. clone this project
2. create new virtual environment
```
py -m venv env
```
4. activate the new virtual
```
.\env\Scripts\activate
```
6. install requirements.txt
 ```
pip install -r requirements.txt
```
9. run local server to begin
```
py manage.py runserver
```
12. go live with localhost:8000

# To access admin panel

 1. run on trimnal 
 ```
 py manage.py createsuperuser
 ```
 2. create new admin user
 2. go to [localhost:8000/admin](http://localhost:8000/admin)
