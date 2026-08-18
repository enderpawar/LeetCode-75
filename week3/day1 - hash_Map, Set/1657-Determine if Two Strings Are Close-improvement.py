"""
1657. 두 문자열이 가까운지 판별하기 - 개선 버전

원본 풀이는 dict와 get()으로 직접 빈도를 세고, count.keys()를 set으로 감싸서 비교했다.
이 버전은 세는 일을 Counter에 맡기고, 문자 종류는 문자열에서 바로 집합으로 만든다.
sorted된 빈도 목록이 같으면 두 문자열의 길이도 같으므로 길이 비교는 생략했다.

시간 복잡도: O(n)
공간 복잡도: O(1) (소문자 알파벳 26종으로 키 개수의 상한이 정해짐)
"""
from collections import Counter

word1 = "cabbba"
word2 = "abbccc"


class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        # 문자열 자체를 집합으로 만들면 등장하는 문자 종류를 바로 얻는다
        if set(word1) != set(word2):
            return False

        # 빈도 목록을 정렬해서 비교 (길이가 다르면 합이 달라 여기서 걸러진다)
        return sorted(Counter(word1).values()) == sorted(Counter(word2).values())


print(Solution().closeStrings(word1, word2))
