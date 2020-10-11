"""Hugo mentioned that different types behave differently in Python.
When you sum two strings, for example, you'll get different behavior than when you sum two integers or two booleans.

In the script some variables with different types have already been created. It's up to you to use them."""

savings = 100
growth_multiplier = 1.1
desc = "compound interest"

# Calculate the product of savings and growth_multiplier. Store the result in year1
year1 = savings * growth_multiplier

# What do you think the resulting type will be? Find out by printing out the type of year1.
print(year1)
print(type(year1))

# Calculate the sum of desc and desc and store the result in a new variable doubledesc
doubledesc = desc + desc

# Print out doubledesc. Did you expect this?
print(doubledesc)