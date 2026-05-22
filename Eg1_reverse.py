# We have to reverse the number :

n = 5678

while n > 0 :
    last_digit = n % 10
    print(last_digit)
    n = n // 10

