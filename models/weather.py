import sys
from backend.db import db




class WeatherInfoModel(db.Model):
    __tablename__="weather_info"
    
    locdatetime=db.Column(db.String(40),primary_key=True)
    location=db.Column(db.String(10),primary_key=True)
    updated_date=db.Column(db.String(13))  
    temperature=db.Column(db.Float())
    precipitation_form=db.Column(db.Float())
    precipitation_prob=db.Column(db.Float())
    humidity=db.Column(db.Float())
    wind_speed=db.Column(db.Float())
    wind_direction=db.Column(db.Float())
    cloud=db.Column(db.Float())
    

    
    
