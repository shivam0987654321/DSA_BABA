n = 12132
original = n
result = 0 
while n > 0:
    last_digit = n % 10
    result = (result * 10) + last_digit
    n = n // 10 

if result == original:
    print("palidrome mila")
else:
    print("not a palidrome")