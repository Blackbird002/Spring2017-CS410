#Riad Shash (Ray) n845y337
#ID: n845y337
#Program #4
#CS 410
#Description: This program does the same thing that the wc command does in UNIX
#or LINUX. Instead of taking a file as an argument, it asks the user for the 
#name of the file. The file has to be located in the same directory. If the
#file is not found, the user is prompted again for the name of the file. The
#main function gets the file name and if found, passes it along to the analyze
#function along with the file name. Then the program displays the name of the
#file, the number of lines,words and characters in the file and ends.

################################################################################
# The main function
################################################################################
def main():
	#Displays an introduction to the user...
	print()
	print("This program analyzes a text file and states the number of")
	print("lines, words and characters in the text file.")
	print("It behaves like the wc command in UNIX/LINUX.")
	print()
	
	#If the file is found, it breaks out of the loop. 
	while True:
		print()
		filename = input("Please enter the name of the file: ")
		
		try:
			infile = open(filename,"r")
			break;
		except FileNotFoundError: #File not found error
			print("Error! The file with the name: ",filename, " was not found!")
			print("Please try again!")
	print("File found!")
	print()
	analyzefile(infile, filename) #Runs the function that counts the lines,words
									#and characters
	infile.close(); #Closes the file when done
	
################################################################################
# The file analyze function
# 	Takes two parameters: file, filename
#		-file is the actual file that was found
# 		-filename is the name of the file
################################################################################
def analyzefile(file, filename):
	#initializes the lines,words, and characters to 0
	numoflines = 0
	numofwords = 0
	numofcharacters = 0
	words = [] #this array is used to store the words found in a line\
	#for each line in the file.... do:
	for line in file:
		numoflines+= 1 #Line counter gets incremented 
		strline = line #The line gets converted to a string
		words = strline.split() #the words gets stored in the words[] array
		numofwords += len(words) #The word count per line is calculated here
		#for each character in a line... do:
		for characters in strline:
			numofcharacters+= 1 
	
	#The results get printed for the user to see.
	print("Selected file: ",filename) 
	print("The number of lines in the file: ",numoflines)
	print("The number of words in the file: ",numofwords)
	print("The number of characters in the file: ",numofcharacters)
	print()

#The program runs here!
main()