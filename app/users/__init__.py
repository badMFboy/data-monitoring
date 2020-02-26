from flask import Blueprint

bp = Blueprint("Users",__name__)

from app.users import routes