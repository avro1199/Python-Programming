x = int (input('Enter Your Age : '))

if x < 5:
	print("Underage")
elif x > 5 and x < 17:
	print("Class :", x - 5)
else:
	print("College Student")