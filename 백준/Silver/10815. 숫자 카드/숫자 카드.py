import sys

N=int(sys.stdin.readline())
array=list(map(int, sys.stdin.readline().split()))
M=int(sys.stdin.readline())
array2=list(map(int, sys.stdin.readline().split()))
array.sort()

def binarySearch(left, right, card):
    if left>=right:
        if array[left]==card:
            return '1'
        else:
            return '0'
    mid=(left+right)//2
    if array[mid]==card:
        return '1'
    elif array[mid]<card:
        return binarySearch(mid+1, right, card)
    else:
        return binarySearch(left, mid-1, card)
    
for i in array2:
    sys.stdout.write(binarySearch(0, N-1, i) + ' ')