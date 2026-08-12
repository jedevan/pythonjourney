salary = int(input("How much is your salary: "))

if (salary >= 30000):
	year = int(input("How long is your working experience: "))
	if (year >= 2):
		print("You qualify for a loan")
	else:
		print("You must have been on your current job for at least two years to qualify.")
else:
	print("You must earn at least $30,000 per year to qualify.")

#grades

score = int(input("What is your grade: "))

if (score >= 90):
	print("Your grade is A.")
elif (score >= 80):
	print("Your grade is B.")
elif (score >= 70):
	print("Your grade is C.")
elif (score >= 60):
	print("Your grade is D.")
else:
	print("Your grade is F.")
			
