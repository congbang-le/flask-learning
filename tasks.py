from celery import Celery

celery = Celery('tasks', backend='db+postgresql://postgres:12345@172.17.0.2:5432/celery_test', broker='redis://172.17.0.3:6379/0')
celery.conf.update(result_extended=True)

@celery.task
def sum_int(a, b):
    return a + b