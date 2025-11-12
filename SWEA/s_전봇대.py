# import sys
# sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(T):
    N = int(input())
    
    wires =[]
    answer = 0
    for _ in range(N):
        start, end = map(int, input().split())

        #기존 선들과 비교(교차점 비교)
        for prev_start, prev_end in wires:
            #1. 기존의 전선보다 시작점이 높고, 도착점이 낮음
            if start > prev_start and end < prev_end:
                answer += 1

            #2. 기존의 전선보다 시작점이 낮고, 도착점이 높음
            if start < prev_start and end > prev_end:
                answer += 1
        #목록에 추가
        wires.append((start, end))
    print(f'#{tc+1} {answer}')

# 분할정렬
