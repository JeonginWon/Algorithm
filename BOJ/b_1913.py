N = int(input())
num_tofind = int(input())





T = int(input())
for tc in range(T):
    N = int(input())
    
    # numbers = list(range(1, N**2+1)) #숫자열
    matrix_snail = [[0]*N for _ in range(N)]
    # print(matrix_snail[0][0])
    direction_x= [1, 0, -1, 0]
    direction_y = [0, 1, 0, -1]
    time = []
    for t in range(N):
        time.append(N-t)
        time.append(N-t)
    time.remove(N)
    #print(time)

    y, x = 0, -1 #start location # 시작하자마자 우측으로 이동하는거 -1 (index_out_of_range)
    dir = 0 #direction
    num = 1 #start

    matrix_snail[y][x] = num
    # num += 1
    for t in time:
        for _ in range(t):
            y += direction_y[dir]
            x += direction_x[dir]
            matrix_snail[y][x] = num
            num += 1
        dir = (dir + 1) % 4



    print(f'#{tc+1}')
    for row in matrix_snail:
        print(*row)
