import sys

def makeN(n):
    if n==1:
        return 1
    elif n==2:
        return 2
    elif n==3:
        return 4
    else:
        return makeN(n-1)+makeN(n-2)+makeN(n-3)
T=int(sys.stdin.readline())
for i in range(T):
    dp=[[]]
    n=int(sys.stdin.readline())
    print(makeN(n))
