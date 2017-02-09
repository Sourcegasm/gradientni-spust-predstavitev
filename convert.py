import sys
import math

#converts csv data from elyptic to rectangular coordinate system

def convert_line(line):
	year, day, r, lat, lon = line.split()
	r, lat, lon = float(r), float(lat), float(lon)
	x = r*math.cos(math.radians(lat))*math.cos(math.radians(lon))*10
	y = r*math.cos(math.radians(lat))*math.sin(math.radians(lon))*10
	# z = r*sin(math.radians(lat))
	return x, y

if __name__ == '__main__':
	if len(sys.argv) == 2 and sys.argv == 'help':
		print('Converts csv data from elyptic to rectangular coordinate system.')
		print('Usage: convert.py [input_file] [output_file] {scv_separator}')
		print('Default separator: \' \'')
		print('If separator is \'geogebra\', output will be set of geogebra points.')
	else:
		with open(sys.argv[1], 'r') as input_file, open(sys.argv[2], 'w') as output_file:

			if len(sys.argv) >= 3 and sys.argv[3] == 'geogebra':
				output_file.write('{')

			i = 0
			for line in input_file:
				x, y = convert_line(line)

				if len(sys.argv) >= 3:
					if sys.argv[3] == 'geogebra':
						if i > 0:
							output_file.write(',')
						output_file.write('('+','.join([str(x), str(y)])+')')
					else:
						output_file.write(sys.argv[3].join([str(x), str(y)])+'\n')
				else:
					output_file.write(' '.join([str(x), str(y)])+'\n')

				i += 1

			if len(sys.argv) >= 3 and sys.argv[3] == 'geogebra':
				output_file.write('}')

