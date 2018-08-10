#Riad Shash (Ray) 
#ID: n845y337
#Program #5
#CS 410
#Description: This program produces a monthly amortization table showing the details of how the loan is paid off 
# over the duration of the loan. It also computes how much money is paid as interest over the lifetime of the
# loan. Each line displays:
#		1. The month number (payment number) of the laon
#		2. The contant payment.
#		3. The amount of monthly payment which is used to reduce the loan.
#		4. The amount of monthly payment which is paid as interest on the current loan balance.
#		5. The new balance of the loan which remains to be paid ater the payment has been made.

# This program also does error checking. It will prompt the user to re-enter the data if an error occurs. 

######################################################################################################################
# The main function
######################################################################################################################
def main():

	#Values declared here to keep track of the variables.
	Principal = 0.0
	Interestrate = 0.0
	YearLength = 0
	TotalMonths = 0
	LoanBalance = 0.0
	CurrentMonthlyInt = 0.0
	MonthlyPrincipalRed = 0.0
	MonthlyRate = 0.0
	MonthlyPayment = 0
	TotalInterestPaid = 0
	
	#Gets the principal
	while True:
		print()
		principalstr = input("\nPlease enter the principal amount of the loan: ")
		try:
			Principal = float(principalstr)
			if(Principal > 0):
				break;
			else:
				print("The principal must be a positive, non-zero value!")
		except ValueError: #Can't convert to a float!
			print("Error! Please check your input!")
	
	#Gets the interest rate 
	while True:
		print()
		interestratestr = input("Please enter the interest rate (as a percent): ")
		try:
			Interestrate = float(interestratestr)
			break;
		except ValueError: #Can't convert to a float!
			print("Error! Please check your input!")
			
	#Gets the length (in years)
	while True:
		print()
		yearlengthstr = input("Please enter the length (in years) of the loan: ")
		try:
			YearLength = int(yearlengthstr)
			break;
		except ValueError: #Can't convert to int!
			print("Error! Please check yuor input!")
			
	LoanBalance = Principal
	TotalMonths = CalcTotalMonths(YearLength) # Calculates the total months 
	MonthlyRate = CalcMonthlyRate(Interestrate) # Calculates the monthly rate
	MonthlyPayment = CalcMonthlyPayment(Principal,MonthlyRate,TotalMonths)
	
	#Formats the statements just before the table
	print("\nThe Schedule for a ${0:0.2f} loan at {1:0.2f}% annual".format(Principal,Interestrate))
	print("interest rate to be paid back over {0} years:\n".format(YearLength))
	print("{0:>5} {1:>15} {2:>15} {3:>15} {4:>15}".format("Month","Payment","Reduction","Interest","Loan Balance"))
	
	print("-" * 69) #Prints a line with 69 "-" characters for the table (top part)
	#Loops the total number on months:
	for i in range(1,(TotalMonths+1)):
		CurrentMonthlyInt = CalcMonthlyInterest(LoanBalance,MonthlyRate) # Calculates the monthly interest
		MonthlyPrincipalRed = CalcMonthlyPrincipalReduction(MonthlyPayment,CurrentMonthlyInt) # Calculates the monthly principal reduction
		LoanBalance = CalcNewBalance(LoanBalance,MonthlyPrincipalRed) # Calculates the new balance
		TotalInterestPaid = TotalInterestPaid + CurrentMonthlyInt #Calculates the total interest paid
		#Makes sure that the last Loan Balance is 0. (Due to rounding issues)
		if(i == TotalMonths):
			LoanBalance = 0.00
		#5 spaces for the month #, 15 spaces for MonthyPayment, 15 spaces for MonthlyPrincipalRed, 15 spaces for CurrentMonthlyInt
		# 15 spaces for LoanBalance. The last 4 variables are rounded to the 2nd decimal point
		print("{0:5} {1:15.2f} {2:15.2f} {3:15.2f} {4:15.2f}".format(i,MonthlyPayment,MonthlyPrincipalRed,CurrentMonthlyInt,LoanBalance))	
	print("-" * 69) #Prints a line with 69 "-" characters for the table (bottom part)
	print("\nThe total interest paid on the loan is: ${0:0.2f}".format(TotalInterestPaid))
			
######################################################################################################################
# Calculates the monthly rate
######################################################################################################################
def CalcMonthlyRate(AnnualInterestRate):
	return (AnnualInterestRate * 0.01) / 12

######################################################################################################################
# Calculates the total months 
######################################################################################################################
def CalcTotalMonths(LengthOfLoan):
	return LengthOfLoan * 12


######################################################################################################################
# Calculates the monthly payment
######################################################################################################################
def CalcMonthlyPayment(Principal,MonthlyRate,TotalMonths):
	return Principal * ((MonthlyRate) / (1 - (1 + MonthlyRate) ** (-1 * TotalMonths)))


######################################################################################################################
# Calculates the monthly interest
######################################################################################################################
def CalcMonthlyInterest(CurrantLoanBalance, MonthlyInterestRate):
	return CurrantLoanBalance * MonthlyInterestRate


######################################################################################################################
# Calculates the monthly principal reduction
###################################################################################################################### 
def CalcMonthlyPrincipalReduction(MonthlyPayment, MonthlyInterest):
	return MonthlyPayment - MonthlyInterest


######################################################################################################################
# Calculates the new balance
######################################################################################################################
def CalcNewBalance(Principal, MonthlyPrincipalReduction):
	return Principal - MonthlyPrincipalReduction
	
main()
	
	
	