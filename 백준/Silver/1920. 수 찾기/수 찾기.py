import sys

N=int(sys.stdin.readline())
array1=list(map(int, sys.stdin.readline().split()))
array1.sort()
M=int(sys.stdin.readline())
array2=list(map(int, sys.stdin.readline().split()))

def binarySearch(left, right, target):
    if left>=right:
        if array1[left]==target:
            return 1
        else:
            return 0
    mid=(left+right)//2
    if array1[mid]==target:
        return 1
    elif array1[mid]<target:
        return binarySearch(mid+1,right,target)
    else:
        return binarySearch(left,mid-1,target)

for i in array2:
    print(binarySearch(0, N-1, i))