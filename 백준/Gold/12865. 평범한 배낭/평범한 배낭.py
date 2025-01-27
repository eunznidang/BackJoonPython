# 다이나믹 프로그래밍
n, k=map(int, input().split())

# 2차원 배열 dp 
dp = [[0] * (k + 1) for _ in range(n + 1)]

item=[]
for i in range(n):
    item.append(list(map(int, input().split())))


for i in range(1, n+1):
    # total 무게를 0~k로 설정
    for j in range(1, k+1):
        weight, value=item[i-1]
        
        # 현재 물건 담을 수 없음
        if j<weight:
            dp[i][j]=dp[i-1][j]

        # 현재 물건 담을 수 있음
        else:
            # dp[i-1][j]: 현재 물건 포함 안 함
            # value + dp[i-1][j-weight]: 현재 물건 포함
            dp[i][j]=max(dp[i-1][j], (value + dp[i-1][j-weight]))

print(dp[n][k])