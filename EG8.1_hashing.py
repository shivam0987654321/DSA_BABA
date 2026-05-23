n = [5,3,2,2,1,5,5,7,5,10]
m =[10,111,1,9,5,67,2]

# shortcut 

from collections import Counter

Count_n = Counter(n)
 
print(Count_n)


for num in m :
    print(Count_n.get(num,0))