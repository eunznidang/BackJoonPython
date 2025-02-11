import sys
n=int(input())
array=set(map(int,sys.stdin.readline().split()))


array=sorted(array)

for i in range(len(array)-1):
    sys.stdout.write(str(array[i]) +' ')

sys.stdout.write(str(array[len(array)-1]))