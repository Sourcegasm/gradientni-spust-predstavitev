import sys
import math

#converts csv data from elyptic to rectangular coordinate system

if len(sys.argv) == 2 and sys.argv == 'help':
	print('Converts csv data from elyptic to rectangular coordinate system.')
	print('Usage: convert.py [input_file] [output_file] {scv_separator}')
	print('Default separator: \' \'')
else:
	with open(sys.argv[1], 'r') as input_file, open(sys.argv[2], 'w') as output_file:
		for line in input_file:
			year, day, r, lat, lon = line.split()
			r, lat, lon = float(r), float(lat), float(lon)
			x = r*math.cos(math.radians(lat))*math.cos(math.radians(lon))*10
			y = r*math.cos(math.radians(lat))*math.sin(math.radians(lon))*10
			# z = r*sin(math.radians(lat))

			if len(sys.argv) >= 3:
				output_file.write(sys.argv[3].join([str(x), str(y)])+'\n')
			else:
				output_file.write(' '.join([str(x), str(y)])+'\n')

