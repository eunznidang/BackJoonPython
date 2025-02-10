import sys
left=list(sys.stdin.readline().strip())
right=[]
N=int(sys.stdin.readline())

for i in range(N):
    command=sys.stdin.readline()
    if 'L' in command and left:
        right.append(left.pop())
    elif 'D' in command and right:
        left.append(right.pop())
    elif 'B' in command and left:
        left.pop()
    elif 'P' in command: # insert 시간 초과 사용 불가.
        left.append(command.split()[1])

print(''.join(left)+''.join(right[::-1]))