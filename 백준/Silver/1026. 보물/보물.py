import sys
n=int(input())
a=list(map(int,sys.stdin.readline().split()))
b=list(map(int,sys.stdin.readline().split()))

a.sort(reverse=True)
b.sort()
sum=0
for i in range (n):
    sum+=a[i]*b[i]

print(sum)