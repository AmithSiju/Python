print("1. Addition \n2. Subtraction \n3. Multiplicaton \n4. Division ")
n = int(input("Choose your operation : "))
a = int(input("Number 1: "))
b = int(input("Number 2: "))

if n == 1:
	print("Sum = ",a + b)
elif n == 2:
	print("Diff = ",a - b)
elif n == 3:
	print("Product = ",a * b)
elif n == 4:
	print("Quotient = ",a / b)
	print("Reminder = ",a%b)
else:
	print("Invalid input!")