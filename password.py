import string
import random
pass_word = int(input("Enter password length: "))

print('''enter how many characters you want in your password :1. Digits 2. Letters 3. Special characters''')
passList = ""
while(True):
	choice = int(input("Pick a number "))
	if(choice == 1):
		passList += string.ascii_letters
	elif(choice == 2):
		passList += string.digits
	elif(choice == 3):
		passList += string.punctuation
		break
	else:
		print("Please pick a valid option!")

password = []

for i in range(pass_word):
	randomchar = random.choice(passList)
	password.append(randomchar)
print("The random password generated is " + "".join(password))
