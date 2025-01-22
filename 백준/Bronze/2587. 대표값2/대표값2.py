import math

array=[]
for i in range(5):
    array.append(int(input()))

print(math.ceil(sum(array)/len(array)))
array.sort()
print(array[math.ceil(len(array)/2)-1])