from flask import request,make_response
from flask.views import MethodView
from flask_smorest import Blueprint,abort
from sqlalchemy.exc import SQLAlchemyError
from schema import PlainGeoSchema,GeoUpdateSchema,GeoParamSchema,GeoSearchAll
from models.geography import GeoModel
from datetime import datetime
from sqlalchemy.exc import SQLAlchemyError,IntegrityError
from backend.db import db


blp=Blueprint("geography",__name__,description="Operation on Geo Information")





@blp.route("/geo/indvidual")
class GeoList(MethodView):
    @blp.arguments(GeoParamSchema)
    @blp.response(200,GeoUpdateSchema)
    def get(self,record):
        data=GeoModel.query.filter_by(location=record['location'],locdate=record['locdate']).first()
        return data
    
    @blp.arguments(PlainGeoSchema)
    @blp.response(200,GeoUpdateSchema)
    def put(self,record):
     
        #add current date
        
        record['updated_date']=datetime.utcnow().strftime("%Y-%m-%d")
        
        match=GeoModel(**record)
        try:
            db.session.add(match)
            db.session.commit()
            
        except IntegrityError:
            abort(400,message="The current infomration has alread exists")
            
        return record
            
    @blp.arguments(GeoParamSchema)
    def delete(self,record):
        data=GeoModel.query.filter_by(location=record['location'],locdate=record['locdate']).first()
        if data:
            db.session.delete(data)
            db.session.commit()
            return make_response({"message":"The selected item deleted!"},200)
        else:
            return make_response({"message":"The item not found!"},404)
        
@blp.route("/geo")
class GeoList(MethodView):
    @blp.arguments(GeoSearchAll)
    @blp.response(200,PlainGeoSchema(many=True))
    def get(self,record):
        data=GeoModel.query.filter_by(location=record['location']).all()
        return data
    
    
    
        
        





