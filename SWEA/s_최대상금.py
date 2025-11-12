#최대상금
   # 교환 로직 (교환횟수 trans만큼 반복)
    # 자릿수 교환 로직(순열) 중복허용 nums에서 2개 뽑기
    #  >뽑힌 수들 자리 교환
 
    # 크기 비교 로직
    # 교환 완료되고 교환 로직에서 탈출, 
    # 리스트 형태로 교환됨 -> 숫자로 변환하여 상금(money)변수에 저장
    #  현재 교환해서 출력된 숫자와 이전 숫자 크기 비교, 더 큰 숫자를 money에 저장
    # 탈출 조건 : 변환횟수 다 쓰면 탈출, 이미 만든 숫자배열이면 탈출
    # 가지치기 : 리스트를 set으로 바꿔서 중복제거하면 탐색 줄일 수 있음.

def dfs(cnt):
    global money
    if cnt == trans:
        money = max(money, int(''.join(nums))) #최댓값 갱신 
        return
    state = (cnt,"".join(nums))
    if state in visited:
        return
    visited.append(state)

    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            nums[i], nums[j] = nums[j], nums[i]
            dfs(cnt + 1)
            nums[i], nums[j] = nums[j], nums[i]


T = int(input())
for tc in range(T):
    nums, trans = input().split()
    nums = list(nums) # 숫자배열은 리스트로 변환
    trans = int(trans)
    money = 0 #최댓값 갱신해서 저장할 money변수
    visited = [] # 자리 교환한 nums 저장 
    dfs(0) 
    print(f'#{tc+1} {money}')