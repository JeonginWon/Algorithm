# 피자 굽기
T = int(input())
for tc in range(T):
    N , M = map(int, input()) # 화덕의 크기 N, 피자개수 M 
    Ci = list(map(int, input().split())) # 치즈의 양

    # 피자 화덕에 넣기
    # 
    for n in range(N):
        