#Riad Shash (Ray) 
#ID: n845y337
#Program #6
#CS 410
#Description:This program encode/decodes zipcodes/barcodes that it reads from a user specified file.
#The user has two choices when the program starts: either encode a zip code(s) or decode bar code(s)
#When saving to a file, this program puts a zip code/bar code on each line. (1 per line)
#This program also expects that each zip code/bar code is on each line too (1 per line) in the given file
#File has to be in the current director too.

######################################################################################################################
# The main function
######################################################################################################################
def main():
	print("This program encodes and decodes barcodes. Please choose the desired option: ")
	choice = input("\nDo you want to encode(e) or decode(d)?")
	if(choice == "e" or choice == "E"):
		print("You chose to encode!")
		infilename = input("\nPlease enter the name of the file to encode: ")
		infile = open(infilename,'r')
		
		outfilename = input("\nPlease enter the name of the output file: ")
		outfile = open(outfilename,'w')
		
		#Calls the encode function with the files as input parameters:
		encode(infile, outfile)
	elif(choice == "d" or choice == "D"):
		print("You chose to decode!")
		infilename = input("\nPlease enter the name of the file to dencode: ")
		infile = open(infilename,'r')
		
		outfilename = input("\nPlease enter the name of the output file: ")
		outfile = open(outfilename,'w')
		
		#Calls the decode function with the files as input parameters:
		decode(infile,outfile)
	
	#Closes the files
	infile.close()
	outfile.close()

######################################################################################################################
# The encode function
######################################################################################################################	
def encode(infile,outfile):
	#The accociated barcode is given by entering the position in the list using []
	numbercodes = ["!!...", "...!!", "..!.!", "..!!.", ".!..!", ".!.!.", ".!!..", "!...!", "!..!.", "!.!.."]
	for line in infile:
		zipstr = line
		barcode = "!"
		checksum = 0
		remain = 0
		fix = 0
		for characters in zipstr:
			if(characters != "\n" and characters != "-" and characters != "+" and characters != ""):
				checksum = checksum + eval(characters)
				barcode = barcode + numbercodes[eval(characters)]
		#modulus 10 is used to get the remaineder, that is then subtracted from 10 and added as a "checksum"
		remain = checksum % 10
		fix = 10 - remain
		barcode = barcode + numbercodes[fix]
		barcode = barcode + "!"
		print(barcode, file=outfile)
		
######################################################################################################################
# The decode function
######################################################################################################################		
def decode(infile,outfile):
	numbercodes = ["!!...", "...!!", "..!.!", "..!!.", ".!..!", ".!.!.", ".!!..", "!...!", "!..!.", "!.!.."]
	convertedbar = ""
	for line in infile:
		barstr = line
		lengthofbarcode = len(barstr)
		#The program determines what zip-code to decode based on the length:
		#******************************************************************************************************
		#For the typical zip code with only numbers
		if(lengthofbarcode == 33):
			barstr = barstr[1:31]
			barstr = barstr[:25]
			#converts the 5 numbers
			for i in range(5):
					convert = barstr[0:5]
					barstr = barstr[5:]
					#Gets the index of the found barcode:
					number = numbercodes.index(convert)
					numberstr = str(number)
					convertedbar = convertedbar + numberstr
			print(convertedbar, file=outfile)
			convertedbar = "" #Resets this string so another zip-code can be decoded
		#******************************************************************************************************
		#For the 2nd kind of zip code with the "-" sign
		elif(lengthofbarcode == 53):
			barstr = barstr[1:51]
			barstr = barstr[:45]
			#converts the 5 numbers
			for i in range(5):
				convert = barstr[0:5]
				barstr = barstr[5:]
				#Gets the index of the found barcode:
				number = numbercodes.index(convert)
				numberstr = str(number)
				convertedbar = convertedbar + numberstr
			convertedbar = convertedbar + "-"
			#converts the 4 numbers
			for i in range(4):
				convert = barstr[0:5]
				barstr = barstr[5:]
				#Gets the index of the found barcode:
				number = numbercodes.index(convert)
				numberstr = str(number)
				convertedbar = convertedbar + numberstr	
			print(convertedbar, file=outfile)
			convertedbar = "" #Resets this string so another zip-code can be decoded
		#******************************************************************************************************
		#For the 3rd kind of zip code with the "+" sign
		elif(lengthofbarcode == 63):
			barstr = barstr[1:61]
			barstr = barstr[:55]
			#converts the 5 numbers
			for i in range(5):
				convert = barstr[0:5]
				barstr = barstr[5:]
				#Gets the index of the found barcode:
				number = numbercodes.index(convert)
				numberstr = str(number)
				convertedbar = convertedbar + numberstr
			convertedbar = convertedbar + "-"
			#converts the 4 numbers
			for i in range(4):
				convert = barstr[0:5]
				barstr = barstr[5:]
				#Gets the index of the found barcode:
				number = numbercodes.index(convert)
				numberstr = str(number)
				convertedbar = convertedbar + numberstr	
			convertedbar = convertedbar + "+"
			#converts the 2 numbers
			for i in range(2):
				convert = barstr[0:5]
				barstr = barstr[5:]
				#Gets the index of the found barcode:
				number = numbercodes.index(convert)
				numberstr = str(number)
				convertedbar = convertedbar + numberstr
			print(convertedbar, file=outfile)
			convertedbar = "" #Resets this string so another zip-code can be decoded
#The program starts here:		
main()
		
