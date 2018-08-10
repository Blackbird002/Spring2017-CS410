#Riad Shash (Ray) 
#ID: n845y337
#Program #7
#CS 410
#Due: 3/24/17
"""Description: The program does two things:
        1. Converts a infix expression into a postfix expression
        2. Takes a infix expression and evaluates it
        
        A list is used as a stack to push/pop elements into using mypop() and mupush() functions. This program uses the
        Shunting-yard algorithm to convert a infix expression to postfix (invented by Edsger Dijkstra). When the user
        wants to evaluate a infix expression, the infix expression is first converted to postfix and then it is
        evaluated. This program also checks for unmatched parentheses errors, and if found, it quits the computation
        and displays the menu again. This program is menu driven and it loops continuously until a user input other
        than 1 and 2 is entered. Anything else quits the program.
        
        Left-associative operators: '-','+','*','/'
        Right-associative operators: '^'
"""
#*********************************************************************************************************************

#Global varaible list 
stack = [] #stack 

######################################################################################################################
# Checks for unmatched parentheses errors 
######################################################################################################################
def checkparentheses(input):
    count = 0
    for token in input:
        if(token == ')' or token == '('):
            count = count + 1
    
    #If the parenthesis count is even, that means that it is balanced
    if(count % 2 == 0):
        return True
    else:
        return False


######################################################################################################################
# Remove Spaces Function 
######################################################################################################################
def removespaces(input):
    nospaces = input.strip() #Gets rid of the spaces before and after the string
    return nospaces
    
######################################################################################################################
# Clears the "stack"
###################################################################################################################### 
def clearstack():
    del stack[:]

######################################################################################################################
# Pushes an item into the "stack"
######################################################################################################################
def mypush(item):
    stack.append(item)
    
######################################################################################################################
# Pops an item into the "stack:
######################################################################################################################
def mypop():
    #Checks to see if the stack is empty
    if(len(stack) != 0):
        return stack.pop()
    else:
        return None
        
######################################################################################################################
# Returns the top element of the "stack"
######################################################################################################################
def topelement():
    if(len(stack) != 0):
        top = stack[len(stack)-1]
        return top #Returns the top element
    else:
        #If the stack is empty 
        return None

######################################################################################################################
# Returns the precedence value 
######################################################################################################################
def getprecedence(operator):
    precedence       = {} # high value means high precedence
    precedence["^"]  = 3 
    precedence["+"]  = 1
    precedence["-"]  = 1
    precedence["*"]  = 2
    precedence["/"]  = 2
    precedence["%"]  = 3
    precedence["("]  = 4
    precedence[")"]  = 4
    return precedence[operator] #Returns the precedence value
    
######################################################################################################################
# Determines if a token is a math operator 
######################################################################################################################
def isoperator(input):
    if (input == '-' or input == '+' or input == '*' or input == '/' or input == '%' or input == '^'):
        return True
    else:
        return False
 
######################################################################################################################
# Does the appropriate math operation with two input numbers
###################################################################################################################### 
def evalmath(operator,num1,num2):
    if(operator == '+'):
        return num1 + num2
    elif(operator == '-'):
        return num1 - num2
    elif(operator == '*'):
        return num1 * num2
    elif(operator == '/'):
        return num1 / num2
    elif(operator == '%'):
        return num1 % num2
    else: #if the operator is a '^'
        return num1 ** num2 #The result is returned
    
######################################################################################################################
# Infix to postfix function 
######################################################################################################################
def infixtopostfix(inputstr):
    leftassociative = ['-','+','*','/'] #Left-associative operators
    rightassociative = ['^']            #Right-associative operators
    output = "" #Postfix output set to empty
    for token in inputstr:
        
        #If there is some whitespace 
        if not token.split():
            continue
            
        #if the token is a number
        if (ord(token) >= 48 and ord(token) <= 57):
            #add it to the end of the postfix output
            output = output + str(token) #No space is added in between (so numbers like 12 are not 1 2)
        else: # operators
        
            if (token == '('):
                #Push onto the stack
                mypush(token)
            elif(token == ')'):
                topofstack = mypop() #We get rid of the '('
                while (topofstack != '('):
                    output = output + " " + str(topofstack)
                    topofstack = mypop()
            else: # math operators
            
                topofstackcheck = topelement() #Gets the top token in the stack
                
                #While there is an operator token topofstackcheck at the top of the stack:
                while(topofstackcheck != '(' and topofstackcheck):
                    #If token is left-associative and its precedence is less than or equal to that of the one on top of the stack
                    # or 
                    #If token is right-associative and has precedence less than the one on top of the stack 
                    #(For the '^' operator)
                    if(((token in leftassociative) and getprecedence(token) <= getprecedence(topofstackcheck)) or
                    (token in rightassociative and getprecedence(token) < getprecedence(topofstackcheck))):
                        #token is popped off the stack and appended to output
                        topofstack = mypop()
                        output = output + " " + topofstack
                    else:
                        break
                    
                    topofstackcheck = topelement()
                #Pushes the token to the stack after the iteration
                mypush(token)
                output = output + " "
    
    #After the for loop, after we went through all the tokens in the inputstr string (There are stil tokens in stack)
    topofstackcheck = topelement()
    while(topofstackcheck):
        #Pop the operator into the output 
        topofstack = mypop()
        output = output + " " + topofstack
        topofstackcheck = topelement()
    return output
    
######################################################################################################################
# Evaluate infix expression
######################################################################################################################
def evaluateinfix(inputstr):
    clearstack()
    output = "" #makes the output string
    postfixstr = infixtopostfix(inputstr)
    print(postfixstr)
    postfix = postfixstr.split()
    
    for token in postfix:
        #If the token is number
        if(isoperator(token) == False and token != '(' and token != ')'):
            mypush(int(token))
        #else if the token is a operator
        elif(isoperator(token) == True and len(stack) != 1):
            num2 = mypop()
            num1 = mypop()
            result = evalmath(token,num1,num2)
            mypush(result)
        #else if the first number is a negative number (specific)
        elif(token == '-' and len(stack) == 1):
            num1 = mypop()
            result = num1 * -1
            mypush(result)
    
    output = mypop() #The solution is the only thing in the stack
    return output   #The solution!

######################################################################################################################
# Main Function
######################################################################################################################
def main():
    #Introduction:
    print("\nThis program converts infix arithmatic expressions to postfix expressions.")
    print("It also evaluates infix expressions.")
    
    #Menu:
    print("\nPlease choose the operation: ")
    print("1. Convert an infix expression to its equivalent postfix expression form")
    print("2. Evaluate a infix expression")
    print("3. Quit the program!")
    strchoice = input("\nChoice: ") #Gets the choice from the user
    
    while (strchoice == "1" or strchoice == "2"):
        if(strchoice == "1"):
            infixstr = input("Please enter a infix arithmatic expression to convert to postfix: ")
            infixstr = removespaces(infixstr)
            if(checkparentheses(infixstr) == True): #Checks if the parentheses are balanced
                #Call the infix to postfix function:
                print("\nThe postfix expression is: " ,infixtopostfix(infixstr))
            else:
                print("\nError! Unmatched parenthses. Please try again.")
        elif(strchoice == "2"):
            infixstr = input("Please enter a infix arithmatic expression to evaluate: ")
            infixstr = removespaces(infixstr)
            if(checkparentheses(infixstr) == True): #Checks if the parentheses are balanced
                #Call the infix eval function:
                print("\nResult is: ", evaluateinfix(infixstr))
            else:
                print("\nError! Unmatched parenthses. Please try again.")
        
        #Menu:
        print("\nPlease choose the operation: ")
        print("1. Convert an infix expression to its equivalent postfix expression form")
        print("2. Evaluate a infix expression")
        print("3. Quit the program!")
        strchoice = input("\nChoice: ") #Gets the choice from the user
    
    #End of program
main()