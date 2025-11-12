# 글자수
T = int(input())
for tc in range(T):
    str1 = list(input())
    str2 = list(input())
    #문자열 길이 정의-> for문에 사용
    N = len(str1)
    M = len(str2)
    #cnt저장할 list
    cnt_lst = []
    #str1 원소 순회 - str2에서 해당원소 count
    for n in range(N):
        cnt = str2.count(str1[n])
        cnt_lst.append(cnt)
    answer = max(cnt_lst)

    print(f'#{tc+1} {answer}')
                