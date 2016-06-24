import time
import random
import math

people = [('Seymour','BOS'),('Franny','DAL'),('Zooey','CAK'),('Walt','MIA'),('Buddy','ORD'),('Les','OMA')]
location = {'BOS':'Boston','DAL':'Dallas','CAK':'Akron','MIA':'Miami','ORD':'Chicago','OMA':'Omaha'}
# laGuardia airport in New York
destination = 'LGA'

flights={}

for line in file('data/schedule.txt'):
	origin, dest, depart, arrive, price = line.strip().split(',')
	flights.setdefault((origin, dest),[])

	# Add details to the list of possible flights
	flights[(origin, dest)].append((depart, arrive, int(price)))

def getminutes(t):
	x = time.striptime(t, '%H:%M')
	return x[3]*60+x[4]

# Example list = [1,4,3,2,7,3,6,3,2,4,5,3]
# Each 2 numbers define the flight number to and back
# 1 means Seymour will take second flight from Boston to New york
# 4 means Seymour will take fifth flight to come back to Boston

def printschedule(r):
	for d in range(len(r)/2):
		name = people[d][0]
		origin = people[d][1]
		out = flights[(origin, dest)][r[d*2]]
		ret = flights[(dest, origin)][r[d*2+1]]
		print '%10s%10s %5s-%5s $%3s %5s-%5s $%3s' % (name, location[origin], out[0], out[1], out[2], ret[0], ret[1], ret[2])