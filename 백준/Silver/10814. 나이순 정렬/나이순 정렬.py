import sys
N=int(input())
people=[]
for i in range(N):
    age, name=sys.stdin.readline().split()
    people.append([int(age), name]) # 숫자 정렬 시 반드시 int형으로 바꾸기

people.sort(key=lambda x: (x[0]))

for p in people:
    print(p[0], p[1])
