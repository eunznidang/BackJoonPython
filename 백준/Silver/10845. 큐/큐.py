import sys
N=int(sys.stdin.readline())
queue=[]

for i in range(N):
    command=sys.stdin.readline()
    if 'push' in command:
        queue.append(command.split()[1])
    elif 'pop' in command:
        try: print(queue.pop(0))
        except: print('-1')
    elif 'size' in command:
        print(len(queue))
    elif 'empty' in command:
        if len(queue)==0: print(1)
        else: print (0)
    elif 'front' in command:
        try: print(queue[0])
        except: print(-1)
    else:
        try: print(queue[len(queue)-1])
        except: print(-1)
