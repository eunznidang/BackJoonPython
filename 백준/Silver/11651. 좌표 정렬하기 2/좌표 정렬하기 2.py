N=int(input())
dot=[]
for i in range(N):
    dot.append(list(map(int,input().split())))

# y로 정렬 후 x로 정렬
dot.sort(key=lambda x: (x[1], x[0]))

for i in range(N):
    print(dot[i][0], dot[i][1])