# 길찾기 DPS, DFS

#dfs정의
def dfs(node):
    global answer
    if node == 99:
        answer = 1
        return
    for next_node in adj_list[node]:
        #다음 지점
        if visited[next_node]: #방문하지 않을때
            continue
        #else: 필요없음. 방문했다면 무조건 다음으로 진행됨.
        visited[next_node] = 1 #다음 노드 가기 전에 방문 처리
        dfs(next_node)
        #visited[next_node] = 0
T = 10
for tc in range(1, T+1):
    _, M = map(int,input().split()) # M = 간선의 수
    info = list(map(int, input().split()))
    adj_list = [[] for _ in range(100)] #빈리스트 100개
    answer = 0
    visited = [0]*100 #특정 번호를 찾을 때

    for i in range(M):
        a = info[2*i] # 출발지 a
        b = info[2*i +1] # 도착지 b

        adj_list[a].append(b) #A가 갈 수 있는 노드
        # adj_list[b].append(a) # 무향 그래프일 때, 이 한 줄 추가

    #dfs이동
    visited[0] = 1 #방문 처리
    dfs(0) #초기값
    #visited[0] = 0

    print(f'#{tc} {answer}')