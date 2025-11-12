# 어디에 단어가 들어갈 수 있을까
T = int(input())
for tc in range(T):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    
    print(arr)
    row_total = 0
    for i in range(N):
        for j in range(N):
            row_count = 0
            if arr[i][j] == arr[i][j+1] and arr[i][j] ==1:
                row_count += 1
            else :
                row_count += 0
        print(row_count)
    #         if row_count == K-1:
    #             row_total +=1
    #         else:
    #             row_total += 0
    # print(row_total)
    
    col_total = 0
    col_count = 0
    for j in range(N-1):
        for i in range(N-1):
            if arr[j][i] == arr[j][i+1] and arr[j][i+1] ==1:
                col_count += 1
            else:
                col_count += 0
    if col_count == K-1:
        col_total += 1
    else:
        col_total += 0
    
    answer = row_total + col_total
    print(f'#{tc+1} {answer}')

