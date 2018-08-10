#Riad Shash (Ray) n845y337
#ID: n845y337
#Program #1
#CS 410
#Description: This program computes 10 term x1 - x10 of values that converge to find the square root of a number given by the user.
#The formula for computing the x(k+1) value using x(k) is given by:
#	x(k+1) = (x(k) + (D/x(k)))/2
#This program also checks if the user entered a digit(s), if so, they will be prompted again to enter a number

#This function does the actual calculation
def evalsquaresequence(termD):
	print("")
	if (termD == 0):
		return 0
	previous = 1
	print("The Approximate Square Root: ")
	for i in range(1,11):
		element = (previous + (termD/previous))/2
		previous = element
		print(element)
	print("")
	print("")
	return element
	
		
		
def main():
	
	while True:
		print("")
		RawInputStr = input("Enter the number to find the sequare root of: ")
		
		while RawInputStr.isdigit() == False: #Checks if the user entered a legal input
			RawInputStr = input("Enter the number to find the sequare root of: ")
		
		initialterm = int(RawInputStr)
		tenthiteration = evalsquaresequence(initialterm) #This function is called here to calculate and display the sequence
		print("After 10 iterations, the approximate square root is: ", tenthiteration)
		print("The square of this number is: ", tenthiteration **2)
		print("")
		
		RawInputStr = str(input("Do you want to enter another number? (y/n) "))
		while (RawInputStr != "y" and RawInputStr != "Y" and RawInputStr != "n" and RawInputStr != "N"):
			RawInputStr = str(input("Do you want to enter another number? (y/n) "))
			
		if(RawInputStr == "n" or RawInputStr == "N"):
			break
			
			
			

# The program starts here!		
main()