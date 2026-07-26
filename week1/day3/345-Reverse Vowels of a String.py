"""
345- vowel,

a e i o u 모음 뒤집기 문제임. 모음 위치들을 전부 뒤집으면 됨.
아마 중심 축을 기준으로 i e | e A 이 순이면 A e | e i 이렇게 될 것 같은데.

if str1[i] in str2이렇게 정의한다음에, 맞으면 해당 위치 tmp에 1로 비트마스킹 해놓음. 

그다음에 for 문 다시 돌려서 swap (str[i], str[n-i-1]) 이렇게 하면 될 것 같은데?
"""

class Solution:
    def reverseVowels(self, s: str) -> str:
        str2 = "aeiouAEIOU"
        loc = []

        res = list(s)

        for i in range (len(s)):
            if s[i] in str2:
                loc.append(i) # loc 에 위치 기억해놓기.

        for j in range (len(loc)//2):
            res[loc[j]], res[loc[-j-1]] = res[loc[-j-1]], res[loc[j]]

        return "".join(res)

# 헷갈렸던 문법 "".join - 배열 형태로 나눠졌던 문자열 합치기
#  "hello" → ["h", "e", "l", "l", "o"]