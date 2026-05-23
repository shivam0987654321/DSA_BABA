n = [5,3,2,2,1,5,5,7,5,10]
m =[10,111,1,9,5,67,2]

# Note when it is given that value can be only till 10 in n 

# create a hash_list with 11 zeros 

hash_list = [0]* (len(n) + 1)

for num in n :
    hash_list[num] = hash_list[num] + 1

for num in m:
    if num < 0 or num > 10:
        print("0")
    else:
        print(hash_list[num])