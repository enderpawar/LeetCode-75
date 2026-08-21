# 394. Decode String - 개선 버전
# 스택 하나에 문자를 전부 쌓는 대신,
# "반복 횟수"와 "바깥에서 만들던 문자열"을 각각 따로 대피시키는 2-스택 풀이


class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """

        num_stack = []   # 아직 반복을 못 끝낸 k들
        str_stack = []   # 안쪽 구간을 처리하는 동안 대피시켜 둔 바깥 문자열
        cur = ""         # 지금 만들고 있는 문자열
        num = 0          # 지금 읽고 있는 숫자

        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)

            elif char == '[':
                num_stack.append(num)
                str_stack.append(cur)
                num = 0
                cur = ""

            elif char == ']':
                cur = str_stack.pop() + cur * num_stack.pop()

            else:
                cur += char

        return cur


if __name__ == "__main__":
    solution = Solution()

    print(solution.decodeString("3[a]2[bc]"))      # aaabcbc
    print(solution.decodeString("3[a2[c]]"))       # accaccacc
    print(solution.decodeString("2[abc]3[cd]ef"))  # abcabccdcdcdef
    print(solution.decodeString("abc"))            # abc
    print(solution.decodeString("10[a]"))          # aaaaaaaaaa
    print(solution.decodeString("2[a3[b]c]"))      # abbbcabbbc
