# 힙
import heapq
import sys

N=int(sys.stdin.readline())

leftHeap=[] # 최대힙: 루트가 가장 큰 값
rightHeap=[] #최소힙: 루트가 가장 최솟값

answer=[]
for i in range(N):
    number=int(sys.stdin.readline())

    # leftHeap에 넣을 땐 부호 바꾸기
    if len(leftHeap)==len(rightHeap):
        heapq.heappush(leftHeap, -number)
    else:
        heapq.heappush(rightHeap, number)

    # left, right 루트 비교
    if  rightHeap and (leftHeap[0]*-1)>rightHeap[0]:
        toRight=heapq.heappop(leftHeap)
        toLeft=heapq.heappop(rightHeap)
        heapq.heappush(rightHeap, toRight*-1)
        heapq.heappush(leftHeap, toLeft*-1)

    # 중앙값 저장
    answer.append(leftHeap[0]*-1)

for i in answer:
    print(i)