"""
1004. 연속된 1의 최대 개수 III

이진 배열 nums와 정수 k가 주어진다.

배열 안의 0을 최대 k개까지 1로 뒤집을 수 있을 때, 만들 수 있는 가장 긴 연속된 1의 길이를 반환하라.

즉,

0 -> 1 변경을 최대 k번까지 가능
그 결과 얻을 수 있는 가장 긴 연속 1 구간의 길이를 구하면 됨
예제 1
Input:
nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2

Output:
6

설명:

0 두 개를 1로 바꾸면 예를 들어

[1,1,1,0,0,1,1,1,1,1,1]

처럼 만들 수 있고, 이때 연속된 1이 최대 6개까지 이어진다.

따라서 정답은:

6

예제 2
Input:
nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
k = 3

Output:
10

# 의사코드

1. 먼저 각 구간별로 1이 몇개씩 있는지 확인
2. 먼저 0이 위치한 인덱스만 따로 빼놓고 슬라이딩 윈도우로 k개씩 밀면서 해당 위치에 있는 것들을 뒤집기.
3. 그다음에 0 양끝점끼리 인덱스를 빼면 되겠네. 

-->> 로직 이 잘못됐어. 
[0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
[0,0,1,1,/1,1/,1,1,1,/1/,1,1,0,0,0,1,1,1,1] 이렇게 된 경우, 즉 좌우에 11이 추가로 있는 경우 그 1까지 더해줘야해.

얘처럼 
"""
nums = [0,0,0,1]
k = 4

class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        zero_idx = []

        for i in range(len(nums)):
            if nums[i] == 0:
                zero_idx.append(i)

        # print(zero_idx) #테스트용 
        # #이렇게 zero_idx 위치 전부 구하고,

        if len(zero_idx) <= k: # [0,0,0,1] 일 경우 예외처리 해줘야함. 즉 k보다 zero_idx의 길이가 적을경우 걍 nums의 길이임.
            return len(nums)
        
        start_pnt = 0
        end_pnt = k

        max_len = 0

        while end_pnt <= len(zero_idx):

            if start_pnt == 0: 
                left_zero = -1
            else:
                left_zero = zero_idx[start_pnt - 1]

            if end_pnt == len(zero_idx):
                right_zero = len(nums)
            else:
                right_zero = zero_idx[end_pnt]

            crt_len = right_zero - left_zero -1

            max_len = max(max_len,crt_len)

            start_pnt += 1
            end_pnt +=1

            #여기에 if zero_idx[start_pnt - 1] == zero_idx[start_pnt] -1 이라면 for문 돌려서 최 좌측점 찾고,  
            # 우측도 그렇게 찾는걸 해볼까? 아냐아냐 그렇게하면 O(N^2)가 된다. 
            # 잠만. 근데 애초에 zero_idx 간에는 무조건 1이 차있는거잖아. 그럼 굳이 탐색하지 않아도 start_pnt-1과 end_pnt+1 간의 거리를 구하고 -1을 해주면 되지
            # print("현재 길이")
            # print(crt_len)
        
            # print("최대 길이")
            # print(max_len)
           

        return max_len 

print(Solution().longestOnes(nums,k))