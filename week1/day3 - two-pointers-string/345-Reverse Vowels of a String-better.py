"""
345. Reverse Vowels of a String

LeetCode에서 이 문제의 주제로 제시한 Two Pointers 방식을 참고한 더 나은 풀이.
왼쪽과 오른쪽에서 모음을 하나씩 찾아 바로 교환한다.

출처:
https://leetcode.com/problems/reverse-vowels-of-a-string/
"""


class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        res = list(s)

        left = 0
        right = len(res) - 1

        while left < right:
            while left < right and res[left] not in vowels:
                left += 1

            while left < right and res[right] not in vowels:
                right -= 1

            res[left], res[right] = res[right], res[left]

            left += 1
            right -= 1

        return "".join(res)

