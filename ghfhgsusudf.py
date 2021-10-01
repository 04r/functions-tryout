x = int(input("Hoe vaak"))

def printx(howmany=x):
	for i in range(x):
		print("Hello World!")


printx(6)

method = input("Welke methode: ")

number1 = int(input("Nummer 1: "))

number2 = int(input("Nummer 2: "))

if method == "addition":
	print(number1 + number2)
elif method == "substraction":
	print(number1 - number2)
elif method == "multiplication":
	print(number1 * number2)
elif method == "division":
	print(number1 / number2)
elif method == "increment":
	print(number1)
elif method == "decrement":
	print(number1 - number2)
else:
	print('Error')

def ask():
	aa = input("Wat is jouw naam? ")
	if aa == "stop":
		exit()
	bb = input("Hoe oud ben je? ")
	if bb == "stop":
		exit()
	cc = aa.capitalize()
	print('Hallo {}, je leeftijd is {} jaar. '.format(cc, bb))
	ask()

ask()