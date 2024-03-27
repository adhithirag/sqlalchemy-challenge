# sqlalchemy-challenge

In this challene, the goal was to do a basic climate analysis and explore the data that was provided on the climate in Hawaii. 

## PART 1
- The first step is to import the necessary dependencies to be able to use the SQLite database in Jupyter
- Then we want to connect our SQLite database using the create_engine function
- We reflect our two tables into classes: station and measurement
- Then we create a session to link Python to our databse 

## Precipitation Analysis
- Find the most recent date in the dataset
- Using that date, we want to get the last 12 months of the precipitation data
- We are going to load the query results into a Pandas dataframe  and plot the data using matplotlib

## Station Analysis
- Query the total number of stations in the station class
- Query to find the most active stations
- Calculate the lowest, highest, and average temperatures of the most active station
- Query the previous 12 months of the temperature observation (TOBS) data and plot the results as a histogram


## Part 2 
- Designing the climate app using Flask to create three static routes 

/api/v1.0/precipitation
/api/v1.0/stations
/api/v1.0/tobs
