T = int(input())
for tc in range(T):
    matrix = []
    for i in range(9):
        row = list(map(int,(input().split())))
        matrix.append(row)
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
        row2_lst = [row[j] for row in matrix]
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
    answer3 = []
    total3 = 0
    for i in range(0,9,3):
        for j in range(0,9,3):
            block = [row[j:j+3] for row in matrix[i:i+3]]

            for _ in block:
                block_list = sum(block, [])
                block_set = set(block_list)
            if len(block_set) == 9:
                answer3.append(1)
            else:
                answer3.append(0)
        if sum(answer3)%9 == 0:
            total3 += 1
        else:
            total3 += 0

    answer = total1+total2+total3
    if answer == 0:
        print(f'Case {tc+1}: INCORRECT')
    elif answer%3 == 0:
        print(f'Case {tc+1}: CORRECT')
    else:
        print(f'Case {tc+1}: INCORRECT')
    if tc != T:
        input()