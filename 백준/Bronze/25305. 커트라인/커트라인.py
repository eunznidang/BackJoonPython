N, k=map(int, input().split())
score=list(map(int, input().split()))

score.sort(reverse=True) # 내림차순 정렬
print(score[k-1])