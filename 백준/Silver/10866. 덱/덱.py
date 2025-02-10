import sys
N=int(sys.stdin.readline())
deque=[]

for i in range(N):
    command=sys.stdin.readline()
    if 'push_front' in command:
        deque.insert(0, command.split()[1])
    elif 'push_back' in command:
        deque.append(command.split()[1])
    elif 'pop_front' in command:
        try: print(deque.pop(0))
        except: print('-1')
    elif 'pop_back' in command:
        try: print(deque.pop())
        except: print('-1')
    elif 'size' in command:
        print(len(deque))
    elif 'empty' in command:
        if len(deque)==0: print(1)
        else: print (0)
    elif 'front' in command:
        try: print(deque[0])
        except: print(-1)
    else:
        try: print(deque[len(deque)-1])
        except: print(-1)
