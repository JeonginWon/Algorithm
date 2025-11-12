N, M = map(int, input().split())
visited = []
def solve(cnt):
    if cnt == M:
        print(*visited)
        return
    for n in range(1, N+1):
        if n in visited:
            continue
        visited.append(n)
        solve(cnt+1)
        visited.pop()
solve(0)