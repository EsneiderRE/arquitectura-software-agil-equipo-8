from flask import Flask
import time
import requests
import threading
from celery import Celery

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dbapp.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app_context = app.app_context()
app_context.push()

REQUEST_INTERVAL = 10
celery = Celery('tasks', broker='redis://localhost:6379/0',  backend='redis://localhost:6379/1')

@celery.task(name="notificar_error")
def registrar_error(error):
    pass


def check_microservice_status():
    while True:
        for microservice_url, microservice_name in [
            ("http://127.0.0.1:5000/grupo", "VistaGrupos"),
            ("http://127.0.0.1:5000/analitica", "VistaAnaliticas"),
        ]:
            try:
                response = requests.get(microservice_url, timeout=2)
                if response.status_code != 200:
                    registrar_error.delay("Error en {}".format(microservice_name))

            except requests.exceptions.RequestException as e:
                registrar_error.delay("Error en {}".format(microservice_name))

        time.sleep(REQUEST_INTERVAL)

# Start the background thread for monitoring
check_microservice_status()
#monitoring_thread = threading.Thread(target=check_microservice_status)
#monitoring_thread.daemon = True
#monitoring_thread.start()