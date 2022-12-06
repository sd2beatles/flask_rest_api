from marshmallow import Schema,fields
from pkg_resources import require

  
#===========weather schemas=====================
class PlainWeatherSchema(Schema):
    locdatetime=fields.Str(required=True)
    location=fields.Str(required=True)
    temperature=fields.Float()
    precipitation_form=fields.Float()
    precipitation_prob=fields.Float()
    humidity=fields.Float()
    wind_speed=fields.Float()
    wind_direction=fields.Float()
    cloud=fields.Float()
   
    
    
    
class WeatherSchema(PlainWeatherSchema):
    updated_date=fields.Str(required=True)
  
    


    
class WeatherSearchSchema(Schema):
    location=fields.Str(required=True)
    updated_date=fields.Str(required=True)
    

#======================geo schemas===========================

class PlainGeoSchema(Schema):
    locdate=fields.Str(required=True)
    location=fields.Str(required=True)
    altitudeMeridian=fields.Str()
    altitude_09=fields.Str()
    altitude_12=fields.Str()
    altitude_15=fields.Str()
    altitude_18=fields.Str()
    azimuth_09=fields.Str()
    azimuth_12=fields.Str()
    azimuth_15=fields.Str()
    azimuth_18=fields.Str()
 
class GeoUpdateSchema(PlainGeoSchema):
     updated_date=fields.Str(required=True) 
     
     
class GeoParamSchema(Schema):
    locdate=fields.Str()
    location=fields.Str()
    
    
class GeoSearchAll(Schema):
    location=fields.Str()
    
