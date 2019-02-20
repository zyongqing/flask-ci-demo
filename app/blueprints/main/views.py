import random
from flask import Blueprint
from .tasks import add as task_add

bp = Blueprint("main", __name__)


@bp.route("/")
def index():
    return "welcome to CI/CD world 🌏"


@bp.route("/add")
def add():
    min, max = 1, 100
    x = random.randint(min, max)
    y = random.randint(min, max)
    try:
        task_id = task_add.delay(x, y)
        return "submit add job success {} 😄".format(task_id)
    except Exception:
        return "submit add job failed 😅"
