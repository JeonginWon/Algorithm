# N*N 보드에 N개의 퀸이 서로 공격 못하게 놓는 경우의 수는 몇가지?
T = int(input())

#퀸을 행마다 하나씩 배치
def n_queen(row):
    global answer

    if row == N:
        answer += 1
        return
    
    for col in range(N):
        # 세로 검사 통과 & 좌하향 통과 & 우하향 통과
        #미방문 상태일때만 가로 검사
        if not col_visited[col] and not main_diag_visited[row-col+N-1] and not sub_diag_visited[row+col]:
            col_visited[col] = 1
            main_diag_visited[row-col+N-1] = 1
            sub_diag_visited[row+col] = 1

            n_queen(row+1)

            #원복 재귀
            col_visited[col] = 0
            main_diag_visited[row-col+N-1] = 0
            sub_diag_visited[row+col] = 0
            #방문기록 체크


#필요 데이터    
for tc in range(1, T+1):
    N = int(input())

    col_visited = [0] * N
    main_diag_visited = [0] * (2*N-1)
    sub_diag_visited = [0] *(2*N-1)
    answer = 0

    n_queen(0)

    print(f'#{tc} {answer}')


# 가로검사가 필요없음. 한 행에 하나의 퀸이 들어가는 것은 자명함.