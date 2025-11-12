# 부분 문제가 전체 로직과 동일할 때 dp를 이용한다.
T = int(input())
for tc in range(1,1+T):
    day, month, quarter, year = map(int,input().split())
    plans = list(map(int, input().split()))

    answer = year

    dp = [0]*13 #0은 시작점이 필요해요 따라서 13이 되어야 한다.
    # dp[0] = 0

    for i in range(1, 13):

        dp[i] = min(dp[i-1] + plans[i-1]*day, dp[i-1]+month) # 이전 까지 썼던 것 중에 최소비용 + 일권 비용
        if i >= 3:
            dp[i] = min(dp[i], dp[i-3]+quarter)
        

        if dp[i] >= answer:
            break
    
    else:
        answer = dp[12]

    
    print(f'#{tc} {answer}')