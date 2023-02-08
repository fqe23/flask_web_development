#from my_app import app
from flask import Blueprint

hello = Blueprint("hello",__name__)

@hello.route("/")
@hello.route("/hello")
def hello1():
    return "Hola Blueprint" 
    

