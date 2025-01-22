import sys

N=int(input())
number=[0] * 10001

for i in range(N):
    # number.append(int(sys.stdin.readline()))
    # append: 메모리 초과.
    number[int(sys.stdin.readline())]+=1 # 계수정렬 사용

for i in range(10001):
    for j in range(number[i]):
        print(i)