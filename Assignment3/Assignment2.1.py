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

test_grades = 0.0
num_of_tests = 0

user_input = raw_input("Please input test grade(s): ")

#Function to validate user input
def test_input(user_input_check):
	while user_input != 'x':
		test_grades += user_input
		num_of_tests += 1

		if user_input == 'x':
			average_test = test_grades / num_of_tests
			print "Your test average is %.2f %%" % average_test
			print "Your test average is letter grade %s" % test_grade(average_test)

test_input(user_input)


