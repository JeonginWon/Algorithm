# 최빈수 구하기
from collections import Counter

T = int(input())
for i in range(T):
    tc = int(input())
    scores = list(map(int, input().split()))
    counts = Counter(scores)
    max_values= max(counts.values())
    max_keys = [key for key, value in counts.items() if value == max_values]
    answer = max(max_keys)
    print(f'#{tc} {answer}')


# sort : 원본 순서도 뒤집힘
# sorted : 원본 유지
T = int(input())
for i in range(T):
    tc = int(input())
    scores = list(map(int, input().split()))
    scores.sort(reverse=True)

    #현재 카운팅 > current_count
    #누적 카운팅 최대 > max_count
    #이전 값 > before_score

    current_count = 0
    max_count =0
    before_score = -1 #전에 없는 값 (예시에 없는 값)

    for score in scores:
        if before_score != score:
            if max_count < current_count:
                max_count = current_count
                answer = before_score
            current_count = 1
        else:
            current_count +=1
        before_score = score

        
