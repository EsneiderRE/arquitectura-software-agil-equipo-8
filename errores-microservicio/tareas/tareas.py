import logging

import requests
from celery import Celery

logger = logging.getLogger(__name__)
celery = Celery('tasks', broker='redis://localhost:6379/0')
logging.basicConfig(filename='app_errores_microservicio.log', level=logging.DEBUG,
                        format='%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')


@celery.task(name="notificar_error")
def registrar_error(error):
    logging.error(error)
