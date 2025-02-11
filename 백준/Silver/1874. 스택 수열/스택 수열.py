import sys
n=int(sys.stdin.readline())
res=[]
state=True
stack=[]

number=1
for i in range(n):
    target=int(sys.stdin.readline())
    
    # push
    if target >= number:
        while target >= number:
            stack.append(number)
            number+=1
            res.append('+')
    
    # pop
    if stack:
        while stack and target != stack[len(stack)-1]:
            s=stack.pop()
            res.append('-')
        if stack:
            s=stack.pop()
            res.append('-')
    
    # NO인 경우
    else:
        state=False
        break

if state:
    for i in res:
        sys.stdout.write(str(i)+'\n')
else:
    print('NO')