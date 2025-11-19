# 로봇청소기
N,M = map(int, input().split())
r,c,d = map(int, input().split())
room = [list(map(int, input().split()))for _ in range(N)]

# 방향 (동서남북)
