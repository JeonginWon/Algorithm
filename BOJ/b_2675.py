T = int(input())

for tc in range(T):
    R, S = map(list, input().split())
    R = int(R[0])
    answer = []
    for s in S:
        A = s*R
        answer.append(A)
    print(''.join(answer))
