# 수영장
# 이용권 계산하는 함수 swim (1월 ~ 12월, 현재 최솟값 = price)
# answer = price갱신
    # 12월까지만 순회 완료후 최솟값 출력

    # 1년 이용권 제외 먼저 계산
        # 1년 이용권이 앞서 계산한 price보다 작으면 1년 채택
    # day, month1, month3 이용권 

def swim(month, price):
    global answer
    if month > 12: #12월 순회 끝나면
        answer = min(answer, price) # answer 최솟값 출력
        return
     
    if answer <= price: # 1년 이용권 요금이 계산한 price(day, month1, month3을 조합한 값)보다 작으면 1년 이요권 선택
        return
    swim(month+1, price + (plan_monthly[month] * day)) # day이용권
    swim(month+1, price + month1) # 1달 이용권
    swim(month+3, price + month3) # 3달 이용권


T = int(input())
for tc in range(T):
    day, month1, month3, year = map(int, input().split())
    plan = list(map(int, input().split()))

    plan_monthly = [0] + plan # 월별로 이용해야 하는 day수 저장, month가 바뀌면 초기화해야함 -> 0삽입
    answer = year # year요금 저장
    swim(1, 0)
    print(f'#{tc+1} {answer}')
    