T = int(input())
for tc in range(T):
    N = int(input())
    numbers = list(map(int, input()))
    count = 0
    count_lst = []
    for i in range(N):
        if numbers[i]==1:
            count += 1
            count_lst.append(count)
        else:
            count = 0
    print(count_lst)
    answer = max(count_lst)
    print(f'#{tc+1} {answer}')