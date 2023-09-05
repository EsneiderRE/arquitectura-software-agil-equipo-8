from flask import Flask

app = Flask(__name__)

#app.config["SQLALCHEMY_DATABASE_URI"] = ""
#app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
#app.config["JWT_SECRET_KEY"] = "frase-secreta"
app.config["PROPAGATE_EXCEPTIONS"] = True

app_context = app.app_context()
app_context.push()
