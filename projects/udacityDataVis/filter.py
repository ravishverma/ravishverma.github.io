import csv

# Columns used to probe inputs and create output data
fields_in = ['Origin','Dest']
# Columns in output data; A1 A2 are airport codes Lat Lon are coordinates
fields_out = ['A1','A2','Lat1','Lon1','Lat2','Lon2','Points','BadFlights','TotalFlights']

codes = {}

# Airport codes: Newyork, Los Angeles, Chicago, Houston, Portland, Albuquerque
airports = ['JFK', 'LAX', 'ORD', 'IAH', 'PDX', 'ABQ']

# Reading geographical coordinates for each airport code
with open('Airport_LatLon_USA.csv','rU') as airportcode:
	reader = csv.reader(airportcode)
	for row in reader: codes[row[0]] = [row[1],row[2]]

# Scanning flight data for each year
for year in range(1987,2008+1):
	file_in = open('./originalData/'+str(year)+'.csv','rU')
	reader = csv.DictReader(file_in)

	# Segregating year wise data into each season
	# Winter
	file_outW = open('./udacityData/Flights_'+str(year)+'_W'+'.csv','w')
	writerW = csv.DictWriter(file_outW, fieldnames=fields_out)
	writerW.writeheader()
	# Spring
	file_outSp = open('./udacityData/Flights_'+str(year)+'_Sp'+'.csv','w')
	writerSp = csv.DictWriter(file_outSp, fieldnames=fields_out)
	writerSp.writeheader()
	# Summer
	file_outSu = open('./udacityData/Flights_'+str(year)+'_Su'+'.csv','w')
	writerSu = csv.DictWriter(file_outSu, fieldnames=fields_out)
	writerSu.writeheader()
	# Fall
	file_outF = open('./udacityData/Flights_'+str(year)+'_F'+'.csv','w')
	writerF = csv.DictWriter(file_outF, fieldnames=fields_out)
	writerF.writeheader()

	data = {}

	# Creating entries for output
	# All input entries are consolidated for each flight route
	for row in reader:
		check = {'Origin':row['Origin'],'Dest':row["Dest"],
		'DepDelay':row['DepDelay'],'Cancelled':row['Cancelled'],
		'Month':row['Month']}
		if 'NA' in check.values(): continue

		try:
			if row['Origin'] not in airports: continue
			if row['Dest'] not in airports: continue

			route = [row['Origin'],row['Dest']]

			route.sort()

			key = route[0]+route[1]+':'+row['Month']

			if key not in data:
				data[key] = {}
				data[key]['Points'] = 0.0
				data[key]['BadFlights'] = 0
				data[key]['TotalFlights'] = 0

			data[key]['A1'] = route[0]
			data[key]['A2'] = route[1]

			data[key]['Lat1'] = float(codes[route[0]][0])
			data[key]['Lon1'] = -float(codes[route[0]][1])

			data[key]['Lat2'] = float(codes[route[1]][0])
			data[key]['Lon2'] = -float(codes[route[1]][1])

			delayed = ( float(row['DepDelay']) >= 15 )
			cancelled = ( int(float(row['Cancelled'])) == 1 )

			# Given points to a flight route based on delay or cancellation of flight
			if cancelled:
				data[key]['Points'] = data[key]['Points'] + 0

			if delayed:
				data[key]['Points'] = data[key]['Points'] + 0.5

			if delayed and cancelled:
				data[key]['Points'] = data[key]['Points'] - 0.5

			if (not delayed) and (not cancelled):
				data[key]['Points'] = data[key]['Points'] + 1.0

			# Counting the number of flights
			if delayed or cancelled:
				data[key]['BadFlights'] = data[key]['BadFlights'] + 1

			data[key]['TotalFlights'] = data[key]['TotalFlights'] + 1
		except (KeyError, ValueError):
			continue

	# Writing the output data to different files based on year and season names 
	for key in data:
		month = key.split(':')[1]
		entry = data[key]

		# Winter 12, 1, 2
		if month in ['12','1','2']:
			writerW.writerow(entry)
		# Spring 3, 4, 5
		elif month in ['3','4','5']:
			writerSp.writerow(entry)
		# Summer 6, 7, 8
		elif month in ['6','7','8']:
			writerSu.writerow(entry)
		# Fall 9, 10, 11
		elif month in ['9','10','11']:
			writerF.writerow(entry)

	file_in.close()
	file_outW.close()
	file_outSp.close()
	file_outF.close()
	file_outSu.close()
