import logging
from celery.signals import after_setup_logger
from celery import Celery

celery = Celery('tasks', broker='redis://localhost:6379/0')

@after_setup_logger.connect
def setup_loggers(logger, *args, **kwargs):
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh = logging.FileHandler('app_errores_microservicio.log')
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(formatter)
    logger.addHandler(fh)

@celery.task(name="notificar_error")
def registrar_error(error):
    logging.error(error)
