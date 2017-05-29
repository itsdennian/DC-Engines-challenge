import math


def isInside(x,y):





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

