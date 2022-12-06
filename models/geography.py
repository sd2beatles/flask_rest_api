import sys
sys.path.append("..")
from db import db



class GeoModel(db.Model):
    __tablename__='geography'
    
    locdate=db.Column(db.String(20),primary_key=True)
    location=db.Column(db.String(10),primary_key=True)
    updated_date=db.Column(db.String(15))
    altitudeMeridian=db.Column(db.String(20))
    altitude_09=db.Column(db.String(20))
    altitude_12=db.Column(db.String(20))
    altitude_15=db.Column(db.String(20))
    altitude_18=db.Column(db.String(20))
    azimuth_09=db.Column(db.String(20))
    azimuth_12=db.Column(db.String(20))
    azimuth_15=db.Column(db.String(20))
    azimuth_18=db.Column(db.String(20))
    