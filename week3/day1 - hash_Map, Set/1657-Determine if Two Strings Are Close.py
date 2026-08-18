"""
1657. 두 문자열이 가까운지 판별하기

두 문자열에 아래 연산을 적용해서 한 문자열을 다른 문자열로 만들 수 있다면, 두 문자열은 가까운(close) 문자열이라고 한다.

연산 1: 문자 위치 바꾸기

문자열에 이미 존재하는 문자 두 개의 위치를 서로 바꿀 수 있다.

예:

abcde → aecdb
연산 2: 두 문자 전체를 서로 교환하기

문자열에 이미 존재하는 서로 다른 두 문자를 선택한 뒤, 한 문자의 모든 등장 위치를 다른 문자로 바꾸고, 다른 문자의 모든 등장 위치도 첫 번째 문자로 바꿀 수 있다.

예:

aacabb → bbcbaa

이 연산에서는:

모든 a → b
모든 b → a

로 동시에 변경된다.

각 문자열에 위 연산들을 원하는 만큼 적용할 수 있다.

문자열 word1과 word2가 주어질 때, 두 문자열이 가까운 문자열이면 true, 그렇지 않으면 false를 반환하라.

예제 1
입력: word1 = "abc", word2 = "bca"
출력: true

설명:

연산 1을 두 번 적용하면 word1을 word2로 만들 수 있다.

"abc" → "acb"
"acb" → "bca"
예제 2
입력: word1 = "a", word2 = "aa"
출력: false

# 의사코드

- 굳이 연산 1 2 를 다 수행할 필요는 없이 해쉬맵으로 a , b, c...를 키로하고 value를 등장횟수로 기록하고 그게 같은지 비교하면 될듯? 어차피 같은 리소스 내에서 순서만 바꾸는 거잖아.
- 
"""

class Solution:
    def closeStrings(self, word1, word2):
        # 길이가 다르면 어떤 연산으로도 같게 만들 수 없음
        if len(word1) != len(word2):
            return False

        count1 = {}
        count2 = {}

        # word1의 문자별 등장 횟수 계산
        for char in word1:
            count1[char] = count1.get(char, 0) + 1

        # word2의 문자별 등장 횟수 계산
        for char in word2:
            count2[char] = count2.get(char, 0) + 1

        # 두 문자열에 존재하는 문자 종류가 다르면 불가능
        if set(count1.keys()) != set(count2.keys()): # Python2에서는 리스트를 반환해서 순서까지 비교한다!!! 그래서 set을 해줘야함... 이거 틀림
            return False

        # 문자별 등장 횟수의 구성이 같은지 확인
        freq1 = sorted(count1.values())
        freq2 = sorted(count2.values())

        return freq1 == freq2
