# 우하, 좌하, 좌상, 우상
dr = [1, 1, -1, -1]
dc = [1, -1, -1, 1]
 
T = int(input())
 
def dessert_run(r, c, turn1, turn2):
    dessert_set = set()
 
    counts = [turn1, turn2, turn1, turn2]
    for dir in range(4):
        for i in range(counts[dir]):
            r += dr[dir]
            c += dc[dir]
            # print(r, c)
            if desserts[r][c] in dessert_set:
                return -1
            dessert_set.add(desserts[r][c])
     
    return len(dessert_set)
 
 
for tc in range(1, T+1):
    N = int(input())
    desserts = [list(map(int, input().split())) for _ in range(N)]
    answer = -1
 
    for s_r in range(N-2):
        for s_c in range(1, N-1):
             
            for turn1 in range(1, N-s_c):
                for turn2 in range(1, N-(s_r+turn1)):
                    if s_c - turn2 >= 0 and (turn1+turn2)*2 > answer:
                        answer = max(answer, dessert_run(s_r, s_c, turn1, turn2))
 
    print(f'#{tc} {answer}')
