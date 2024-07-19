yr = int(input("Enter the final year: "))
current = int(input("Enter the current year: "))
if yr <= current:
	print("Invalid")
else:
	# Next leap year is 2024
	n = current%4
	print("The leap years are: ")
	for i in range(current + (4-n), yr, 4):
		print(i)