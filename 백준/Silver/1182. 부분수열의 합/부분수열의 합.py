import sys
from itertools import combinations

n, s=map(int, sys.stdin.readline().split())
arr=list(map(int, sys.stdin.readline().split()))

res=0
for i in range(1, n+1):
    for comb in combinations(arr, i):
        sum=0
        for c in comb:
            sum+=c
        if sum==s:
            res+=1

print(res)