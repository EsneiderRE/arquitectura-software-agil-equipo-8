import logging

import requests
from celery import Celery

logger = logging.getLogger(__name__)
celery = Celery('tasks', broker='redis://localhost:6379/0')


@celery.task(name="notificar_error")
def registrar_error(error):
    logger.error(error)
