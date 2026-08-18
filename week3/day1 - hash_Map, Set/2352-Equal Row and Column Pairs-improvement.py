"""
2352. 같은 행과 열 쌍의 개수 - 개선 버전

원본 풀이는 dict와 get()으로 행의 등장 횟수를 직접 세고, 답을 반복문 안에서 누적했다.
이 버전은 Counter로 행을 세고, 열마다 조회한 값을 sum으로 한 번에 더한다.
Counter는 없는 키를 조회해도 KeyError 대신 0을 돌려주므로 기본값을 따로 넘기지 않아도 된다.

시간 복잡도: O(n^2)
공간 복잡도: O(n^2)
"""
from collections import Counter

grid = [
    [3, 1, 2, 2],
    [1, 4, 4, 5],
    [2, 4, 2, 2],
    [2, 4, 2, 2],
]


class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # 각 행을 튜플로 바꿔 등장 횟수를 센다
        row_count = Counter(tuple(row) for row in grid)

        # zip(*grid)가 돌려주는 각 열은 이미 튜플이므로 그대로 조회한다
        return sum(row_count[column] for column in zip(*grid))


print(Solution().equalPairs(grid))
