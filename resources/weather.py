
import os 
from flask import request,make_response
from flask.views import MethodView
from flask_smorest import Blueprint,abort
from sqlalchemy.exc import SQLAlchemyError
import sys
sys.path.append("..")
from db import db
from schema import PlainWeatherSchema,WeatherSchema,WeatherSearchSchema
from models.weather import WeatherInfoModel
from datetime import datetime
from sqlalchemy.exc import SQLAlchemyError,IntegrityError



blp=Blueprint("weather",__name__,description="Operation on Weather Information")


@blp.route("/weather/dateby")
class WeatherList(MethodView):
    @blp.arguments(WeatherSearchSchema)
    @blp.response(200,WeatherSchema(many=True))
    def get(self,record):
        data=WeatherInfoModel.query.filter_by(location=record['location'],updated_date=record["updated_date"]).all()
        return data
        
    @blp.arguments(PlainWeatherSchema)
    @blp.response(200,WeatherSchema)
    def put(self,record):
        record['updated_date']=datetime.utcnow().strftime("%Y-%m-%d")
        item=WeatherInfoModel(**record)
        
        try:
            db.session.add(item)
            db.session.commit()
            
        except IntegrityError:
            abort(400,message="The current infomration has alread exists")
            
        return record 
        
