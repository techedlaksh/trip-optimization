import time
import random
import math

people = [('Seymour','BOS'),('Franny','DAL'),('Zooey','CAK'),('Walt','MIA'),('Buddy','ORD'),('Les','OMA')]

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