# Great Circle Distances between geographic points

# import the math functions we need.
from math import radians, acos, sin, cos, fabs

def convert(num):
    return radians(num[0]), radians(num[1])

def lawOfCosines(geo1, geo2):
    # The geographic coordinates are tuples with latitude and longitude values
	# convert the geographic coordinates to radians and compute absolute differences
	# Use the Law of Cosines formula to determine the central angle
    r1 = convert(geo1)
    r2 = convert(geo2)
    
    # formula time 
    delta_longitude = fabs(r2[1] - r1[1])
    delta_latitude  = fabs(r2[0] - r1[0]) # not sure i need this but assignment says convert it so whatever

    return acos(sin(r1[0]) * sin(r2[0]) + cos(r1[0]) * cos(r2[0]) * cos(delta_longitude))


def distance(radius,centralAngle):
    # The distance is the radius of the earth times the calculated central angle
	# Return the unrounded integer distance
    return int(radius * centralAngle)

def main():
	# obtain two geographic points as tuples
	geo1 = (float(input('latitude  #1?\n')), float(input('longitude #1?\n')))
	geo2 = (float(input('latitude  #2?\n')), float(input('longitude #2?\n')))
	# obtain the radius of the earth
	radius = float(input('radius of earth?\n'))
	# print distance between points
	dis = distance(radius, lawOfCosines(geo1, geo2))
	print('the distance from', geo1, 'to', geo2, 'is', dis)


# do not change the following code
if __name__ == '__main__':
    main()
