#팩토리얼 함수 (역순으로 곱하기)

n = 5  # 변경 X > 목적지이기 때문
answer = 1

def fact(depth):
    global answer
    if n == depth:
        return
    else:
        answer *= (depth+1)
        fact(depth + 1)

fact(1)
print(answer)


##강사님 답안
n = 5  # 변경 X > 목적지이기 때문
answer = 1

def fact(depth):
    global answer
    if n == depth:
        return
    else:
        depth += 1
        answer *= (depth)
        fact(depth + 1)

fact(1)
print(answer)

#재귀함수 연습해오기