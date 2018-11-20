##############################
#                            #
#        Instructions        #
#                            #
##############################

# To run, use the following command:
# $ python ignorered.py <input_file>
# where <input_file> is the filename with the question's input

import sys
import re
import json

# Check to make sure correct number of arguments supplied
if (len(sys.argv) != 2):
    print('Invalid number of arguments!')
    sys.exit()

# Read the input from the file provided as argument
input_file = open(sys.argv[1])
puzzle_input = json.loads(input_file.read())
input_file.close()

# Recursively gets the sum of an object in the JSON document
def get_sum(obj):
	total = 0

	# If the object is a list, get the subtotal of each item
	if isinstance(obj, list):
		for item in obj:
			total += get_sum(item)

	# If the object is a dictionary, get the subtotal of each item
	# or return 0 if any item has a value of 'red'
	elif isinstance(obj, dict):
		for item in obj:
			if obj[item] == 'red':
				return 0
			else:
				total += get_sum(obj[item])

	# If the object is a primitive
	else:
		# If the value is red, return 0
		if obj == 'red':
			return 0

		# Otherwise, try to add the item to the sum or add nothing if its not an integer
		try:
			total += int(obj)
		except ValueError:
			total += 0
			# do nothing
	return total

# For each item in the JSON document, add its subtotal to the total
total = 0
for item in puzzle_input:
	total += get_sum(puzzle_input[item])

# Print the total
print ('The sum of all the non-red numbers in the document is', total)
