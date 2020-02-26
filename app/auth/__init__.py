"""
Auth blueprint.
Packet contain two modules.
'forms.py' - contain class forms and it settings for login page.
'routes.py' - contain handlers for URLs.
"""
from flask import Blueprint 

bp = Blueprint('Auth', __name__)

from app.auth import routes