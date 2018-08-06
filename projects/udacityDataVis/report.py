import csv
from pprint import pprint as pp

years = range(1987,2008+1)

seasons = ['W','Sp','F','Su']

print 'Overall'

data = {}

for y in years:
	for s in seasons:
		points = 0
		flights = 0
		with open('./udacityData/Flights_'+str(y)+'_'+s+'.csv','rU') as file:
			reader = csv.DictReader(file)
			for row in reader:
				points = points + int(float(row['Points']))
				flights = flights + int(float(row['TotalFlights']))

		if flights>0: data[str(y)+'_'+s] = float(points)/flights

minp = min(data.values())
maxp = max(data.values())

for key in data:
	if minp == data[key]: print 'Min: ', key, data[key]
	if maxp == data[key]: print 'Max: ', key, data[key]

print '\nSeason wise'

data = {}

for s in seasons:
	points = 0
	flights = 0
	for y in years:
		with open('./udacityData/Flights_'+str(y)+'_'+s+'.csv','rU') as file:
			reader = csv.DictReader(file)
			for row in reader:
				points = points + int(float(row['Points']))
				flights = flights + int(float(row['TotalFlights']))

	if flights>0: data[s] = flights

pp(data)

print '\nYear wise'

data = {}

for y in years:
	points = 0
	flights = 0
	for s in seasons:
		with open('./udacityData/Flights_'+str(y)+'_'+s+'.csv','rU') as file:
			reader = csv.DictReader(file)
			for row in reader:
				points = points + int(float(row['Points']))
				flights = flights + int(float(row['TotalFlights']))

	if flights>0: data[y] = flights

pp(data)