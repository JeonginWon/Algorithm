# 퇴사 14051


N = int(input())
time = []
pay = []

for _ in range(N):
    t, p = map(int, input().split())
    time.append(t)
    pay.append(p)

    # DP배열
dp = [0]*(N+1) # N+1 까지 생성 / 여기에 누적 수익금 저장

for i in range(N-1, -1, -1): # bottom-up
    # i번째 날 상담을 했는데? 퇴사일 넘으면
    if i + time[i] > N: # 근무 불가
        dp[i] = dp[i + 1] # 다음 날 이익 그대로 
    else: # 근무 가능
        # 근무 yes or no 선택을 했을 때 중 큰 값 선택
        dp[i] = max(pay[i] + dp[i + time[i]], dp[i + 1])
            
print(dp[0])
