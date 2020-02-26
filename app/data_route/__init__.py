from flask import Blueprint

bp = Blueprint('Data_route', __name__)

from app.data_route import routes
