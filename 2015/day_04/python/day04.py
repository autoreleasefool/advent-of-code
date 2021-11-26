from hashlib import md5

## Part 1

# Input from the site
PUZZLE_INPUT = "ckczppom"

# Start with checking 1
lowest_positive_int = 1
hashed = md5()
hashed.update(("ckczppom" + str(lowest_positive_int)).encode())
digest = hashed.hexdigest()

# While the first 5 characters are not all 0s, increment the counter and generate a new hash
while digest[:5] != "00000":
    lowest_positive_int += 1
    hashed = md5()
    hashed.update((PUZZLE_INPUT + str(lowest_positive_int)).encode())
    digest = hashed.hexdigest()

# Print the lowest valid positive integer
p1_solution = lowest_positive_int
print(p1_solution)

## Part 2

# Start with checking 1
lowest_positive_int = 1
hashed = md5()
hashed.update(("ckczppom" + str(lowest_positive_int)).encode())
digest = hashed.hexdigest()

# While the first 6 characters are not all 0s, increment the counter and generate a new hash
while digest[:6] != "000000":
    lowest_positive_int += 1
    hashed = md5()
    hashed.update((PUZZLE_INPUT + str(lowest_positive_int)).encode())
    digest = hashed.hexdigest()

# Print the lowest valid positive integer
p2_solution = lowest_positive_int
print(p2_solution)
