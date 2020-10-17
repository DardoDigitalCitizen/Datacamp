"""
Somebody thought it would be funny to mess with your accurately generated dictionary. An adapted version of the europe
dictionary is available in the script on the right.

Can you clean up? Do not do this by adapting the definition of europe, but by adding Python commands to the script to
update and remove key:value pairs.
"""

# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'bonn',
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw',
          'australia':'vienna' }

# The capital of Germany is not 'bonn'; it's 'berlin'. Update its value.
europe['germany'] = 'berlin'

# Australia is not in Europe, Austria is! Remove the key 'australia' from europe.
del europe['australia']

# Print out europe to see if your cleaning work paid off.
print(europe)