#Riad Shash (Ray) n845y337
#ID: n845y337
#Program #3
#CS 410
#Description: This program encodes a user defined message and shits each character
#along the alphabet using a user defined key that contains a number that indicates
#how many shifts to shift each character in the message. Only the characters a-z and
#characters A-Z get encoded. Numbers and other special characters other than the ones
#stated previously do not get encoded. They just stay the same in the encoded message.

################################################################################
# The main function
################################################################################
def main():
	encodedmessage = ""
	alphabet = str("abcdefghijklmnopqrstuvwxyz") #the lowercase characters in a string
	ALPHABET = str("ABCDEFGHIJKLMNOPQRSTUVWXYZ") #the uppercase characters in a string
	print()
	print("This program encodes a message that you type in using a provided key!")
	
	#Asks the user for the key (This should be a integer)
	while True:
		print()
		key = input("Please enter the key (the number of shifts): ")
		#If the it can't convert to a int, asks for the key again
		try:
			key = int(key)
			break
		except ValueError:
			print("Error, the key needs to be a integer, please try again.")
	
	
	#Asks the user for the message to encode
	message = str(input("Please type in the message you want to encode: "))
	
	#The for loops goes through the entire message string 
	for i in range(len(message)):
		#If the character is lowercase....
		if(ord(message[i]) >= 97 and ord(message[i]) <= 122):
			position = key + ord(message[i]) #Adds the key to the position
			position -= 19 	#This is the offset for the lowercase numbers
			if(position > 26):
				position = position % 26
			encodedmessage+= alphabet[position]
		#If the character is Uppercase....
		elif(ord(message[i]) >= 65 and ord(message[i]) <= 90):
			position = key + ord(message[i]) #Adds the key to the position
			position -= 13		#This is the offset for the Uppercase numbers
			if(position > 26):
				position = position % 26
			encodedmessage+= ALPHABET[position]
		#if the character is anything else like a number or special character 
		else:
			encodedmessage+= message[i]
	
	print()
	print("The encoded message is:", encodedmessage)		
	print()
	
#Program runs here!		
main()