#File: hw3_part4.py
#Author: Raymond Trang
#Date: 03/02/18
#Section: IzSaRa
#E-mail: traymon1@umbc.edu
#Description: 
#	Program will output a 'counting' box

def count(width, height):
	start = 0
	#While there rows to iterate
	while start < height:
		#For every row to iterate
		for i in range(1, height + 1):
			#For every number in that row
			for x in range(width):
				#Increment by 1 and print
				start += 1
				print start,
			#After every number in a row, start new line
			print
		
def count_box():
	input1 = int(raw_input("Please enter a width: "))
	input2 = int(raw_input("Please enter a height: "))
	return count(input1, input2)

count_box()
 


