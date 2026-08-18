# 2390. Removing Stars From a String - 개선 버전
# 스택 대신 오른쪽에서 왼쪽으로 훑으며 "밀린 별 개수"만 세는 풀이


class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """

        result = []
        stars = 0

        for char in reversed(s):
            if char == '*':
                stars += 1

            elif stars:
                stars -= 1

            else:
                result.append(char)

        result.reverse()

        return ''.join(result)


if __name__ == "__main__":
    solution = Solution()

    print(solution.removeStars("leet**cod*e"))  # lecoe
    print(solution.removeStars("erase*****"))   # (빈 문자열)
    print(solution.removeStars("ab*c"))         # ac
    print(solution.removeStars("a*"))           # (빈 문자열)
    print(solution.removeStars("abc"))          # abc
