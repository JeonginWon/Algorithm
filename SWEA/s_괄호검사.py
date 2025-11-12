T = int(input())
for tc in range(T):
    text = input()
    top =-1
    #스택생성
    stack = [0]*100
    #()탐색
    ans = 1
    for x in text:
        if x =='(' or x== '{': #여는 괄호인 경우
            top+= 1
            stack[top] = x #text의 x를 top에 push
        elif x == ')' or x =='}': #닫는 괄호인 경우
            if top == -1: #스택이 비어있으면
                ans = 0 #여는 괄호가 없음 -> 0 -> break
                break
            # else: #여는 괄호 하나 버림
            #     top -= 1 #pop
            elif x ==')' and stack[top] == '(':
                top -= 1
            elif x == '}' and stack[top] == '{':
                top -= 1

            else:
                is_correct = 0
                break

    if top != -1: #여는 괄호가 남아있으면 0
        ans = 0
    print(f'#{tc+1} {ans}')
            
