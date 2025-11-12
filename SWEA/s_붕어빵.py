# 진기의 붕어빵
T = int(input())
# 필요한 데이터
for x in range(T):
    N, M, K = map(int,input().split()) # N : 손님 수, M : 붕어빵 만드는 시간, K : 붕어빵 갯수
    buyer = list(map(map(int, input().split())))

    # M초마다 K개의 붕어빵 생산
    # 도착 시간을 오름차순으로 정렬 (먼저오는사람 먼저 줘야 함)
    buyer.sort()
    
    # 손님 방문 count하는 변수 선언 / cnt = 0
    # for 반복문 (buyer 순회)
        # i번째로 손님이 도착하는 시간을 붕어빵 만드는 시간으로 나누기 -> 몫 * k = 손님오기전에 만들어진 붕어빵 갯수
        # 도착한 손님 count (누적)

        # if 문 : 붕어빵보다 손님이 많은지 검사
            # 만들어진 붕어빵 갯수 < count한 손님 수 이면 대기발생 -> impossible출력
        # 아니면 (같거나 작으면) -> possible출력

        # answer에 'possible'이나 'impossible' 할당

        # print('#{tc+1} {answer}')

    # 1. 손님 도착 시간 정렬(선착순)

    # 2. 손님 도착 시간 리스트 순회
        # ㄱ. 붕어빵을 줄 수 있을 때
        #      현재 손님 번째 <= 현재 생산 붕어빵량
        #       > ~번째 : range 또는 count 필요
        #       > 도착 당시 붕어빵량 : 도착시간 / M * K
        # ㄴ. 붕어빵을 줄 수 없을 때
        #       > 순회 중지 - Impossible

    # 3. 순회 중 붕어빵을 줄 수 없는 경우가 없었을 때 > Possible
T = int(input())

for tc in range(1, T+1):
    N, M, K = map(int, input().split())  # 사람 수, 걸리는 시간, 한 번에 만드는 붕어빵 수
    customers = list(map(int, input().split()))
    customers.sort()  # 도착 시간을 오름차순 정렬

    possible = True
    for i in range(N):
        arrival = customers[i]            # i번째 손님 도착 시간
        made = (arrival // M) * K         # arrival 시각까지 만들어진 붕어빵 개수
        served = i + 1                    # 지금까지 도착한 손님 수
        if made < served:                 # 만들어진 붕어빵보다 손님 수가 많으면 대기 발생
            possible = False
            break

    print(f'#{tc} {"Possible" if possible else "Impossible"}')
