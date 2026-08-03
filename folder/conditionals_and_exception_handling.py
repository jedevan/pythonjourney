try:
	salary = int(input("Please provide your annual salary: "))
	
	
	if (salary >= 30000):
		years_worked = int(input("Please provide years on the job: "))
		if years_worked >= 2:
			print("You are qualified to avail of the highest loan.")
		else:
			print("You must be employed for at least 2 years to avail of the loan.")
	if ((salary >= 15000) and (salary <= 29000)):
		if (years_worked >= 2):
			print("You are qualified to avail of the lower-range loan.")
		else:
			print("You must be employed for at least 2 years to avail of the loan")
	else:
		print("You must earn at least Php 30,000.00 to avail of the loan.")


	score =  int(input("Please give your score value: "))

except ValueError:
	print("That is an invalid input.")

	if (score >= 90):
		if (score >= 96) and (score <= 100):
			print('Your grade is A+.')
		elif (score >= 92) and (score <= 95):
			print('your grade is A.')
		else: 	
			print('Your grade is A-.')
	elif (score >= 80):
		if (score >= 86) and (score <= 89):
			print('Your grade is B+.')
		elif (score >= 82) and (score <= 85):
			print('Your grade is B.')
		else:
			print('Your grade is B-.')
	elif (score >= 70):
		if (score >= 76) and (score <= 79):
			print('Your grade is C+.')
		elif (score >= 72) and (score <= 75):
			print('Your grade is C.')
		else:
			print('Your grade is C-.')
	elif (score >= 60):
		if (score >= 66) and (score <= 69):
			print('Your grade is D+.')
		elif (score >= 62) and (score <= 65):
			print('Your grade is D.')
		else:
			print('Your grade is D-.')
	else:
		print('Your grade is F.')
