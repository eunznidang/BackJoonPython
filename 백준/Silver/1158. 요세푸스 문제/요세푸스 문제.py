import sys
from collections import deque
n, k=map(int, sys.stdin.readline().split())

dq=deque()
for i in range(1,n+1):
    dq.append(i)

res=[]
while dq:
    dq.rotate(k*(-1))
    res.append(str(dq.pop()))

print('<'+', '.join(res)+'>')