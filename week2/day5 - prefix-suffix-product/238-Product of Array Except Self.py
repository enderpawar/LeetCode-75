"""
# [문제] 자신을 제외한 배열의 곱 (Product of Array Except Self)
#
# 정수 배열 nums가 주어졌을 때, answer[i]가 nums[i]를 제외한
# 나머지 모든 요소의 곱과 같아지도록 하는 배열 answer를 반환합니다.
Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

-> 그러니까 ans x nums 했을때 값들이 전부 같아지도록 하라. 이거인데...

You must write an algorithm that runs in O(n) time and without using the division operation.

# 의사코드
어떻게 하지?? 원래 n만큼 포문 돌려서 -30~30까지 for문 반복하면서 큰 수를 나눠가며 구하려고 했는데 이건 또 안되고..
큰수를 곱해가며 O(N X M) 하려했는데 10^5까지 nums.length라 못해..

아 규칙 발견 남은 수를 전부 곱하면 되네!! i 를 제외한 확인했어. 2*3*4 = 24 1*3*4 = 12

근데 나머지 수들을 전체 다 곱하려면 직관적으로는 O(N^2) 가 듬. continue로 넘기려고 해도..

나눗셈이 되면 max 한다음에 그걸 나누면 되는데.

누적곱? 그러니까 인덱스 i의 누적곱을 구할까? 공간복잡도는 상관없으니까. 

left right 나눠서. 단일 포문 두개로.
그니까 영역을 굳이 나누려고 하면 for i 이중 탐색되서 for(N^2)이 되니까. 일단 i부터 누적곱을 다 채우고, 
"""
nums = [1,2,3,4]

class Solution(object):
    def productExceptSelf(self, nums):
        n = len(nums)
        answer = [1]*n

        left = 1
        for i in range(n):
            answer[i] = left # 그 값은 answer[i]의 좌측이 되잖아
            left *= nums[i] # 1. nums[i]의 값을 left에 넣어주면 

        right = 1
        for j in range(n - 1, -1, -1): #이렇게하면 역순회 함
            answer[j] *= right
            right *= nums[j]

        return answer

print(Solution().productExceptSelf(nums))

#근데 여기서 공간복잡도 1로 하는건 어떻게 하는지 알아봐야할듯. 