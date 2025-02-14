import sys

def tracking(t, idx):
    if idx==(n-1):
        return t
    
    if t%arr[idx]!=0:
        return tracking(t*arr[idx], idx)
    else:
        return tracking(t, idx+1)
    

n=int(sys.stdin.readline())
arr=list(map(int, sys.stdin.readline().split()))
arr.sort()

print(tracking(max(arr)*min(arr), 0))