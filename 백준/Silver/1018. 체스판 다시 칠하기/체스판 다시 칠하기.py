N, M=map(int, input().split())
array=[]
for i in range(N):
    array.append(list(input()))

count=[]
tmp=[]
templit1=['W','B','W','B','W','B','W','B']
templit2=['B','W','B','W','B','W','B','W']

c=0

for i in range(0, N - 7):
    for j in range(0, M - 7):
        tmp=templit1
        count.append(0)
        for k in range(8):
            for l in range(8):
                if array[i+k][j+l] != tmp[l]:
                    count[c]+=1
            if tmp==templit1:
                tmp=templit2
            else:
                tmp=templit1
        c+=1

        count.append(0)
        tmp=templit2
        for k in range(8):
            for l in range(8):
                if array[i+k][j+l] != tmp[l]:
                    count[c]+=1
            if tmp==templit1:
                tmp=templit2
            else:
                tmp=templit1
        c+=1

print(min(count))