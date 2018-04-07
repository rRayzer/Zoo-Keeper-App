#This is a Test Average Calculator

#Function to find average test grade
def test_grade(score):
	if score >= 90:
		letter = 'A'
	elif score >= 80:
		letter = 'B'
	elif score >= 70:
		letter = 'C'
	elif score >= 60:
		letter = 'D'
	else:
		letter = 'F'
	return letter

#Function/program
def test_average_calculator():
	test_grades = 0.0
	num_of_tests = 0
	user_input_valid = True

	#while loop to receive inputs
	while user_input_valid:
		user_input = raw_input("Please input test grade(s): ")
		if user_input == float:
			test_grades += user_input
			num_of_tests += 1

		elif user_input != float and user_input != 'x' and user_input.lower():
			print raw_input("Please enter valid test grade or 'x' to end: ")

		elif user_input == 'x':
			user_input_valid = False
			average_test = test_grades / num_of_tests
			print "Your test average is %.2f %%" % average_test
			print "Your test average letter grade is %s" % test_grade(average_test)
			

test_average_calculator()

