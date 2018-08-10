#Riad Shash (Ray) n845y337
#ID: n845y337
#Program #1a
#CS 410
#Description: This program is part A of assignment #2. It calcules the interest accured on an account using nominal rate and the number of
#compounding periods. When run, the program prompts the user for the principal, the yearly rate, and finally the compounded times per year.
#The program then displays the future value in the account. 

def main():
	print()
	print("This program calculates the future value given the nominal rate and the number of compounding periods.")

	#Asks the user for the principal amount
	while True:
		print()
		InitialPrincipal = input("Please enter the initial principal: ")
		#If it can't convert to a float, it asks the user for input again.
		try:
			InitialPrincipal = float(InitialPrincipal)
			break
		except ValueError:
			print("Error! Please try again!")
			
	#Asks the user for the yearly rate (rate)
	while True:
		print()
		Rate = input("Please enter the yearly rate as a decimal (ex: 3% = 0.03): ") #Has to be a decimal
		#If it can't convert to a float, it asks the user for input again.
		try:
			Rate = float(Rate)
			break
		except ValueError:
			print("Error! Please try again!")
			
	#Asks the user for the compound times (periods)
	while True:
		print()
		CompoundTimes = input("Please enter the number of times interest is compounded each year: ")
		#If it can't convert to a integer, it asks the user for input again.
		try:
			CompoundTimes = int(CompoundTimes)
			break
		except ValueError:
			print("Error! Please try again! Please input a integer.")
			
	FuturePrincipal = CalculateFutureValue(InitialPrincipal,CompoundTimes,Rate)
	print()
	#The future value is formatted to two decimal places 
	print("The value in 10 years using a rate of" ,Rate, "and a period of", CompoundTimes, "times each year is: $" + "{:.2f}".format(FuturePrincipal))
	print()
			

#This function calculates the furure value given the parameters: initial principal, the period, and the rate
#It retruns the future value
def CalculateFutureValue(principal, period, rate):
	for i in range(10 * period):
		principal = principal * (1 + (rate / period))
	
	return principal

#The program runs here:	
main()