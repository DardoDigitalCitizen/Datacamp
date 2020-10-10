# MULTIPLE FUNCTION PARAMETERS

# Accept more than 1 parameter:
def raise_to_power(value1, value2):
    """Raiser value1 to the power of value2"""
    new_value = value1 ** value2
    return new_value

# Call function: #of arguments = # of parameters

result = raise_to_power(2, 3)
print(result)

# A QUICK JUMP INTO TUPLES

# Make functions return multiple values: Tuples!

# TUPLES:
#   - Like a list = can contain multiple values
#   - BUT! Unlike a list, its...
#       - Immutable = it can't modify values!
#       - Constructed using parentheses()
even_nums = (2, 4, 6)
print(type(even_nums))

# UNPACKING TUPLES

# Unpack a tuple into several variables:
even_nums = (2, 4, 6)
a, b, c = even_nums

print(a)
print(b)
print(c)

#ACCESSING TUPLE ELEMENTS

# Access tuple elements like you do with lists:
even_nums = (3, 5, 7)
print(even_nums[1])

second_num = even_nums[1]
print(second_num)
# Uses zero-indexing

# RETURNING MULTIPLE VALUES
def raise_both(value1, value2):
    """Raise value1 to the power of value2 and vice versa."""
    new_value1 = value1 ** value2
    new_value2 = value2 ** value1

    new_tuple = (new_value1, new_value2)
    return new_tuple

result = raise_both(2, 3)
print(result)