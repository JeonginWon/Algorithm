T = int(input())
for tc in range(T):
    room = int(input())
    box = list(map(int, input().split()))
    count_lst = []
    
    start = 0
    for i in box:
        fall_count =0
        for _ in range(start,room):
            if i  > box[_]:
                fall_count += 1
            start += 1
        count_lst.append(fall_count)

    print(f'#{tc+1} {max(count_lst)}')