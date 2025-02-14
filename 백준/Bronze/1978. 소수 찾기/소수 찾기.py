import sys

def factorint(target):
    factors={}
    d=2
    while d*d<=target:
        while target%d==0:
            if d not in factors:
                factors[d]=1
            else:
                factors[d]+=1
            target//=d
        d+=1
    if target>1:
        factors[target]=1
    return factors
    
n=int(sys.stdin.readline())
res=0

for target in list(map(int, sys.stdin.readline().split())):
    factors=factorint(target)
    if len(factors)==1 and list(factors.values())[0]==1:
        res+=1

print(res)
