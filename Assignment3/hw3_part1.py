#File: hw3_part1.py
#Author: Raymond Trang
#Date: 03/01/18
#Section: IsArA
#E-mail: traymon1@umbc.edu
#Description:
#	Program will wish user "happy birthday" for their age

def happy_birthday():
	valid_age = True
	while valid_age:
		age = int(raw_input("Please enter your age: "))
		if age > 125:
			print "An age of", age, "is not possible."
			print "No one has ever lived more than 125 years."
			continue
		elif age < 0:
			print "It's impossible to be negative years old."
			continue
		else:
			print "Happy", age, "th birthday!"
			valid_age = False

happy_birthday()

