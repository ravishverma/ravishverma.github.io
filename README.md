# Air Travel in USA

## Source of Data

I have obtained the data set from the website of **American Statistical Association**. The original dataset has many details related to commercial flights between 1987 and 2008. More details can be found [here](http://stat-computing.org/dataexpo/2009/the-data.html)

In addition to the original data, I also downloaded another dataset that maps each airport code to geographical coordinates. I have included the dataset in the project files. This datset can also be found [here](https://opendata.socrata.com/dataset/)

## Filtered & Derived Data

It, ofcourse, would not have made sense to have retained every field in the dataset. So I created a python script that parses the original data and extracts just the following fields,
1. Origin -> Airport code of flight origin
1. Dest -> Airport code of flight destination
1. Month -> The month in which the filght was scheduled
1. DepDelay -> Departure delay for the flight
1. Cancelled -> Indicator to mark a cancelled flight

Using the above fields, I have created some new fields,
1. A1, A2: These two fields have airport codes of airports connected by the flight
1. Lat1, Lat2: Latitude coordinates of each airport
1. Lon1, Lon2: Longitude coordinates of each airport
1. TotalFlights: Total flights on the route
1. BadFlights: Count of the flights that are either delayed or cancelled
1. Points: This represents the bad quality of flight. I add 1 for dely and 2 for cancellation

The filtered dataset contains flight data between only 6 airports
1. New York
1. Chicago
1. Los Angeles
1. Portland
1. Houston
1. Albuquerque

I have further split the data into different files based on the season of the year.

## The Visualization
Using the new data, I have created a visualization using JavaScript d3 library. The visualization give three major information for air travel in any particular year and season,
1. Number of flights for every route
1. Suffering score on each route -> This is an average of points for delay and cancellation
1. Summary -> This contains total flights and suffering score for all the routes in the selected time period


## Feedbacks
	_"Format of display is really nice. What seems off are the choice of colors. Some of the flight routes are really thin and do not get observed as easily"_ - *Friend 1*


	_"There is no take away for a lazy visitor. Only way to get numeric detail is to hover over the graphics."_ - *Friend 2*


	_"It would become more attention grabing if an overall summary is shown to visitor during landing."_ - *Friend 3*