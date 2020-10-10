# You'll learn:
#Define functions without parameters
# Define functions with one parameter
# Define functions that return a value
# Later: How to pass multiple arguments to functions, as well as return multiple values from them

# str()

x = str(5)
print(x)
print(type(x))

# Defining a functions

def square():   #<- Function header
    new_value = 4 ** 2  # <- Function body
    print(new_value)
square()

# Function parameters

def square(value):
    new_value = value ** 2
    print(new_value)
square(5)

# RETURN VALUES FROM FUNCTIONS

# - Return a value from a functions using return

def square(value):
    new_value = value ** 2
    return new_value
num = square(6)

print(num)

# DOCSTRINGS

#   Docstrings describe what your functions does, such as the computations it perfors or its return values.
#   Serve as documentation for your functions
#   Placed in the immediate line after the function header
#   In between triple double quotes """ docstrings """

def square(value):
    """Returns the square of a value."""
    new_value = value ** 2
    return new_value
num2 = square(7)



