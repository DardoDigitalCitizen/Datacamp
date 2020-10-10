#In the last video, Hugo described the basics of how to define a function.
# You will now write your own function!

#Define a function, shout(), which simply prints out a string with three exclamation marks '!!!' at the end.
# The code for the square() function that we wrote earlier is found below.
# You can use it as a pattern to define shout().
"""def square():
    new_value = 4 ** 2
    return new_value"""

# Define the function shout
def shout():
    """Print a string with three exclamation marks!!!"""
    # Concatenate the strings: shout_word
    shout_word = 'congratulations' + '!!!'

    # Print shout_word
    print(shout_word)

#Call shout
shout()
