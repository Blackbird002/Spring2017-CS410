#Riad Shash (Ray) n845y337
#ID: n845y337
#Program #2b
#CS 410
#Description: This program is for part B for homework #2. It approximates the value of pi by summing the terms of the series:
# ((4/1) - (4/3)) + ((4/5) - (4/7)) + ((4/9) - (4/11)) + ... Instead of prompting the user when to stop, the loop stops when
#the difference between the new (Sk) and previous (Sk-1) term is less than 0.0001

import math #The math library is imported to get the pi constant so then the approximated pi value can be subtracted from the actual 

def main():
	print()
	print("This program approximates the value of pi.")
	denominator1 = 1 #Initial Value
	denominator2 = 3 #Initial Value
	NewTerm = (4/denominator1) - (4/denominator2) #The 1st term is calculated here.
	PreviousSum = 0 
	Approxpi = NewTerm #The first Sk term 
	
	while ((abs(Approxpi - PreviousSum) >= 0.0001)): #The loop stops if the difference is less than 0.0001
		PreviousSum = Approxpi #the previous Sk-1 term gets stored here
		
		denominator1 += 4 #adds 4 to the 1st denominator
		denominator2 += 4 #adds 4 to the 2nd denominator
		NewTerm = (4/denominator1) - (4/denominator2) #this is the "new" term
		Approxpi += NewTerm #new term is added (Sk term)
		
	print("The approximate calculated value of pi is: ",Approxpi)
	print("The difference between  math.pi and the calculated approximation is: ", math.pi - Approxpi)
	print()

main()