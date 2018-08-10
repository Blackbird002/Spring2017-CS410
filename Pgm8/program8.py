#Riad Shash (Ray) 
#ID: n845y337
#Program #8
#CS 410
#Description: This program is like the program in the textbook on pages 313-315. It reads in a file of students and
# their assocaited hours and quality points and finds the student(s) with the best GPA. The version in the book only
# finds the first student with the highest gpa. The students with the same GPA would not get printed to the screen. 
# This variation of the program will print all the students with the same highest GPA to the terminal screen. 
# This program also uses a class called "Student".
# The GPA is calculated by dividing the quality points by the hours taken 

######################################################################################################################
# Class Student
######################################################################################################################
class Student:

	#Constructor
	def __init__(self, name, hours, qpoints):
		self.name = name
		self.hours = float(hours)
		self.qpoints = float(qpoints)
	
	def getName(self):
		#Retruns the name of the student
		return self.name
		
	def getHours(self):
		#Retruns the hours of the student	
		return self.hours
		
	def getQPoints(self):
		#Retruns the quality points of the student
		return self.qpoints
	
	def gpa(self):
		#Calculates the GPA of the student and returns the result
		return self.qpoints / self.hours
		
######################################################################################################################
# Function makeStudent
######################################################################################################################		
def makeStudent(infoStr):
	# infoStr is a tab-separated line: name hours qpoints
	# retuns a corresponding Student object (a instance of the class)
	name, hours, qpoints = infoStr.split("\t")
	return Student(name, hours, qpoints)
	
######################################################################################################################
# Main Function
######################################################################################################################		
def main():
	#Open the input file for reading:
	inputfilename = input("\nPlease enter the name of the student file: ")
	infile = open(inputfilename, 'r')
	
	#Set the best to the record for the first student in the file (as a list)
	best = []
	best.append(makeStudent(infile.readline()))
	
	#Process subsequent lines in the file
	for line in infile:
		nextstudent = makeStudent(line)
		#If this student's GPA is best so far, set best to this student
		if nextstudent.gpa() > best[0].gpa():
			if(len(best) > 1):
				#Clears the list of all the students with the same previous high GPA
				best = []
				best.append(nextstudent) #Adds the current found student with the highest GPA so far. 
			else:
				best[0] = nextstudent
		#If two students have the highest gpa, adds the student to the list
		elif (nextstudent.gpa() == best[0].gpa()):
			best.append(nextstudent)
			
	infile.close()
	print("\nThe student(s) with the best GPA is: ")
	#Prints all the students in the list with the same highest GPA
	for students in best:
		print(students.getName(), "with a hour count of:", students.getHours(),
		"and a GPA of:", students.gpa())
	print()
	
main()
	