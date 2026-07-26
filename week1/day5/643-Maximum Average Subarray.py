"""
643. 최대 평균 부분배열 I (쉬움)
n개의 원소로 이루어진 정수 배열 nums와 정수 $k$가 주어집니다.
길이가 $k$인 연속된 부분 배열 중 평균값이 가장 큰 것을 찾아 그 값을 반환하세요. 
계산 오차가 $10^{-5}$ 미만인 답은 정답으로 인정됩니다.
"""
from typing import List

nums = [1,12,-5,-6,50,3]
k = 4

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        max = float("-inf")

        for i in range (len(nums)-k+1):

            for j in range(k,len(nums)):
                
                sum1+=nums[j] 

            avg= sum1 / k
            print(i,avg)

            if(max < avg):
                max = avg
                

        return max
        

print(Solution().findMaxAverage(nums,k))

"""

list slicing : result = sum(numbers[1:4]) 식으로 사용할 수 있다.  그럼 1~3까지 더하게 되는거임.
"""