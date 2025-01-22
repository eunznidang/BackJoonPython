import sys # input 보다 얘가 효율적
# input: prompt message 출력, 개행 문자 삭제하는 데 시간이 더 걸림

N=int(input())
number=[]
for i in range(N):
    number.append(int(sys.stdin.readline()))

for i in sorted(number) : print(i)