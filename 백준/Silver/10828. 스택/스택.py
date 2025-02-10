import sys
N=int(sys.stdin.readline())
stack=[]

for i in range(N):
    command=sys.stdin.readline()
    if 'push' in command:
        stack.append(command.split()[1])
    elif 'pop' in command:
        try: print(stack.pop())
        except: print('-1')
    elif 'size' in command:
        print(len(stack))
    elif 'empty' in command:
        if len(stack)==0: print(1)
        else: print (0)
    else:
        try: print(stack[len(stack)-1])
        except: print(-1)