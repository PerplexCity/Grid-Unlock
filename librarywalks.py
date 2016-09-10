# the library version of the simulator is essentially the 8x8 simulator with a few variations

import random

# instead of writing a new set of rules for the final intersection, we simply expand the
# simulation by a block in each direction and then subtract extra walking time at the end

def dumbwalk(north, west):
	time = 0
	while north < 14:
		#vertical blocks have 40 second stops
		flip = random.randint(1,90)
		if flip < 41:
				time += flip
		north += 1
		time += 50

	while west<5:
		#horizontal blocks have 55 second stops
		flip = random.randint(1,90)
		if flip < 56:
			time += flip
		west += 1
		time += 100



	time += -150

	print round(time/float(60), 2)




def smartwalk(north, west):
	time = 0
	direction = "north"
	while north < 14 or west < 5:
		if north == 14:
			flip = random.randint(1,90)
			if flip < 56:
				time += flip
			west += 1
			time += 100
		elif west == 5:
			flip = random.randint(1,90)
			if flip < 41:
				time += flip
			north += 1
			time += 50
			
		else:
			if direction == "north":
				flip = random.randint(1,90)
				if flip < 41:
					direction = "west"
					west += 1
					time += 100
				else:
					north += 1
					time += 50
			
			elif direction == "west":
				flip = random.randint(1,90)
				if flip < 56:
					direction = "north"
					north += 1
					time += 50
				else:
					west += 1
					time += 100


	time += -150

	print round(time/float(60), 2)




# ten thousand trials
for i in range(10000):
	dumbwalk(0,0)	

# ten thousand trials
for i in range(10000):
	smartwalk(0,0)



