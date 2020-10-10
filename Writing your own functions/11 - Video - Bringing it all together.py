# YOU'VE LEARNED
#   How to write functions
#       Accept multiple parameters
#       Return multiple values
# Up next: FUNCTIONS FOR ANALYZING TWITTER DATA

# LET'S RECAP: BASIC INGREDIENTS OF A FUNCTION

#   Function Header: Which begins with the keyword 'def'. This is followed by the functions name,
#   parameters in parentheses and a colon (:).
def raise_both(value1, value2):
    new_value1 = value1 ** value2
    new_value2 = value2 ** value1

    new_tuple = (new_value1, new_value2)

    return new_tuple

# Function Body: Which contains docstrings enclosed in triple quotation marks ("""docstrings""");
# docstrings describes what the functions does; the rest of the function body performs the computation
"""Raise value1 to the power of value2 and vice versa."""
# that the function does; the function body closes with the keyword 'return',
# followed by the value or values returned by the function.