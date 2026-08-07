"""
151. Reverse Words in a String
이걸 한 문자 단위로 어떻게 인식하게 하지?
s.split을 사용 시 단어 단위로 분리 가능. 그리고 걍 swap 해서 뒤집으면 되겠네. 그렇게 words[::-1]
"""

class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        res = " ".join(words[::-1])

        return res