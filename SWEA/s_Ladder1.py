

# a, b : 현재 위치 / ni, nj : 새로 갈 위치
# 이동하는 함수 

def ladder(a, b, arr):
    dir_i = [0, 0, -1] # 위치 좌표 정의
    dir_j = [1, -1, 0]
    while True:
        for k in range(3):
            ni = a + dir_i[k] #좌우 
            nj = b + dir_j[k] #상 
            if ni == 0: #좌우 우선 고려, 좌우 이동 후엔 위로가는 것 고려 / 
                return nj
            if 0<= ni <100 and 0 <= nj < 100 and arr[ni][nj] == 1:
                arr[a][b] = 0 # 다시 돌아오는 거 방지, 방문한 좌표 0으로 바꾸기 /현재위치는 0처리
                a = ni #새로 간 좌표 저장
                b = nj #새로 간 좌표 저장
                break #for문 나와서 while 다시 진행


# 도착지점 위치 출력하는 조건문
for tc in range(10):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    
    for i in range(99, 100):
        for j in range(100):
            if arr[i][j] == 2:
                a = i
                b = j
                break
        break
    print(f'#{tc} {ladder(a, b, arr)}')



# 강사님 코드
dr = [-1,0,0]
dc = [0, -1, 1]
search_dir = [[1,2,0], [0,1],[0,2]]

T =10
for tc in range(1, T+1):
    input()
    ladder = [list(map(int, input().split())) for _ in range(100)]
    # 시작점
    r=99
    c = ladder[99].index(2)
    #다음 방향 탐색
    dir = 0
    while r> 0:
        for i in range(len(search_dir[dir])):
            #다음 방향 후보
            next_dir = search_dir[dir][i]
            next_r = r+dr[next_dir]
            next_c = c+dc[next_dir]

            if 0 <= next_c < 100 and ladder[next_r][next_c] ==1:
                dir = next_dir
                r = next_c
                r = next_r
                break
    print(f'#{tc} {c}')

