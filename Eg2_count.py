# We have to count the numbers :
# Solution 1: 

n = 5678
count = 0
while n > 0:
    count = count + 1
    n = n // 10 # floor division give you integer

print(count)

# one liner
# Solution 2: 

n = 5676878

import math
number=int(math.log10(n) + 1 ) 
print(number)