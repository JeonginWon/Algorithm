T = int(input())
for tc in range(T):
    N,M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    arr_vertical = [[0]*N for _ in range(M)]
    for i in range(M):
        for j in range(N):
            arr_vertical[i][j] = arr[j][i]
    
    max_cnt = 0
    # 행
    for n in range(N):
        cnt = 0
        for m in range(M):
            if arr[n][m] == 1:
                cnt += 1 #연속된 1의 갯수 count

            if arr[n][m] ==0:
                if max_cnt< cnt:
                    max_cnt = cnt
                cnt = 0
        max_cnt = max(max_cnt,cnt)
            
    #열 순회
    #vertical 행은 M*N
    for n in range(M):
        cnt_ver = 0
        for m in range(N):
            if arr_vertical[n][m] == 1:
                cnt_ver += 1 #연속된 1의 갯수 count

            if arr_vertical[n][m] ==0: #0 정의해주면 반복문이 계속돌면서 행이 바뀌어도 1값 누적 x
                if max_cnt< cnt_ver:
                    max_cnt = cnt_ver #최댓값 갱신
                cnt_ver = 0 
                
        max_cnt = max(max_cnt,cnt_ver)
    
    if max_cnt <= 1:
        print(f'#{tc+1} 0')

    else:
        print(f'#{tc+1} {max_cnt}')
