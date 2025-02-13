import sys
from itertools import combinations

s=list(map(int, sys.stdin.readline().split()))
while s[0] != 0:
    k=s[0]
    combs=combinations(s[1:], 6)
    for comb in combs:
        print(' '.join(map(str, comb)))
    print()
    s=list(map(int, sys.stdin.readline().split()))