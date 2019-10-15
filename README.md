# Instaglam
​
This is an attempt at cloning the social media site instagram where users share comment and like photos and share experiences and fun moments.
​
## Getting Started
​
Fork this repository or clone it to your local machine on ubuntu use the following commands
```
git clone 
```
​
### Prerequisites
​
1. You will need to install the following for you you to be able to run the following application in your local machine.
* Python version 3.6
* postgres database
​
### Installing
​
A step by step series of examples that tell you how to get a development env running
​
1. set up a virtual environment using the following command
​
```
python3.6 -m venv --without-pip virtual
```
​
And activate it
​
```
source virtual/bin/activate
```
1. install the latest version of pip
​
```
curl https://bootstrap.pypa.io/get-pip.py | python
```
​
1. Install the requirements in the requirements.txt file using
```
pip install -r requirements.txt
```
1. create a .env file in your rootfolder and add the following configurations
```
SECRET_KEY='<random-string>'
DEBUG=True
ALLOWED_HOSTS='*'
DATABASE_URL='postgres://databaseowner:password@localhost/databasename'
```
1. create postgres database
```
CREATE DATABASE <your-database-name>
```
1. create a migration using the following command
```
python3.6 manage.py makemigrations
```
​
and migrate
```
python3.6 manage.py migrate
```
1. create a admin account
```
python 3.6 manage.py createsuperuser
```
and add your credentials
​
1. run the application using 
```
python3.6 manage.py runserver
```
1. navigate to the admin panel by typing 
```
localhost:8000/admin
```
​
​
End with an example of getting some data out of the system or using it for a little demo
​
## Running the tests
​
Run the system test by typing the following commands
```
python3.6 manage.py tests
```
​
## Deployment
​
View the following [document](https://github.com/jakhax/deploying-django-to-heroku-manual) inorder to deploy to a live system
​
## Built With
​
* [Django](https://www.djangoproject.com/download/) - The web framework used
* [Bootstrap](https://getbootstrap.com) - The css toolkit used
* Html
* Python
​
​
## Author
​
* **Christian Williams Jire** - *Initial work* - [chrisjire](https://github.com/chrisjire)
​
## License
​
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
