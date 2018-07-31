from flask import Flask
#from myapp import setting 

app = Flask(__name__)
from myapp.controller import  law_c

app.config.from_object('myapp.setting')
app.config.from_envvar('FLASKR_SETTINGS')
