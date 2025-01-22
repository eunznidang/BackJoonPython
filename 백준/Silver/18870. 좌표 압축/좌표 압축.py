import sys
N=int(input())
cord=list(map(int,(input().split())))

dic={y:x for x, y in enumerate(sorted(set(cord)))}

for c in cord:
    print(dic[c], end=" ")