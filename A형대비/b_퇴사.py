# 퇴사 14051
# 계산하는 함수

N = int(input())

for n in range(N):
    # T, P
   

    #DP선언
    dp = [0]*(N+1)
    for i in range(1, N+1):
        dp[i] = max(dp[i-1])