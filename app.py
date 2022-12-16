from flask import Flask
from flask_smorest import Api
from flask_jwt_extended import JWTManager
from resources.geography import blp as GeoBluePrint
from resources.weather import blp as WeatherPrint
from configparser import ConfigParser
from db import db
import os


def get_value(path,key,value,interpolation=True):
    # if you want to avoid interpolation,set interpolation as False
    parser=ConfigParser() if interpolation else ConfigParser(interpolation=None)
    
    parser.read(path)
    return parser.get(key,value)


def create_app(db_url=None):
    user,passwd=get_value('dev.ini','mysql','user'),get_value('dev.ini','mysql','password')
    ip_address=get_value('dev.ini','mysql','ip')
    
    user,passwd,ip_address=os.getenv("user"),os.getenv("password"),os.getenv("ip")
    
    app=Flask(__name__)

    app.config["PROPAGATE_EXCEPTIONS"]=True
    app.config["API_TITLE"]="Stores REST API"
    app.config["API_VERSION"]="v1"
    app.config["OPENAPI_VERSION"]="3.0.3"
    app.config["OPENAPI_URL_PREFIX"]="/"
    app.config["OPENAPI_SWAGGER_UI_PATH"]="/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"]="https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    #app.config["SQLALCHEMY_DATABASE_URI"]=db_url or os.getenv("DATABASE_URL","sqlite:///data.db")
    app.config["SQLALCHEMY_DATABASE_URI"]="mysql+pymysql://{0}:{1}@{2}:3306/solardb"\
        .format(user,passwd,ip_address)
    #mysql+pymysql
    app.config["SQLALCHEMY_TRACK_MODIFICATION"]=False
    db.init_app(app)
    api=Api(app)
    
    @app.before_first_request
    def create_tables():
        db.create_all()
    
    api.register_blueprint(GeoBluePrint)
    api.register_blueprint(WeatherPrint)
    return app
        
