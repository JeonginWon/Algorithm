
T =int(input())

for tc in range(T):
        
    N,M = map(int,input().split())

    matrix = [list(map(int,input().split())) for _ in range(N)]

    max_count = 0

    for i in range(N):
        count = 0
        for j in range(M):
            if matrix[i][j] == 1:
                count += 1
            
            if matrix[i][j] == 0:
                if max_count < count:
                    max_count = count
                count = 0

        max_count = max(max_count,count)



    for j in range(M):
        col_count = 0
        for i in range(N):
            if matrix[i][j] == 1:
                col_count += 1
        
            
            if matrix[i][j] == 0:
                if max_count < col_count:
                    max_count = col_count
                col_count = 0


        max_count = max(max_count,col_count)

    if max_count <= 1:
        print(f'#{tc+1} 0')

    else:
        print(f'#{tc+1} {max_count}')