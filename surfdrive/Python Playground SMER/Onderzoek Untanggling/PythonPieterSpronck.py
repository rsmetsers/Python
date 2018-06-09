# --------- ABUTMENT ------------- #


### (abst) datatypes int



#A11
# All datatypes: For each of the following indicate its type: 4, 0.5, False, "Hello", 'c'
# ANSWER: int, float/double, Boolean, String, Char


#A14
#Int: What is the result of 4+5? ANSWER: 9
#String: What is the result of "4"+"5"? ANSWER: 45
#String: What is the result of 3*"4"? ANSWER: 444


#Misconception: Strings are mutable
#What does the following code print?
s = 'Humpty Dumpty sat on the wall'
print( s.replace( ' sat on ' , ' fell off ' ) )
print( s )
#ANSWER: 'Humpty Dumpty fell off the wall'
# 'Humpty Dumpty sat on the wall'
#source:  De programmeursleerling, Pieter Spronck


### VARIABLES
### variables	declaration
### variables assignment (and initialization)


#A21
#What does the following statement do?
#JAVA: int a
#ANSWER: initialize an integer variable with the name a

#A22
#What does the following statement do?
#JAVA: int a;
#       String b;
#ANSWER: initialize a integer variable with the name a and a String variable with the name b



#A21
#A22
#What does the following statement do?
#JAVA: int a = 4;
a=4
#ANSWER: initialize an integer variable with the name a and assign it the value 4


#A23
#two declarations following each other
#What does the following code do?
# JAVA: int a = 5;
#     int b = 6;
a = 5
b = 6
#ANSWER: initialize an integer variable with the name a and assign it the value 5 and an integer variable with the name b with the value 6

#A23
#declaration followed by an assignment of the same variable
# What does the following code do?
# JAVA:
# int a = 5;
# a = 7;
a=5
a=7



# #A23 (TOO DEEP??)
# #decl, decl, assignment
# int a = 5; int b = 6; a = 7;
# #A23
# #decl, decl, ass, ass
# int a = 5; int b = 7; a = 8; b = 9


#A10 (could also belong to methods:print or datatypes)
#Goal: understands the difference between string and a variable.
#What does the following piece of code output?
name = "John Doe"
print( "name" )
#Answer: name
#source:  De programmeursleerling, Pieter Spronck






### OPERATORS
### arithmetic operators	"+"

#A41
# Goal: understands how the + operator works on integers
a = 1
b = 4
print( a + b )
#source:  De programmeursleerling, Pieter Spronck


#A34
#Goal: understands how the + operator works in combo with assignment
#What is the value of c?
a = 17
b = 23
c = a + b
#source:  De programmeursleerling, Pieter Spronck

#A34
#Goal: understands how the += operator works
#What is the value of a?
a = 17
b = 23
a += b
#source:  De programmeursleerling, Pieter Spronck

#Strings:
#A14
#goal: understands how the + operator works on strings
c = "1"
d = "4"
print( c + d )
#source:  De programmeursleerling, Pieter Spronck

#A33
#misconception: a=b vs. b=a
#misconception: variable can take on multiple values
# What are the values of a and b after execution?
a = 1
b = 2
a = b
#ANSWER: a is 2 (not multiple values: 1 and 2) and b is 2 (not inverted assignment: 1)
#source:  De programmeursleerling, Pieter Spronck

#A33
#misconception: changing b also changes value of a
# What are the values of a and b after execution?
a = 1
b = a
b = 3
#source:  De programmeursleerling, Pieter Spronck


#A34
#Goal: understands assignment in combo with arithmetic operation +
#What is the value of nr_of_bananas after the following statement:
nr_of_bananas = 100
nr_of_bananas = nr_of_bananas + 1
print( nr_of_bananas )
#source:  De programmeursleerling, Pieter Spronck

#A34
#Goal: understands assignment in combo with shorthand arithmetic operation +=
#What is the value of nr_of_bananas after the following statement:
nr_of_bananas = 100
nr_of_bananas += 1
print( nr_of_bananas )
#source:  De programmeursleerling, Pieter Spronck

#A34
#Goal: understands execution flow of assignements and arithmetic operations.
# source: http://www.pd4cs.org/4-execution-flow-with-variables/
#What are the values of x, y, and z after executing the following code?
x = 7
y = 2
z = x - y
y = x - 6
y = y + 1
#source:  De programmeursleerling, Pieter Spronck

#A34
#Goal: understands the assignment of a variable
# "misconception: values of b and a both changed
# [source: http://www.pd4cs.org/4-execution-flow-with-variables/]"
# What are the values of a and b after executing the following code?
a = 3
b = 2
a = b + 1
# ANSWER: a is 3 and b is 2
#source:  De programmeursleerling, Pieter Spronck

#A34
#GOAL:
# "misconception: assignment statements are stored as a formula rather than as a value
# [http://www.pd4cs.org/variables-misconception-assignment-statements-like-a-b-1-are-stored-as-a-formula-rather-than-as-a-value-2/]"
# What are the values of a and b after executing the following code?
b = 5
a = b + 1
b = 7
# ANSWER: a is 6 (not 8) and b is 7
#source:  De programmeursleerling, Pieter Spronck


### relational operators	"=="

#A51
#Goal: understands relational operations in relation to the given datatype
#What is printed in the console after execution of each of these statements?
print( "1.", 2 < 5 )
print( "2.", 2 <= 5 )
print( "3.", 3 > 3 )
print( "4.", 3 >= 3 )
print( "5.", 3 == 3.0 )
print( "6.", 3 == "3" )
print( "7.", "syntax" == "syntax" )
print( "8.", "syntax" == "semantics" )
print( "9.", "syntax" == " syntax" )
print( "10.", "Python" != "rubbish" )
print( "11.", "Python" > "Perl" )
print( "12.", "banana" < "orange" )
print( "13.", "banana" < "Orange" )
#source:  De programmeursleerling, Pieter Spronck



### BOOLEAN OPERATORS
#A4a0
#For the code below, determine whether this will evaluate to True or False.
t = True
f = False
print( t and t )
print( t and f )
print( f and t )
print( f and f )
print( t or t )
print( t or f )
print( f or t )
print( f or f )
print( not t )
print( not f )
#source:  De programmeursleerling, Pieter Spronck



# BOOLEAN COMBINED WITH LOGICAL OPERATORS
#For the code below, give values True or False to each of the variables a, b, and c, so that the two expressions evaluate to different values.
#a = # True of False?
#b = # True of False?
#c = # True of False?
print( (a and b) or c )
print( a and (b or c) )
#source:  De programmeursleerling, Pieter Spronck



### EVALUATION ORDER OF BOOLEAN EXPRESSIONS
#Determine the output of the code below.
x = 1
y = 0
print( (x == 0) or (y == 0) or (x / y == 1) )
#PYTHON ANSWER: True, because left-to-right and stops as soon as evaluation is known.
#source:  De programmeursleerling, Pieter Spronck


### SELECTION
###   selection if




#Goal: understanding multiple if-statements in sequence, in combination with logical operators
x = 5
if x == 5:
    print( "x equals 5" )
if x > 4:
    print( "x is greater than 4" )
if x >= 5:
    print( "x is greater than or equal to 5" )
if x < 6:
    print( "x is less than 6" )
if x <= 5:
    print( "x is less than or equal to 5" )
if x != 6 :
    print( "x does not equal 6" )
#source:  De programmeursleerling, Pieter Spronck



#Goal: understanding program flow
#What does the following output to the console?
x = 3
if x == 4:
    print("Hi")
x = 5
#ANSWER: nothing
#source:  De programmeursleerling, Pieter Spronck





### 	selection two-branch
#Goal: understanding if-then-else, two-branch
x = 4
if x > 2:
    print( "x is bigger than 2" )
else:
    print( "x is smaller than or equal to 2" )
#source:  De programmeursleerling, Pieter Spronck


### SELECTION MULTI-BRANCH
#A80
age = 21
if age < 12:
    print( "You ' re still a child!" )
elif age < 18:
    print( "You are a teenager!" )
elif age < 30:
    print( "You ' re pretty young!" )
elif age < 50:
    print( "Wisening up, are we?" )
else:
    print( "Aren't the years weighing heavy?" )
#source:  De programmeursleerling, Pieter Spronck


#A80
#Goal understanding programming flow in a multi-branch selection
#Fic the reasoning error in the following code:
score = 98.0
if score >= 60.0:
    grade = ' D '
elif score >= 70.0:
    grade = ' C '
elif score >= 80.0:
    grade = ' B '
elif score >= 90.0:
    grade = ' A '
else:
    grade = ' F '
print( grade )
#source:  De programmeursleerling, Pieter Spronck



### LOOPS	while
#Goal: repeat printing output a fixed number of times (using counter controlled loop plan (while))
#A92, A93, A94
#What does the following code do?
num = 1
while num <= 5:
    print( num )
    num += 1
print( "Done" )
#Answer: print the numbers 1 to 5
#source:  De programmeursleerling, Pieter Spronck



#Goal: SUM PLAN: repeat prompting user-input a fixed number of times (using counter controlled loop plan (while))
#A92, A93, A94, user I/O (input), casting (basic function)
#What does the following code do?
total = 0
count = 0
while count < 5:
    total += int ( input( "Please give a number: " ))
    count += 1
print( "Total is", total )
#ANSWER: finds the sum of 5 input values
#source:  De programmeursleerling, Pieter Spronck


#Goal: SUM PLAN: add all numbers input by user (using sentinel controlled loop plan (while))
#A92, A93, A94, user I/O (input), casting (basic function)

#What does the following code do?
num = int (input( "Enter a number: " ))
total = 0
while num != 0:
    total += num
    num = int (input( "Enter a number: " ))
print( "Total is", total )
#source:  De programmeursleerling, Pieter Spronck


### FOR LOOPS: counter-controlled loop plan (FOR)
for letter in "banana":
    print( letter )
print( "Done" )
#source:  De programmeursleerling, Pieter Spronck

#FOR loop using a variable as collection
fruit = "banana"
for letter in fruit:
    print( letter )
print( "Done" )
#source:  De programmeursleerling, Pieter Spronck


#FOr loop loop using a range of numbers
for x in range( 10 ):
    print( x )
#ANSWER: prints the values 0 through and including 9
#source:  De programmeursleerling, Pieter Spronck

#For loop  with manual collections
for x in ("apple", "pear", "orange", "banana", "mango", "cherry"):
    print( x )
#source:  De programmeursleerling, Pieter Spronck

### METHODS & RETURN VALUES

#method control flow
def goodbyeWorld ():
    print( "Goodbye , world!" )

print( "Hello , world!" )
goodbyeWorld ()
#source:  De programmeursleerling, Pieter Spronck

#method control flow with parameters
def hello( name ):
    print( "Hello " +  name  )

hello( "Adrian" )
hello( "Binky" )
hello( "Caroline" )
hello( "Dante" )
#source:  De programmeursleerling, Pieter Spronck

#misconception: functions can change the value of the parameters
# What does the following code output?
# x = 1.56
# print( int( x ) )
# print( x )
# ANSWER: 1 and then 1.56

#control flow with return values
#misconception, code after return is still executed
def pythagoras( a, b ):
    if a <= 0 or b <= 0:
        return -1
        print( "This line will never be printed" )
    return sqrt( a * a + b * b )
#source:  De programmeursleerling, Pieter Spronck

#misconception: return is same as print
#what is the difference between print3() and return3()?
def print3():
    print( 3 )
print3()
#source:  De programmeursleerling, Pieter Spronck

def return3():
    return 3
print( return3() )
# ANSWER: Both the function print3() and return3() are called in their respective codes, and result
# in the printing of the value 3. The function print3() can only be used for one purpose, namely to display the number 3.
# The function return3(), however, can be used wherever I need the number 3, regardless
# whether I need to display it, use it in a calculation, or assign it to a variable.
#source:  De programmeursleerling, Pieter Spronck


### RECURSION
def factorial( n ):
    if n <= 1:
        return 1
    else:
        return n * factorial( n-1 )

print( factorial( 5 ) )
#source:  De programmeursleerling, Pieter Spronck

# --------- NESTING ------------- #


### (abst) datatypes int
# ????TODO???  CASTING: What is the result of the following: int("4") + 5?  ANSWER: 9
# ????TODO???  CASTING: What is the result of the following code: "I have" + str(15) + "appels"? ANSWER: I have 15 apples.

### VARIABLES
### variables	declaration
### variables assignment (and initialization)

### OPERATORS
### arithmetic operators	"+"
### relational operators	"=="


### SELECTION
###   selection if
### 	selection two-branch
### 	selection multi-branch


#BLOCK CODE NESTED IN A ONE-branch SELECTION
#Goal: understand program flow with nested code blocks in a one-branch selection
x = 7
if x < 10:
    print( "This line is only executed if x < 10." )
    print( "And the same holds for this line." )
print( "This line , however , is always executed." )

#BLOCK CODE NESTED IN A SELECTION
#Goal: understand program flow with nested code blocks in a two-way selection
num = int(input( "Please enter a positive integer: " ))
if num < 0:
    print( "You should have entered a positive integer!" )
else:
    print( "Now I am processing your integer", num )
    print( "Lots and lots of processing" )
    print( "Hundreds of lines of code here" )


# NESTING two-way selections in two-branch selections
age = 21
if age < 12:
    print( "You ' re still a child!" )
else:
    if age < 18:
        print( "You are a teenager!" )
    else:
        if age < 30:
            print( "You ' re pretty young!" )
        else:
            if age < 50:
                print( "Wisening up, are we?" )
            else:
                print( "Aren ' t the years weighing heavy?" )


#Goal relate a two-way selection nested in a two-way selection to an multi-branch
#What is the difference between the two following pieces of code?
#Code sample A:
age = 21
if age < 12:
    print( "You ' re still a child!" )
else:
    if age < 18:
        print( "You are a teenager!" )
    else:
        if age < 30:
            print( "You ' re pretty young!" )
#Code sample B:
age = 21
if age < 12:
    print( "You ' re still a child!" )
elif age < 18:
    print( "You are a teenager!" )
else:
    print( "You ' re pretty young!" )
#ANSWER: no difference



# NESTING A two-branch selection nested in a three-branch selection
x = 41
if x%7 == 0:
    # --- Here starts a nested block of code ---
    if x%11 == 0:
        print( x, "is dividable by both 7 and 11." )
    else:
        print( x, "is dividable by 7, but not by 11." )
    # --- Here ends the nested block of code ---
elif x%11 == 0:
    print( x, "is dividable by 11, but not by 7." )
else:
    print( x, "is dividable by neither 7 nor 11." )


### LOOPS	while



# --------- MERGING ------------- #


### (abst) datatypes int



### VARIABLES
### variables	declaration
### variables assignment (and initialization)

### OPERATORS
### arithmetic operators	"+"
### relational operators	"=="


### SELECTION
###   selection if
### 	selection two-branch
### 	selection multi-branch


### LOOPS	while




# --------- PLAN ------------- #

#INITIALISATION PLAN: datatype: int, variables, assignment operator '='
#JAVA
#int sum = 0;

#INITIALISATION PLAN: datatype: ARRAYS
#JAVA
# int letterCount[26]; // Array to store count of letters
# int i; // Iterative counter
# // Initialise array of counts
# for(i=0; i<26; i++) {
#     letterCount[i] = 0;
# }
#


#AVERAGE PLAN: SUM PLAN, COUNT PLAN, OPERATOR: /
#JAVA
# int sum = 15; // Stores the some of some numbers
# int count = 3; // Stores the count of those numbers
# int average; // Will store the calculated average
#
# // Calculate the average
# average = sum / count;
#
# // Output the average
# printf("Average: %i\n", average);

#PYTHON
sum = 15 # Stores the some of some numbers
count = 3 #Stores the count of those numbers

# Calculate the average
average = sum / count #Will store the calculated average

# Output the average
print("Average: " + str(average) ) #or print("Average: ", average)
#Note: to accept print("..", average) the student should show understanding that print is a function that accepts multiple variables
# if the student has merely learned to print a string, then the + opertor in combination with str() should be used
