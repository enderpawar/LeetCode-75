"""
1456. 주어진 길이의 부분 문자열에서 모음의 최대 개수

문자열 s와 정수 k가 주어진다.

s에서 길이가 정확히 k인 모든 부분 문자열(substring) 중, 포함된 모음( ㅏ ㅔ ㅣ ㅗ ㅜ )의 개수가 가장 많은 경우의 모음 개수를 반환하라.

영어에서 모음은 다음 5개다.

'a', 'e', 'i', 'o', 'u'
예제 1
입력:
s = "abciiidef"
k = 3

출력:
3

설명:

길이가 3인 부분 문자열 중 "iii"에는 모음이 3개 들어 있다.

따라서 정답은 3.

예제 2
입력:
s = "aeiou"
k = 2

출력:
2

설명:

길이가 2인 어떤 부분 문자열을 골라도 모음이 2개 들어 있다.

따라서 정답은 2.


#의사코드
- sliding window 방식으로 윈도우(커널 사이즈)를 k로 해놓고 for 문 돌려서 전체 탐색하면 되지 않을까. 
-> 안돼. 이번에도 s.length가 10^5 여서 n^2  때리면 100억이 된다. 따라서 정석 슬라이딩 윈도우 방식으로 해야햏.

- 정석 슬라이딩 윈도우 방식이 무엇이냐? 처음에만 내부 k 전체 탐색하고 진짜 인덱스를 이동시키는게 아니라, deque를 써서 popleft 로 왼쪽꺼 뺴고 pop right로 오른쪽 뺴기 이런식으로 가야해
"""
from collections import deque

s = "abciiidef"
k = 3

class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        window = deque(s[0:k])
        vowel_num = 0
        

        end_point = k-1

        for i in range(k):
            if window[i] in "aeiou":
                vowel_num += 1

        max_vowel = vowel_num
        
        while end_point < len(s) - 1:

            if window[0] in "aeiou":
                vowel_num -= 1

            window.popleft()
            window.append(s[end_point + 1])

            if s[end_point+1] in "aeiou":
                vowel_num += 1 

            max_vowel = max(vowel_num,max_vowel)

            end_point +=1

            
        return max_vowel

print(Solution().maxVowels(s,k))

            





        