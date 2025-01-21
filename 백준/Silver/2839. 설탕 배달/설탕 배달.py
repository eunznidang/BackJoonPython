def find(N):
    for x in range(5001):
        for y in range(5001):
            if (x*3 + y*5) == N:
                return x+y
    return -1

N = int(input())
print(find(N))