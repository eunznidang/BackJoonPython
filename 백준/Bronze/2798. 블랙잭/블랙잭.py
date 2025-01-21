#  카드 N장 중 3장 뽑아서 M 이하로 최대한 크게
N, M= map(int, input().split())
numb=list(map(int, input().split()))

array=[]
for i in range(N):
    for j in range(N):
        for k in range(N):
            if(i!=j and i!=k and j!=k):
                sum=numb[i]+numb[j]+numb[k]
                if sum<=M:
                    array.append(sum)


print(max(array))