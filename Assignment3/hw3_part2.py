#File: hw3_part2.py
#Author: Raymond Trang
#Date: 03/01/18
#Section: IzZy
#E-mail: traymon1@umbc.edu
#Description:
#	Calculate answer to integer division problem

def division(divisor, dividend):



	result = 0
	count = 0
	while dividend != 0: #Only intiate if dividend is not 0
		if dividend < divisor: 
			divisor -= dividend 
			result += 1 #This becomes the answer

		elif dividend > divisor: #Once the dividend > divisor, return the result
			return result

		elif dividend == divisor: #If they're the same number, return 1 
			result += 1
			return result
		count += 1
		print "count: " + str(count)
def calculate():
	input1 = int(raw_input("Please enter the first number: "))
	input2 = int(raw_input("Please enter the second number: "))
	#Call that division function
	print input1, " // ", input2, " = ", division(input1, input2) 
	
calculate()



