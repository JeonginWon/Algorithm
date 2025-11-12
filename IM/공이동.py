#IM 기출
#N*N 격자판, 격자의 각 칸에는 정수가 하나씩, 공은 어떤 칸에서 시작해서 상하좌우로 이동
#이동할 수 있는 조건 : 현재 칸보다 숫자가 작은 칸으로만 이동
# 가장 많이 이동할 수 있는 경우의 이동 횟수 구하기 (어디서 출발하면 가장 많이 이동할 수 있는지, 그 최대 이동 횟수를 구하기)

# 3
# 5
# 19 57 74 73 94
# 26 27 32 98 61
# 40 88 49 38 25
# 21 66 53 95 46
# 80 23 58 39 89
# 7
# 40 49 56 83 84 31 11
# 42 95 12 16 21 19 26
# 98 93 29 68 10 92 82
# 23 13 24 58 35 25 47
# 17 66 39 67 70 14 87
# 22 34 46 94 69 96 89
# 62 88 50 51 61 71 86
# 9
# 90 57 65 18 25 93 64 11 54
# 95 19 80 37 63 44 15 14 10
# 89 59 46 70 38 36 21 51 97
# 53 47 60 88 40 48 79 56 55
# 83 13 27 86 45 71 75 28 84
# 30 20 29 35 99 98 61 94 23
# 85 42 43 22 16 77 31 78 34
# 74 26 73 92 50 72 87 49 32
# 68 24 91 12 17 82 69 67 81

T = int(input())
delta = [(0,1),(0,-1),(1,0),(-1,0)]#방향
for tc in range(T):
    N = int(input())
    balls = [list(map(int, input().split())) for _ in range(N)]
    
    cnt_lst = []
    for i in range(N):
        for j in range(N):
            #현재위치 갱신
            x,y = i, j
            cnt = 0
            min_value = 100
            while True: #최솟값이 현재값보다 크면, break
                x_move, y_move = -1, -1
                for dx, dy in delta:
                    nx, ny = x+dx, y+dy #상하좌우 값
                    if 0<= nx<N and 0<= ny <N:
                        min_value = min(min_value, balls[nx][ny])
                        x,y = nx,ny
                        if min_value == balls[x][y]:
                            cnt+=1
                            break
                if x == -1:
                    break
    answer = max(cnt_lst)
    print(answer)



#답안
# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
# T = int(input())
T = 1
for test_case in range(1, T+1):
    N = int(input())
    
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_count = 0
    
    # 처음 시작 좌표
    for r in range(N):
        for c in range(N):
            count = 1
            pre_r = r
            pre_c = c
            # 최소값을 현재 시작 좌표로 설정
            min_r = pre_r
            min_c = pre_c
            min_number = arr[pre_r][pre_c]  
            # while 반복문 이용해서 더 못갈때까지 계속 좌표 찾기
            while True:                              
                # 시작값 비교 상하좌우값 비교
                for k in range(4):
                    nr = pre_r + dr[k]
                    nc = pre_c + dc[k]
                    # nr nc가 유효하다면 유효한 상하좌우값 중에 가장 작은 값과 작은 값의 좌표 찾기
                    if 0<= nr < N and 0<= nc < N:
                        if arr[nr][nc] < min_number:
                            min_number=arr[nr][nc]
                            min_r = nr
                            min_c = nc
                
                # 자기 자신이 최소값이면 while 반복문 끝 
                if min_r == pre_r and min_c == pre_c:
                    max_count = max(max_count, count)
                    break
                else:
                    pre_r = min_r 
                    pre_c = min_c
                    count += 1 
     
    print(max_count)