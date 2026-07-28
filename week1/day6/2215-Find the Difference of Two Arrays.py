"""
문제
0부터 시작하는 정수 배열 nums1과 nums2가 주어질 때, 크기가 2인 리스트 answer를 반환하세요.

answer[0]은 nums2에는 존재하지 않는 nums1의 모든 서로 다른(중복 없는) 정수 리스트입니다.

answer[1]은 nums1에는 존재하지 않는 nums2의 모든 서로 다른(중복 없는) 정수 리스트입니다.

참고: 리스트 안의 정수 순서는 자유롭게 반환해도 됩니다.

## 의사코드 -
- 걍 저기 뭐시기 not in 으로 검사하면 되지 않을까? 
- 예상 시간복잡도는 그럼 O(m x n) 인데..
- answer[i][0] = 1 


"""
from typing import List
nums1 = [1,2,3,3]
nums2 = [1,1,2,2]

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:

        answer = [[],[]] # answer은 2차원 배열로 만들어서 반환하자.

        cnt1 = 0 
        # answer[0]에는 nums1의 독립 리스트, answer[1]에는 nums2의 독립 리스트.

        for i in range(len(nums1)):        
           if nums1[i] not in nums2 and nums1[i] not in answer[0]:
                answer[0].append(nums1[i])
                # answer[0][cnt1] = nums1[i] -> 빈 리스트이므로 인덱스 접근하게 되면 out of range남. 따라서 동적 공간 할당 해주는 index로 해야됨.
                # cnt1 += 1

        cnt2 = 0

        temp2 = []

        for j in range(len(nums2)):
            if nums2[j] not in nums1 and nums2[j] not in answer[1]:
                answer[1].append(nums2[j])
                # answer[1][cnt2] = nums2[j]
                # cnt2 += 1


        return answer

print(Solution().findDifference(nums1,nums2))
