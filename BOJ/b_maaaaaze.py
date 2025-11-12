# 5*5*5 판
# 층은 바꾸기 가능
# 0은 못 들어가는 칸 검은색
# 1은 들어갈 수 있는 칸 흰색
# 최단거리 = BFS 사용
from collections import deque
# # 3차원 델타 선언
dx=[1,-1,0,0,0,0]
dy=[0,0,1,-1,0,0]
dz=[0,0,0,0,1,-1]
dir = [0,0,0,0,0]

# 순열 구하기
def perm(arr, count):
    # 종료 조건
    if count == 5:
        perm_list.append(list(picked_number))        
        return 
    
    for i in range(5):
        if visited[i] == 1:
            continue
        picked_number.append(arr[i])
        visited[i] = 1
        perm(arr, count+1)
        picked_number.pop()
        visited[i] = 0

visited = [0]*5
picked_number = []
perm_list = []
number = [0,1,2,3,4]
perm(number, 0)

# 판을 회전하는 함수
def turn(arr, dir):    
    turn_arr = [[0]*5 for _ in range(5)]
    for i in range(5):
        for j in range(5):
            turn_arr[j][4-i]=arr[i][j]
    return turn_arr 


# 미로 탈출 함수(BFS)
def escape(maze):
    global res
    cnt=1
    queue = deque()
    # enque
    queue.append((0,0,0))
    while queue:
        if (4,4,4) in queue:
            temp_res=cnt
            if res==-1:
                res=temp_res
            else:
                res=min(res,temp_res)
            break
        x,y,z=queue.popleft()
        for i in range(6):
            nx,ny,nz=x+dx[i],y+dy[i],z+dz[i]
            if 0<=nx<5 and 0<=ny<5 and 0<=nz<5 and maze[nx][ny][nz]==1 and visited[nx][ny][nz]==0:
                queue.append((nx,ny,nz))
                visited[nx][ny][nz]==cnt
        cnt+=1



# # 층
plate_1=[[0]*5 for _ in range(5)]
plate_2=[[0]*5 for _ in range(5)]
plate_3=[[0]*5 for _ in range(5)]
plate_4=[[0]*5 for _ in range(5)]
plate_5=[[0]*5 for _ in range(5)]
# 층에 넣어주기
for i in range(5):
    plate_1[i] = list(map(int, input().split()))
for i in range(5):
    plate_2[i] = list(map(int, input().split()))
for i in range(5):
    plate_3[i] = list(map(int, input().split()))
for i in range(5):
    plate_4[i] = list(map(int, input().split()))
for i in range(5):
    plate_5[i] = list(map(int, input().split()))

visited = [[[0]*5 for _ in range(5)] for _ in range(5)]

res = -1

maze = [plate_1, plate_2, plate_3, plate_4, plate_5]
for plate_order in perm_list:
    new_maze = [maze[plate_order[0]], maze[plate_order[1]], maze[plate_order[2]], maze[plate_order[3]], maze[plate_order[4]]]
    isright = True
    # 0,0,0이 0이면 1이 나올때까지 돌리기
    while new_maze[0][0][0] == 0:
        new_maze[0] = turn(new_maze[0])
        dir[0] = (dir[0]+1)
        # 돌려도 시작을 못함
        if dir[0] == 4:
            isright = False
            break                
    if isright == False:
        continue
    # 시작할 수 있다면
    escape(new_maze)

print(res)
        







