import random
from flask import Blueprint, current_app
from ...extensions import celery

bp = Blueprint('main', __name__)


@bp.route('/')
def index():
    return 'hello world'


@bp.route('/add')
def add():
    min, max = 1, 100
    x = random.randint(min, max)
    y = random.randint(min, max)
    task_add.delay(x, y)
    return 'add job submit'


@celery.task()
def task_add(x, y):
    result = x + y
    current_app.logger.info('%d + %d = %d' % (x, y, result))
    return result
