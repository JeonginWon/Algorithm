# 회문1
for tc in range(10):
    N = int(input()) #회문길이
    arr = [input() for _ in range(8)] #회문 matrix input
    cnt = 0 #회문 세서 저장할 변수 선언
    #행
    
    for i in range(8):
        for j in range(9-N):
            block = '' # 글자수 N개의 회문
            block += arr[i][j:j+N] #회문 저장, N간격만큼
            if block== block[::-1] and len(block) == N: #회문을 거꾸로 해도 똑같은지 조건 + 회문의 길이가 N인지
                cnt += 1

    #열
    for j in range(8):
        for i in range(9-N):
            block =''
            for k in range(N): # 세로 열에서 k 즉, N만큼 순회하기 위한 for문
                block += (arr[i+k][j]) 
            if block == block[::-1]:
                cnt += 1
    
    print(f'#{tc+1} {cnt}')



# for t in range(10):
#     k = int(input())
#     arr = [input() for _ in range(8)]
#     cnt = 0
 
#     # 행 순회
#     for r in range(8):
#         for i in range(8-k+1):
#             words = ''
#             words += arr[r][i:i+k]
#             if words == words[::-1] and len(words) == k:
#                 cnt += 1
 
#     # 열 순회
#     for r in range(8):
#         for c in range(8 - k + 1):
#             words = ''
#             for j in range(k):
#                 if c+j < 8:
#                     words += arr[c+j][r]
#             if words == words[::-1]:
#                 cnt += 1
# #     print(f"#{tc} {cnt}")
