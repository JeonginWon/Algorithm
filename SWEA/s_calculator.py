# 계산기
T = 10
#입력
for tc in range(1, T+1):
    N = int(input())
    stack = [0]*(N+1)
    top =-1
    infix = input()
    icp = {'(':3, '*':2, '/':2, '+':1, '-':1} # 밖에 있을 때의 우선순위 (클수록 높음)
    isp = {'(':0, '*':2, '/':2, '+':1, '-':1} # 스택 안에서의 우선 순위(")
    postfix = ''

    answer =0
	

    for token in infix:
        if token not in '(+-*/)':  # 피연산자라면 후위식에 추가
                postfix += token
                answer += int(token)
        else:
            if top == -1 or isp[stack[top]] < icp[token]:
                top += 1
                stack[top] = token 
            elif isp[stack[top]] >= icp[token]:
                while top > -1 and isp[stack[top]] >= icp[token]:
                    postfix += stack[top]
                    top -= 1
                top += 1
                stack[top] = token
    print(f"#{tc} {answer}")