"""
이건 걍 너무 쉽잖아 XOR 연산 때리면 됨
"""

class Solution(object):

    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        for num in nums:
            ans ^= num
        return ans