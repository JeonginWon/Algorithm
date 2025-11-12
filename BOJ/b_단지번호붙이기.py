# 단지번호 붙이기

# 필요 로직
# bfs logic : 단지마다house 세는 함수
# house 좌표저장하는 덱
# 센 house는 1-> 0 으로 변환
# 0 으로 바꿔줄때마다 house_count+=1
from collections import deque
def count_house(x,y):
    #deque 생성
    q = deque()
    # delta
    delta_x = [0, -1, 0, 1]
    delta_y = [1, 0 , -1, 0]
    #house 세기
    house_count = 1
    arr[x][y] = 0 #초기화
    q.append([x,y])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + delta_x[i], y + delta_y[i]
            if 0 <= nx < N and 0 <= ny < N: 
                if arr[nx][ny] == 1:
                    q.append([nx,ny])
                    arr[nx][ny] = 0
                    house_count+=1
    return house_count

# 필요데이터
N = int(input())
arr = [list(map(int, input())) for _ in range(N)]

# 단지 수 세기
cnt = 0
result = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            result.append(count_house(i,j))
            cnt += 1
result.sort() # 오름차순
print(cnt)

for n in result:
    print(n)