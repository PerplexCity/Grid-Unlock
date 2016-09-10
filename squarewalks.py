import random

def dumbwalk(north, east):
	# set timer
	time=0

	# walks north until nothern boundary is reached, confronts stoplight (flip) before each block
	while north < 8:
		flip = random.randint(0,1)
		if flip == 1:
			time += 1
		north += 1
		time += 1

	# then walks east until finish line, confronts stoplight (flip) before each block
	while east < 8:
		flip = random.randint(0,1)
		if flip == 1:
			time += 1
		east += 1
		time += 1


	print time


def smartwalk(north, east):
	# set timer
	time = 0

	# begins walk facing north
	direction = "north"
	
	# iterates until finish line achieved 
	while north < 8 or east < 8:
		# walk approximates dumbwalk on either border
		if north == 8:
			flip = random.randint(0,1)
			if flip == 1:
				time += 1
			east += 1
			time += 1
		
		elif east == 8:
			flip=random.randint(0,1)
			if flip == 1:
				time += 1
			north += 1
			time += 1
			
		# otherwise walker will continue in direction if given greenlight and pivot for reds
		else:
			if direction == "north":
				flip = random.randint(0,1)
				if flip == 1:
					direction = "east"
					east += 1
					time += 1
				else:
					north += 1
					time += 1
			
			elif direction == "east":
				flip = random.randint(0,1)
				if flip == 1:
					direction = "north"
					north += 1
					time += 1
				else:
					east += 1
					time += 1

	print time
	
# ten thousand trials
for i in range(10000):
	dumbwalk(0,0)	

# ten thousand trials
for i in range(10000):
	smartwalk(0,0)


