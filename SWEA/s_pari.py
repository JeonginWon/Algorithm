#파리퇴치 연습
# 파리퇴치 3

#+ 
def plus_spray(x,y):
    delta = [(0,1), (0,-1), (1,0),(-1,0)] #방향 좌표
    total = arr[x][y] #각 좌표의 총 합

    for dx, dy in delta: #방향 이동 반복
        for m in range(1, M): # M강도 만큼 지정
            nx, ny = x+dx*m, y+dy*m # spray가 나가는 좌표들 정의
            if 0<=nx <N and 0<= ny <N: #범위 넘어가서 생기는 오류 방지
                total += arr[nx][ny] #각 좌표값 누적 합
    return total

    
#x
def cross_spray(x,y):
    delta = [(1,1), (1,-1), (-1,1),(-1,-1)] #방향 좌표
    total = arr[x][y] #각 좌표의 총 합
    for dx, dy in delta:
        for m in range(1, M):
            nx, ny = x+dx*m, y+dy*m 
            if 0<= nx < N and 0 <= ny < N:
                total += arr[nx][ny] 
    return total


T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    answer = 0
    for i in range(N):
        for j in range(N):
            answer = max(answer, plus_spray(i,j), cross_spray(i,j))
    print(f'#{tc+1} {answer}')



# 파리퇴치 1
