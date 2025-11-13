# 퇴사 14051
# 계산하는 함수

N = int(input())
time = []
pay = []
for n in range(N):
    # Time, Pay
    t, p = map(int, input().split())
    time.append(t)
    pay.append(p)

    #DP선언
    dp = [0]*(N+1)
    for i in range(1, N+1):
        if time[i-1] <= N-i+1: #근무가능
            dp[i] = max(dp[i-1], )
        else:
            pass
            #근무 불가능
            
# print(time)