import math

def isInside(x,y):
	dist = math.pow((x-50),2) + math.pow((y-50),2)
	if math.sqrt(dist) <= 50:
		return True
	else:
		return False

def angle_sector(perc):
	return float(float(perc)/100*360)


def angle_point(x_coord,y_coord):
	shift = 50
	x = float(x_coord - shift)
	y = float(y_coord - shift)

	x1 = float(50 - shift)
	y1 = float(100 - shift)

	dot_prod = float(x1*x + y1*y)

	mag = math.sqrt(math.pow(x,2) + math.pow(y,2))
	mag = float(mag)*float(50)
	
	cos = float(dot_prod)/float(mag)
	return math.degrees(math.cos(cos))


def borw(perc, x_coord, y_coord):
	if (isInside(x_coord,y_coord) and angle_point(x_coord,y_coord) < angle_sector(perc)):
		return 'black'
	else:
		return 'white'






t = int(input())
for q in range(t):
	perc, x_coord, y_coord = map(int, input().split(' '))
	print('Case #'+str(q+1)+':', end =' ')
	print(borw(perc,x_coord,y_coord))

