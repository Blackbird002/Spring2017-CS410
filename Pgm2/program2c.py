#Riad Shash (Ray) n845y337
#ID: n845y337
#Program #2c
#CS 410
#Description: This program part C for assignment #2. This program approximates the value of the square root of a number. 
#It uses the guess and check approach using Newton's method: guess = (guess + (x/guess))/2, where "x" is the value we want the 
#root of, and "guess" is the current guessed number. Instead of asking the user for the number of times the loop should be executed, the 
#exit condition for the loop is when the absolute value of the difference between the number and the guess is less than 0.000001. The program
#asks for the user to input a number to find the square root of. 

import math #The math library is imported to get the actual square root of the number (Used when comparing)

def main():
	#Makes sure the user enters a legal float or int number. If not, the user is prompted again.
	while True:
		print()
		InputNumber = input("Please enter a number to find the approximate square root of: ")
		try:
			InputNumber = float(InputNumber)
			break
		except ValueError:
			print("Error! Please try again!")
			
	guess = InputNumber / 2 #Initial value of guess
	print()
	
	#The exit condition for the loop is when the absolute value of the difference between the number and the guess is less than 0.000001.
	while (abs(InputNumber - (guess**2)) >= 0.000001):
		guess = (guess + (InputNumber/guess))/2
		
	print("The approximate value of the square root of ",InputNumber, "is :", guess)
	print()
	print("The difference between  math.sqrt(x) and the calculated approximate")
	print("square root of ", InputNumber, "is :", math.sqrt(InputNumber) - guess)
	print()

#Program starts here	
main()