#Receives check amount
check = float(raw_input("Please input check amount: "))

#Receives tip amount
tip_percentage = float(raw_input("Please input desired tip percentage: "))

#Changes tip to decimal
tip = tip_percentage * .01

#Multiplies tip with check amount
amount_to_tip = tip * check

#Adds tip amount to check amount
check_with_tip = amount_to_tip + check


#Receives number of people in party
party = int(raw_input("Please input how many people in party: "))


#Calculates total amount
amount_to_pay = check_with_tip / party

print '''
So your check was %r.
You have decided to tip %r %%.
You have %r in your party.
Your amount you have to pay is %.2f.
''' % (check, tip_percentage, party, amount_to_pay)