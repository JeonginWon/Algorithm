#sum
for tc in range(10):
    tc = int(input())
    r=100
    c=100
    matrix = [list(map(int, input().split())) for _ in range(r)]

    #row
    row_sum = [0]*r
    for i in range(r):
        for j in range(c):
            row_sum[i] += matrix[i][j]
    n1 = max(row_sum)


    #col
    col_sum = [0]*c
    for j in range(c):
        for i in range(r):
            col_sum[j] += matrix[i][j]
    n2 = max(col_sum)


    #cross
    cross1_sum = sum([matrix[i][i] for i in range(100)])
    cross2_sum = sum([matrix[i][r-1-i] for i in range(100)])
    n3 = max(cross1_sum,cross2_sum)

    #max
    answer = max(n1, n2, n3)
    print(f'#{tc} {answer}')
