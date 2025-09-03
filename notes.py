# def is the keyword to define a function 
#what type is the name of the function
# userInput is the parameter of the function 
def whatType(userInput):
    print(type(userInput))
    # print is a Python built-in fuction that prints to the console 
    # type is a Python-built in function that finds the data type 
    # userInput is the variable that the user enters 
    print(type(userInput))
# the pound symbol is for one line comments
# the program ignores all comments 
"""
multiple line comments 
"""
#Call the function with different inputs 
#If you dont call the functions, nothing will run in the program 

"""
Test SUITE
"""
whatType(3)
whatType(3.0)
whatType("3.0")
whatType(True)
whatType("Alice")
whatType('p')

#create a variable named message 
message = """this is a 
multiline message 
to my bestie."""
print(message)

#test inputs to print and see how they print 
print(42000)
#every time you have a comma between values, it will understand it as a different 
#parameter input 
print(42, "poly", 3, "chem", "computer")
print(42000)
print(42,000)
