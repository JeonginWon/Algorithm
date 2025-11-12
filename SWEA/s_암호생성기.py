# 암호생성기
T = 10
for tc in range(T):
    tc = int(input())
    nums = list(map(int, input().split()))
    
    # 리스트의 앞부분 감소
    for n in range(8):
        for i in range(1,6):
            move = nums[0] - i
    # 감소한 원소값 뒤로 인덱스 이동
            for j in range(7):
                nums[j] = nums[j+1]
                nums[7] = move
    print(nums)

T = 10
# 필요데이터
for test_case in range(1, T+1):
    N = input()
    nums = list(map(int, input().split()))
    #덱
    boolean = True
    temp_number = 0 # 1~5 빼고 이동할 숫자 따로 저장 (인덱스 할당 대비)
    while boolean:
        for i in range(5):
            temp_number = nums[0] - (i+1) #1~5 빼기
            for j in range(1,8):
                nums[j-1] = nums[j] # 한칸씩 앞으로 이동
            nums[7] = temp_number # temp_number 뒤로 이동
            if nums[7] <= 0: # 0 이면 멈춤
                nums[7] = 0
                boolean = False
                break     
    print(f'#{test_case}', *nums)