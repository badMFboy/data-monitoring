#-*-coding:utf-8-*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
from config import Config
from flask_login import LoginManager




db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
login.login_view = 'login'

def create_app(config_class = Config):
    
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app,db)
    login.init_app(app)

    from app.auth import bp as auth_bp
    app.register_blueprint(auth_bp)

    from app.charts import bp as charts_bp
    app.register_blueprint(charts_bp)

    from app.data_route import bp as data_route_bp
    app.register_blueprint(data_route_bp)

    from app.users import bp as users_bp
    app.register_blueprint(users_bp)



    return app





from app import models
