import sys
n=int(input())

def checkVPS(sentence):
    res=0
    for i in sentence:
        if i == '(':
            res+=1
        else:
            res-=1
        
        if res<0:
            return('NO')

    if res==0:
        return('YES')
    else: return('NO')

for i in range(n):
    vps=list(sys.stdin.readline().strip())
    print(checkVPS(vps))