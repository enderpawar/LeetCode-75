"""
2215. Find the Difference of Two Arrays

set의 차집합을 이용한 O(n + m) 풀이.
각 배열의 중복을 제거하고, 상대 배열에 없는 원소만 구한다.

시간복잡도: O(n + m)
공간복잡도: O(n + m)
"""

from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = set(nums1)
        set2 = set(nums2)

        return [list(set1 - set2), list(set2 - set1)]

