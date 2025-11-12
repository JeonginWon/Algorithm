T = int(input())
for _ in range(T):
    S = input()
    S_lst = list(S)
    answer = S_lst[0]+S_lst[-1]
    print(answer)