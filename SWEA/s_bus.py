#전기버스
T = int(input())
for tc in range(T):
    K,N,M = map(int, input().split())
    stops = list(map(int, input().split()))
    stops.append(N) #-1 position부터 시작하는 거 말고, 종점을 충전소로 추가

    position = 0 
    charge_count = 0 

    while position + K < N:
        #다음 충전소 탐색
        go_range = [s for s in stops if position < s <= position + K]
        if not go_range:
            #한 칸도 못가면 종료. retrun 0
            charge_count = 0
            break
        # 충전할 곳으로 이동 (최대거리 이동)
        position = go_range[-1]
        charge_count += 1
    print(f'#{tc+1} {charge_count}')
        



# T = int(input())
# for tc in range(1, T+1):
#     K, N, M = map(int, input().split())
#     stations = list(map(int, input().split()))
#     stations.append(N)           # 도착지를 충전소 목록에 추가
 
#     position = 0                 # 현재 위치
#     charge_count = 0             # 충전 횟수
 
#     # 도착지에 다다를 수 있을 때까지 반복
#     while position + K < N:
#         # 갈 수 있는 범위(position, position+K] 내 충전소만 골라서
#         reachable = [s for s in stations if position < s <= position + K]
#         if not reachable:
#             # 한 칸도 못 가면 종료하고 0 리턴
#             charge_count = 0
#             break
#         # 가장 먼 곳으로 이동(충전)
#         position = reachable[-1]
#         charge_count += 1
 
#     print(f"#{tc} {charge_count}")