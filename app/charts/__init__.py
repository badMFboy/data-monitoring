from flask import Blueprint

bp = Blueprint('Charts',__name__)

from app.charts import routes
