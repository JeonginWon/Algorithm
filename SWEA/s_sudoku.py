T = int(input())
for tc in range(T):
    matrix = []
    for i in range(9):
        row = list(map(int,(input().split())))
        matrix.append(row)
    # print(matrix[:][0])
    total1 = 0
    answer1 = []

    #case1
    for j in range(9):
        row1_lst = matrix[j][:] #스도쿠 가로
        row1 = set(matrix[j][:])

        if len(row1) == 9:
            answer1.append(1)
        else:
            answer1.append(0)
    if sum(answer1)%9 ==0:
        total1 += 1
    else:
        total1 += 0

    #case2
    total2 = 0
    answer2 = []
    for j in range(9):
        row2_lst = [row[j] for row in matrix] #스도쿠 세로
        row2 = set(row2_lst)
    
        if len(row2) == 9:
            answer2.append(1)
        else:
            answer2.append(0)
    if sum(answer2)%9 == 0:
        total2 += 1
    else:
        total2 +=0


    #case3
    total3 = 0
    answer3 = []
    dist = 3
    row3_lst =[]
    for i in range(0,9,3):
        for j in range(0,9,3):
            block = [row[j:j+3] for row in matrix[i:i+3]]
            # print(set(block))
            for n in range(3):
                block_len = sum(sum(row) for row in block)
            if block_len == 45:
                answer3.append(1)
            else:
                answer3.append(0)
            if sum(answer3)%9 ==0:
                total3 += 1
            else:
                total3 += 0 
    # print(total1)
    # print(total2)
    # print(total3)
    answer = total1+total2+total3
    # print(answer)
    if answer == 0:
        print(f'#{tc+1} 0')
    elif answer%3 == 0:
        print(f'#{tc+1} 1')
    else:
        print(f'#{tc+1} 0')