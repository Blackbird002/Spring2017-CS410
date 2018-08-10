#Riad Shash (Ray) 
#ID: n845y337
#Program #9
#CS 410
#4/9/2017
"""Description: It reads in a file of students and their assocaited hours and quality points and calculates the 
   GPA of every created student. This program is a slight modification of the program located on pages 354-355.
   As problem 11.9 states, a disadvantage of the original program is that the sort() function has to call the
   gpa() method repeatedly, slowing the sort down. This problem uses an alternative way of sorting the student
   objects by creating a decorated list of the student's GPA and then the actual student object itself. A list
   of tuples is created: [(gpa1, Student1), (gpa2, Student2), ...]. The sort function is then given a anonymous
   function that tells it to only look at the first term in each tuple for sorting to make sure that the program
   works if two or more students have the same gpa since the sort() python method will look at the second term 
   in the tuple if no key is specified. As the program in chapter 11, this program reads in a file and then
   it creates a file with the sorted students from the highest GPA to the lowest. 
"""

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
# Function readStudents
######################################################################################################################	   
def readStudents(filename):
    #reads in line, one at a time and creates the list of tuples of the students GPA and the student object
    infile = open(filename, 'r')
    students = []
    for line in infile:
        student = makeStudent(line) #creates a student object
        students.append((student.gpa(), student)) #creates the "decorated" list for sorting (tuples)
    infile.close()
    return students #returns a decorated list where each element in the list is: (GPA, the student object)- a tuple

######################################################################################################################
# Function writeStudents
######################################################################################################################	
def writeStudents(students, filename):
    outfile = open(filename, 'w')
    for s in students:
        print("{0}\t{1}\t{2}".format(s[1].getName(), s[1].getHours(), s[1].getQPoints()), file = outfile)
    outfile.close()
    
######################################################################################################################
# Main Function
######################################################################################################################
def main():
    print("\nThis program sorts a file of students according to their GPA.")
    filename = input("\nPlease enter the name of the input data file: ")
    data = readStudents(filename)
    
    #A anonymous function is passed in. The sort function looks at the function handle only.
    #Only looks at the first element in each tuple
    data.sort(key = lambda x: x[0], reverse = True) #This sorts the "decorated" list of student objects
    
    filename = input("\nPlease enter the name of the output file: ")
    writeStudents(data, filename)
    print("\nThe data has been written to:", filename)
    #End of program
    
main()
    
    
    
