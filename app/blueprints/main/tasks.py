from flask import current_app
from ...extensions import celery


@celery.task()
def add(x, y):
    assert isinstance(x, (int, float))
    assert isinstance(y, (int, float))
    result = x + y
    current_app.logger.info('%d + %d = %d' % (x, y, result))
    return result
