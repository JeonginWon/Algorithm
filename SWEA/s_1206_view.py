for tc in range(10):
    N = int(input())
    heights = list(map(int,(input().split())))
    sum_heights = 0
    for i in range(N-4):
        comp = heights[i:i+5]
        max_com = max(comp)
        # print(max(comp))
        if (comp[2] - max(comp[0],comp[1],comp[3],comp[4])) <= 0:
            sum_heights += 0
        else:
            sum_heights += (comp[2]-max(comp[0],comp[1],comp[3],comp[4]))

    print(f'#{tc+1} {sum_heights}')