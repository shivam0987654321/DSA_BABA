n = [5,3,2,2,1,5,5,7,5,10]
m =[10,111,1,9,5,67,2]


dicti = {}
for i in range(len(n)):
    if n[i] in dicti:
        dicti[n[i]]+=1
    else:
        dicti[n[i]] = 1


for num in m :
    print(dicti.get(num,0))


