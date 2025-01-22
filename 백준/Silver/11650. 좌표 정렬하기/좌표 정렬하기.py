import sys
N=int(input())
dot=[]
for i in range(N):
    dot.append(list(map(int,input().split())))

# x로 정렬 후 y로 정렬
dot.sort(key=lambda x: (x[0], x[1]))

for i in range(N):
    print(dot[i][0], dot[i][1])