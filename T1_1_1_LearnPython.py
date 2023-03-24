"""
#Print function and its feature
#Dyanmic typing and Static typing - In python we dont need to specify any variable type
#Dynamics Binding - In python we can have 1 variable holding multiple data types , string,int,float
#Python is a case sensitive Langauge
print("India","Pakistan","Nepal","Srilanka")
print("India","Pakistan","Nepal","Srilanka",sep="-")
print("India","Pakistan","Nepal","Srilanka",end="\n")

#keyword
import keyword
print(keyword.kwlist)
#Identifiers Numbers cant have start for variable for eg a = 9 is valid but 9 = a is not valid

#input from user
#input(prompt ="Divey")

# Implicit - System internally adds automatically
print(4+4.5)
# Explicit - Where programmer needs to tell
a = eval(input("Enter a number"))
b = eval(input("Enter a number"))
print(a+b)

# Literals - Data given to python - Numerical (Binary,Decimal,Octal,hexadecimal,float), string,boolean,special
# Operators - Arithmetic + - * / //, Comparison > != ==, Logical, Bitwise AND OR NOT XOR << >>, Assignemnt =, Identity is , Membership in

# If ELse Elif statement
"""
# Guessing Number
import random
random.randint(1,100)
