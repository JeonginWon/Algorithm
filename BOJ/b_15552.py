# 시간초과
# T = int(input())
# for i in range(T):
#     a, b = map(int, input().split())
#     print(a+b)


# sys.stdin.readline()
import sys
input = lambda: sys.stdin.readline().rstrip()
T = int(input())
for i in range(T):
    a, b = map(int, input().split())
    print(a+b)