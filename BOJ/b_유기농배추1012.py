import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    field = [[0] * M for _ in range(N)]

    for _ in range(K):
        x, y = map(int, input().split())
        field[y][x] = 1

    cnt = 0
    dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]

    for y in range(N):
        for x in range(M):
            if field[y][x] == 1:
                cnt += 1
                stack = [(x, y)]
                field[y][x] = 0  # 방문 처리

                while stack:
                    cx, cy = stack.pop()
                    for dx, dy in dirs:
                        nx, ny = cx + dx, cy + dy
                        if 0 <= nx < M and 0 <= ny < N and field[ny][nx] == 1:
                            field[ny][nx] = 0
                            stack.append((nx, ny))

    print(cnt)
