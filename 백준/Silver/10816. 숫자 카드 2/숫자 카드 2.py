import sys
n=int(input())
card={}
for i in list(map(int, sys.stdin.readline().split())):
    if i in card:
        card[i]=card[i]+1
    else:
        card[i]=1

m=int(input())
for number in list(map(int, sys.stdin.readline().split())):
    if number in card:
        sys.stdout.write(str(card[number])+' ')
    else:
        sys.stdout.write('0 ')

