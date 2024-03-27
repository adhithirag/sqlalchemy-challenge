# Import the dependencies.
import numpy as np
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify
  

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///../Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(autoload_with = engine)

# Save references to each table
measurement = Base.classes.measurement
station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)




#################################################
# Flask Routes
#################################################
@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Welcome to the Hawaii Climate API!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs"
    )

#precipitation route
@app.route("/api/v1.0/precipitation")
def precipitation():
    session = Session(engine)
    
    #precipitation query to return the JSON with date as the key and value as precipitation
    year_ago = dt.date(2017,8,23) - dt.timedelta(days=365)
    sel = [measurement.date, measurement.prcp]
    
    past_twelve_months = session.query(*sel).filter(measurement.date >= year_ago).all()
    
    session.close()
    
    prcp_data = list(np.ravel(past_twelve_months))
    
    return jsonify(prcp_data)

    
#stations route
@app.route("/api/v1.0/stations")
def stations():
    station = Base.classes.station
    session = Session(engine)
    
    #stations query 
    check = session.query(station.name, station.station).all()
    
    session.close()
    
    
    # Create a dictionary from the stations and append to a list of all_stations
    all_stations = []
    for name, station in check:
        station_dict = {}
        station_dict["name"] = name
        station_dict["station"] = station
        all_stations.append(station_dict)

    return jsonify(all_stations)


#tobs route
@app.route("/api/v1.0/tobs")
def tobs():
    session = Session(engine)
    
    #query for the tobs data for the most active station
    year_ago = dt.date(2017,8,23) - dt.timedelta(days=365)
    sel = [measurement.date, measurement.tobs]
    
    most_active_station = session.query(*sel).filter(measurement.date >= year_ago).filter(measurement.station == 'USC00519281').all()
    
    session.close()
    
    tobs_data = list(np.ravel(most_active_station))
    
    return jsonify(tobs_data)







if __name__ == '__main__':
    app.run(debug=True)

