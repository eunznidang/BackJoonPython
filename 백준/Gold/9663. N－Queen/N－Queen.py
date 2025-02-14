import sys

def check(q):
    global n, cnt
    if q==n:
        cnt+=1
        return
    
    for i in range(n):
        # 위아래, 대각선1, 대각선2 확인
        if not col[i] and not line1[n-1+(q-i)] and not line2[q+i]:
            col[i]=True
            line1[n-1+(q-i)]=True
            line2[q+i]=True
            check(q+1)
            col[i]=False
            line1[n-1+(q-i)]=False
            line2[q+i]=False
    

n=int(sys.stdin.readline())
cnt=0
col=[False] * n # 열 확인 
line1=[False]*(2*(n-1)+1) # 대각선 1
line2=[False]*(2*(n-1)+1) # 대각선 2

check(0)
print(cnt)


