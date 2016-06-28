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

def schedulecost(sol):
	totalprice = 0
	latestarrival = 0
	earliestdep = 24*60

	for d in range(len(sol)/2):
		# Get the inbound and outbound flights
		origin = people[d][1]
		outbound = flights[(origin, destination)][int(sol[d])]
		returnf = flights[(destination, origin)][int(sol[d+1])]

		# Total price is the price of all outbound and reutrn flights
		totalprice += outbound[2]
		totalprice += returnf[2]

		# Track the latest arrival and earliest departure
		if latestarrival < getminutes(outbound[1]):
			latestarrival = getminutes(outbound[1])
		if earliestdep > getminutes(returnf[0]):
			earliestdep = getminutes(returnf[0])

		# Every person must wait at the airport until the latest person arrives.
		totalwait = 0
		for d in range(len(sol)/2):
			origin = people[d][1]
			outbound = flights[(origin, destination)][int(sol[d])]
			returnf = flights[(destination, origin)][int(sol[d+1])]
			totalwait += latestarrival - getminutes(outbound[1])
			totalwait += getminutes(returnf[0]) - earliestdep

		# Extra day of car rental? Extra $50
		if latestarrival > earliestdep:
			totalprice += 50

		return totalprice + totalwait