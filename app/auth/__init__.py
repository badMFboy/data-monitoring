from flask import Blueprint 

bp = Blueprint('Auth', __name__)

from app.auth import routes