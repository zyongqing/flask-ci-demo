from flask import Blueprint

bp = Blueprint("state", __name__)


@bp.route("/ready")
def ready():
    return "yes"
