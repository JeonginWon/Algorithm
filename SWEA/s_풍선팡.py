T = int(input())
for tc in range(T):
    N = int(input())
    bubble = [list(map(int, input().split())) for _ in range(N)]

    #시작점마다 +모양에 있는 숫자 합 중 최댓값 (파리퇴치3과 비슷한 문제)
    #+모양으로 풍선 더하기
    def bubble_score(x,y):
        delta = [(0,1),(0,-1),(1,0),(-1,0)] #우좌상하 direction 설정
        total = bubble[x][y] #시작점을 기준으로 순회하면서 누적합
        for dx, dy in delta: #방향순회
            for n in range(1,N): #순회 범위
                nx, ny = x+dx*n, y+dy*n 
                if 0<= nx<N and 0<= ny < N:
                    total += bubble[nx][ny] #순회하는 좌표들의 누적값
        return total
    answer = 0
    for i in range(N):
        for j in range(N):
            answer = max(answer, bubble_score(i,j))
    print(f'#{tc+1} {answer}')


#답안
dy = [-1, 1, 0, 0] # 상 하 좌 우
dx = [0, 0, -1, 1]

def get_score(y, x): # score 계산해서 그 결과를 달라
    score = arr[y][x] # 초기화 - 현재좌표

    for i in range(4): # 방향이 4방향이라서 (상, 하, 좌, 우)
        ny, nx = y, x # 현재 위치
        while True:
            ny += dy[i]
            nx += dx[i]
            if 0 <= ny < N and 0 <= nx < N: score += arr[ny][nx] # 점수계산
            else: break # 범위벗어나면 break

    return score


T = int(input())


for tc in range(1, T + 1):
    N = int(input()) # NxN 행렬
    arr = [list(map(int, input().split())) for _ in range(N)] # 2차원 배열
    result = float('-inf')  # 최대값 초기화 (음의 무한대)

    for y in range(N): # 행순회
        for x in range(N):
            # 함수호출하면서 최대값 갱신
            # 함수 왜 만들까?? ---> 디버깅 때문에!!
            temp = get_score(y, x)
            result = max(result, temp)

    print(f'#{tc} {result}') # 최대값 출력

dy = [-1, 1, 0, 0] # 상 하 좌 우
dx = [0, 0, -1, 1]

def get_score(y, x): # score 계산해서 그 결과를 달라
    score = arr[y][x] # 초기화 - 현재좌표

    for i in range(4): # 방향이 4방향이라서 (상, 하, 좌, 우)
        ny, nx = y, x # 현재 위치
        while True:
            ny += dy[i]
            nx += dx[i]
            if 0 <= ny < N and 0 <= nx < N: score += arr[ny][nx] # 점수계산
            else: break # 범위벗어나면 break

    return score


T = int(input())


for tc in range(1, T + 1):
    N = int(input()) # NxN 행렬
    arr = [list(map(int, input().split())) for _ in range(N)] # 2차원 배열
    result = float('-inf')  # 최대값 초기화 (음의 무한대)

    for y in range(N): # 행순회
        for x in range(N):
            # 함수호출하면서 최대값 갱신
            # 함수 왜 만들까?? ---> 디버깅 때문에!!
            temp = get_score(y, x)
            result = max(result, temp)

    print(f'#{tc} {result}') # 최대값 출력
