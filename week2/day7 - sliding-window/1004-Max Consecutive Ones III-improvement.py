"""
1004. 연속된 1의 최대 개수 III - 개선 버전

원본 풀이는 0의 위치를 zero_idx 배열에 따로 모아두고 그 위에서 슬라이딩했다.
이 버전은 별도 배열 없이 nums 위에서 두 포인터로 직접 윈도우를 유지한다.

시간 복잡도: O(n)
공간 복잡도: O(1) (원본은 O(n))
"""
nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
k = 2


class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left = 0
        zeros = 0
        max_len = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1

            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len


print(Solution().longestOnes(nums, k))
