"""
정수 배열 nums가 주어졌을 때, i < j < k 이면서 nums[i] < nums[j] < nums[k]를 만족하는 
인덱스 세 쌍 (i, j, k)가 존재하면 true를 반환하고, 
존재하지 않으면 false를 반환하세요.

예시 1:

입력: nums = [1,2,3,4,5]

출력: true

설명: i < j < k인 모든 인덱스 세 쌍이 조건을 만족합니다.

입력: nums = [5,4,3,2,1]

출력: false

설명: 조건을 만족하는 세 쌍이 존재하지 않습니다.

#의사코드
1. 그러니까 i < j < k 랑 nums[i] nums[j] nums[k] 이걸 만족하는 세쌍이 필요.. 
2. 일단 쪼개서, i < j and nums[i] < nums[j] 이 조건을 찾고, 순서는 정해져있으니
3. j < k and nums[j] <nums[k]를 찾아보자.

근데 일단 min 값을 찾고, 그다음 min값 찾고. 이걸 해야하나. 
-> 기각. 가장 작은 값이 맨 뒤로 가 있으면 비효율적임.

걍 순차적으로 앞에서부터 탐색하는게 맞는것 같아. 순서는 정해져있으니까.

-> 이렇게 하니까 1,5,0,4,1,3 반례에 막힘.
 
2차 시도 -> 3중포문..

>class Solution(object):
    def increasingTriplet(self, nums):
        
        :type nums: List[int]
        :rtype: bool
        
        n = len(nums)

        for i in range(n):
            scd_idx = 0
            for j in range(i + 1,n): # 이렇게 돌리면 i<j 조건 성립함. 
                if nums[j] > nums[i]:
                    scd_idx = j
                    print(i,j, scd_idx)
                    for k in range(scd_idx + 1,n):
                        if nums[k] > nums[scd_idx]:
                                print("도달했나?")
                                return True
                                -> 이렇게 하니까 시간 초과 나옴. 최대 O(N^2)인듯

기각.
first,  second 값으로 하자. 전체 순회할 필요없이 
"""

nums = [1,5,0,4,1,3]



class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)

        first = float("inf")
        second = float("inf")

        for i in range(n):
            if nums[i] <= first:
                 first = nums[i]
            elif nums[i] <= second:
                 second = nums[i]
            else: # 이러면 index 조건도 만족하고, 값만 비교하면 되잖아. 
                 # 어차피 인덱스는 순차적으로 증가해서 비교 필요 x 값만.
                 # first , second 보다 크네??
                 return True
        return False

print(Solution().increasingTriplet(nums))