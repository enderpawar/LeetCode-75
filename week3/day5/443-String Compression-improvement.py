# 443. String Compression - 개선 버전
# 직접 read/write 포인터를 옮기는 대신,
# itertools.groupby로 "연속된 같은 문자 묶음"을 바로 얻어와 반복한다.

from itertools import groupby


class Solution:
    def compress(self, chars):
        write = 0

        for char, group in groupby(chars):
            char_cnt = sum(1 for _ in group)

            chars[write] = char
            write += 1

            if char_cnt > 1:
                for digit in str(char_cnt):
                    chars[write] = digit
                    write += 1

        return write


if __name__ == "__main__":
    solution = Solution()

    chars1 = ["a", "a", "b", "b", "c", "c", "c"]
    n1 = solution.compress(chars1)
    print(n1, chars1[:n1])  # 6 ['a', '2', 'b', '2', 'c', '3']

    chars2 = ["a"]
    n2 = solution.compress(chars2)
    print(n2, chars2[:n2])  # 1 ['a']

    chars3 = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
    n3 = solution.compress(chars3)
    print(n3, chars3[:n3])  # 4 ['a', 'b', '1', '2']
