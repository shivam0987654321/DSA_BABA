# https://www.geeksforgeeks.org/problems/armstrong-numbers2727/1
number = 1634 
original = number 
result = 0 
length = len(str(number))
while number > 0:
    last_digit = number % 10
    result = result + (last_digit)**length
    number = number // 10 

if result == original:
    print("armstrong")
else:
    print("nhi")
