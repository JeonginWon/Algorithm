for tc in range(10):
    dump = int(input())
    box = list(map(int, input().split()))
    sort_box = sorted(box)
    for i in range(dump):
        sort_box[0] = sort_box[0] + 1
        sort_box[-1] = sort_box[-1] - 1
        sort_box.sort()
    answer = sort_box[-1]-sort_box[0]
    print(f'#{tc+1} {answer}')