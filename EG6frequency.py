nums = [5,6,7,7,1,9,11,1,1]
dicti = {}

for i in range(0,len(nums)):
    if nums[i] in dicti:
        dicti[nums[i]]+=1
    else:
        dicti[nums[i]] = 1

print(dicti)

# Shortcut :
dicti1={}

for i in range(0,len(nums)):
    dicti1[nums[i]] = dicti1.get(nums[i],0) + 1
print(dicti1)