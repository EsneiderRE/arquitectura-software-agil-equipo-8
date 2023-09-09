from flask import Flask
from flask_restful import Api
app = Flask(__name__)

app_context = app.app_context()
app_context.push()