import sys
from collections import deque

T=int(sys.stdin.readline())
flag=True
for i in range(T):
        p=list(sys.stdin.readline().strip())
        n=int(sys.stdin.readline())
        if n!=0:
            arr=deque(map(int,sys.stdin.readline().strip()[1:-1].split(',')))
        elif n==0 and 'D' in p:
             sys.stdin.readline()
             print('error')
             continue
        elif n==0 and 'D' not in p:
             sys.stdin.readline()
             print('[]')
             continue

        state=True

        flag=True
        for ac in p:
            if ac=='R' and n!=0:
                 flag=not flag
            elif ac=='D':
                try:
                    if flag:
                        arr.popleft()
                    else:
                        arr.pop()
                except:
                     state=False
                     print('error')
                     break
        
        if state:
            if flag:
                print('[' + ','.join(map(str,arr))+ ']')
            else:
                arr.reverse()
                print('[' + ','.join(map(str,arr))+ ']')

