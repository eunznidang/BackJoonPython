def mkSum(number):
    sum=number
    for i in range(len(str(number))-1, -1, -1):
        sum+=(number // (10**i))
        number %= (10**i)
    return sum

N=int(input())
answer=0

for i in range(N):
    if mkSum(i)==N:
        answer=i
        break

print(answer)