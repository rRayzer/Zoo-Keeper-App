#File: hw3_part.py
#Author: Raymond Trang
#Date: 03/01/18
#Section: IsZaRa
#E-mail: traymon1@umbc.edu
#Decription:
#	Simulate the up and down movement of a hailstone in a storm

#Function to calculate height
def height_calculator(hail):
	hailstone_valid = True
	if hail == 0 or hail == 1:
		print "Hail stopped at height %d" % hail
		hailstone_valid = False	

	else:
		print "Hail is currently at height %d" % hail

	while hailstone_valid:
		#If even, divide by 2
		if hail % 2 == 0:	
			hail = hail / 2
			#If 1, stop
			if hail == 1:
				print "Hail stopped at height %d" % hail
				hailstone_valid = False
			#If not 1, keep printing
			else:
				print "Hail is currently at height %d" % hail

		else:
			#Else, keep multiplaying by 3 and adding 1
			hail = hail * 3 + 1
			print "Hail is currently at height %d" % hail

start = True
#Loop to ask for correct input if user inputs incorrectly, extra credit? ;-)
while start: 		
	try:
		hailstone = int(raw_input("Please enter the starting height of the hailstone: "))
		height_calculator(hailstone)
		start = False
	except ValueError:
		print "Please enter valid height."