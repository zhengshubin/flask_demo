from flask import  Flask
from user import user

@user.route('/')
def hello_world():
    return 'Hello World!'
