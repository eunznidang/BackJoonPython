import sys

testcase=int(input())
for i in range(testcase):
    n, m=map(int, sys.stdin.readline().split())
    priority=[]
    queue=[]
    if n==1:
        sys.stdin.readline()
        print('1')
        continue

    else:
        for j in list(map(int, sys.stdin.readline().split())):
            queue.append(j)
        priority=sorted(queue,reverse=True)
        count=0

        while True:
            if queue[0]==priority[0] and m==0:
                count+=1
                print(count)
                break
            elif queue[0]==priority[0]:
                queue.pop(0)
                priority.pop(0)
                count+=1
                m-=1
            else:
                tmp=queue.pop(0)
                queue.append(tmp)
                if m !=0:
                    m-=1
                else:
                    m=len(queue)-1
    

            