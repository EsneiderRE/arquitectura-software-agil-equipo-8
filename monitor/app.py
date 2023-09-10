from flask import Flask, jsonify
import time
import requests
import threading
from celery import Celery
import logging

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dbapp.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app_context = app.app_context()
app_context.push()
REQUEST_INTERVAL = 20
celery = Celery('tasks', broker='redis://localhost:6379/0',  backend='redis://localhost:6379/1')

logging.basicConfig(filename='app_monitor.log', level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

MICROSERVICES = {
    "grupo": "http://127.0.0.1:5002/grupo",
    "analitica": "http://127.0.0.1:5001/analitica"
}
MICROSERVICES_AVAILABILITY = {
    "grupo":True,
    "analitica": True
}

@app.route('/api-gateway/<service_name>', methods=['GET'])
def gateway(service_name):
    service_url = MICROSERVICES.get(service_name)
    if not service_url:
        return jsonify(error="Service not found"), 404
    if MICROSERVICES_AVAILABILITY[service_name]:
        response = requests.get(service_url)
        if response.status_code!=200:
            logging.error("Api gateway , Error en el servicio {}", service_name)
        return response.content, response.status_code
    else:
        return jsonify(error="Service is down or unreachable"), 503

@celery.task(name="notificar_error")
def registrar_error(error):
    pass


def check_microservice_status():
    while True:
        for microservice_url, microservice_name in [
            ("http://127.0.0.1:5002/grupo", "grupo"),
            ("http://127.0.0.1:5001/analitica", "analitica"),
        ]:
            try:
                response = requests.get(microservice_url, timeout=10)
                if response.status_code == 200:
                    MICROSERVICES_AVAILABILITY[microservice_name] = True
                    logging.info("{} se encuentra OK".format(microservice_name))
                else:
                    logging.error("Error en {}".format(microservice_name))
                    registrar_error.delay("Error en {}".format(microservice_name))
                    MICROSERVICES_AVAILABILITY[microservice_name] = False

            except requests.exceptions.RequestException as e:
                logging.error(e)
                logging.error("Error en {}".format(microservice_name))
                registrar_error.delay("Error en {}".format(microservice_name))
                MICROSERVICES_AVAILABILITY[microservice_name] = False

        time.sleep(REQUEST_INTERVAL)

# Start the background thread for monitoring
monitoring_thread = threading.Thread(target=check_microservice_status)
monitoring_thread.daemon = True
monitoring_thread.start()