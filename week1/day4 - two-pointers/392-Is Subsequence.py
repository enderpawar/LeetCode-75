"""
392 - Is Subsequence

부분 집합인가? 를 물어보는 문제. 
주어진 s 가 t의 부분 집합인지를 보면 됨.
s, t 는 오직 소문자로만 구성되니까 예외처리 x
"""

s = "abc"
t = "ahbgdc"

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool: 

        # two pointer 정의
        i = 0 
        j = 0
        result = False
        
        # s의 abc 순서는 지켜야하니까 상관 x
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1 
            j += 1
        # 이렇게 되면 i 다 돌면 나가짐.
        
        if i == len(s):
            result = True
        
        return result

print(Solution.isSubsequence(Solution,s,t))
