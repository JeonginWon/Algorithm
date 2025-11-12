S = list(input())
alpha = ['a', 'b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
answer =[]
for a in alpha:
    if a not in S:
        answer.append(-1)
    else:
        answer.append(S.index(a))
print(*answer)