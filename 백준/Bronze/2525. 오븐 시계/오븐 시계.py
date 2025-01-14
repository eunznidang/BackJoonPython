A, B=map(int, input().split())
C=int(input())

B=B+C
H=B//60
M=B%60

A=A+H
print(str(A%24) +' ' + str(M))