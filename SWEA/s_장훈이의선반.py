T = int(input())
# 점원 키를 nCr로 뽑아서 B이상 중 가장 최소인 것 구하기

#조합
picked = []
def comb(cnt, idx):
    global answer
    if sum(picked) == B:
        answer = 0
        return
 
    if sum(picked) >= B:
        answer = min(answer, sum(picked) - B)  
  
    if cnt == len(heights):
        return
    for i in range(idx, len(heights)):
        picked.append(heights[i])
        comb(cnt+1, i+1)
        picked.pop()
  
  
for tc in range(T):
    N, B = map(int, input().split())
    heights = list(map(int, input().split()))
    answer = 1e10
    comb(0,0)
    print(f"#{tc+1} {answer}")