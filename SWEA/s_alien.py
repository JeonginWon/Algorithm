# 우주 괴물
T = int(input())
for tc in range(T):
    N= int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 시작점 정의 (우주괴물 위치)
    for i in range(N):
        for j in range(N):
           if arr[i][j] == 2:
               nx = i
               ny = j
    # 광선 방향
    delta = [(0,1), (1,0), (0,-1), (-1,0)]
    laser_lst = []
    # 광선 지나가기
    for dx, dy in delta:
        for i in range(1,N):
            laser_x, laser_y = nx + dx*i, ny + dy*i
            if 0<= laser_x <N and 0<= laser_y<N:
                laser=arr[laser_x][laser_y]
                # print(laser) # 00010000
            #laser가 지나가는 길이 0이면 +1(attack), 1이면 stop
                if laser == 0:
                    laser += 1
                elif laser == 1:
                    break
                laser_lst.append(laser)
    # 전체 arr의 0 갯수 - 1로 바뀐 0의 갯수(attacked area)
    cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0:
                cnt+=1
            else:
                cnt+=0
    answer = cnt - len(laser_lst)
    print(f'#{tc+1} {answer}')
                


