#This is a Test Average Calculator

test_grades = 0.0
num_of_tests = 0

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

while test_grades != "x":
	test_input = float(raw_input("Please input test grade(s): "))
	try:
		num_of_tests += 1
		test_grades += test_input
	except ValueError:
		break

average_test = test_grades / num_of_tests
print "Your test average is %.2f %%" % average_test
print "Your test average letter grade is %s" % test_grade(average_test)