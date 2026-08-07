"""
1456. 주어진 길이의 부분 문자열에서 모음의 최대 개수 - 개선 버전

원본 풀이는 deque에 윈도우 글자를 그대로 복사해서 들고 있었다.
이 버전은 s를 인덱스로 직접 참조해서 왼쪽/오른쪽 글자만 확인한다.

시간 복잡도: O(n)
공간 복잡도: O(1) (원본은 O(k))
"""
s = "abciiidef"
k = 3


class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        vowels = set("aeiou")

        vowel_num = sum(1 for ch in s[:k] if ch in vowels)
        max_vowel = vowel_num

        for right in range(k, len(s)):
            if s[right] in vowels:
                vowel_num += 1
            if s[right - k] in vowels:
                vowel_num -= 1

            max_vowel = max(max_vowel, vowel_num)

        return max_vowel


print(Solution().maxVowels(s, k))
