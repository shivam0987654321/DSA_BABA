s = "azyxyyzaaa"
q =["d","a","y","z"]

from collections import Counter 

Count = Counter(s)

for i in range(len(q)):
    print(Count.get((q[i]),0))