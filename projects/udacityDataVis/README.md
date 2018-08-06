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
1. BadFlights: Count of the flights that are either delayed more than 15 minutes or cancelled
1. Points: This represents the quality of flight. I award 0 for every cancellation, 0.5 for every delayed flight if the delay is more than 15 minutes or 1.0 otherwise.

The filtered dataset contains flight data between only 6 airports
1. New York
1. Chicago
1. Los Angeles
1. Portland
1. Houston
1. Albuquerque

I have further split the data into different files based on the season of the year.

## The Visualization
Using the new data, I have created a visualization using JavaScript d3 library. The visualization gives three major information for air travel in any particular year and season,
1. Number of flights for every route -> In the form of thickness of the lines
1. Quality score on each route -> This is average Points/Flight for the route shown in color code. In earlier versions, I had used an inverted score representing bad quality, but it was difficult to interprete.
1. Fixed Summary -> This contains total flights and average quality score for all the routes in the selected time period
1. Tool Tip for Every Flight Route -> This shows some data for every route on mouseover

In the first version of visualization, I lacked contrast and ease of noting information. Based on the feedbacks from my friends, I refined the graphics, page layout and added animations into the final version. The animation helps in conveying a message to a visitor and also explain the graphics to some extent.

### Feedbacks

_"Format of display is really nice. What seems off are the choice of colors. Some of the flight routes are really thin and do not get observed as easily"_ - **Friend 1**


_"There is no take away for a lazy visitor. Only way to get numeric detail is to hover over the graphics. Also, the layout is different on my tablet and my desktop"_ - **Friend 2**


_"It would become more attention grabing if an overall summary is shown to visitors during landing."_ - **Friend 3**

## Summary

I noticed some interesting things about the air traffic. Below are my discoveries,

- The visualization shows air traffic between Newyork, Chicago, Los Angeles, Houston, Albuquerque and Portland
- Since 1987, the air traffic has increased by 400%
- In general, Summer season experiences 12% more air travel than Winter season
- Many routes face frequent departure delays but cancellations are rare
- The quality of air travel has stayed up high. It has never been below 0.85. This implies that fewer flights have suffered long delays or cancellations
- By far, the Spring of 1994 has been the best period of air travel, with a score of 0.95