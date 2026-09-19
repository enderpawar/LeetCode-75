"""
1161. 이진 트리의 최대 레벨 합

난이도: Medium

이진 트리의 root가 주어졌을 때, 루트 노드의 레벨은 1, 루트의 자식 노드들의 레벨은 2이며, 그다음 레벨은 3과 같이 증가합니다.

각 레벨에 있는 모든 노드의 값을 합산했을 때, 합이 가장 큰 레벨 중 가장 작은 레벨 번호 x를 반환하세요.

예제 1

입력:

root = [1,7,0,7,-8,null,null]

출력:

2

설명:

레벨 1의 합 = 1

레벨 2의 합 = 7 + 0 = 7

레벨 3의 합 = 7 + (-8) = -1

따라서 노드 값의 합이 가장 큰 레벨은 2이므로 2를 반환합니다.

예제 2

입력:

root = [989,null,10250,98693,-89388,null,null,null,-32127]

출력:

2
제약 조건

트리의 노드 개수는 1 이상 10⁴ 이하입니다.

각 노드의 값은 -10⁵ 이상 10⁵ 이하입니다.

#의사코드
1순위 조건 : 레벨간 합이 제일 클 것 
2순위 조건 : 합이 같으면 레벨이 가장 낮은 걸 찾기
일단 이건 진짜 BFS이긴 하네. 근데 같은 레벨인걸 어떻게 알지
레벨 상승 조건을 좀 생각해봐야할것 같아.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque

class Solution:
    def maxLevelSum(self, root: TreeNode | None) -> int:

        max = float('-inf')
        level = 1
        queue = deque([root])
        max_lev = 0
        
        while queue: #이렇게 하면 매 레벨 별로 하게 되지 시작 레벨은 1.
            level_sum = 0

            for _ in range(len(queue)): # for문을 하나더 생성해서, 해당 레벨 안에서의 모든 것들은 해치우고 나가게 하자
                node = queue.popleft()
                level_sum += node.val


                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            
            if level_sum > max:
                max = level_sum
                max_lev = level

            level += 1 #

        return  max_lev
    
root = [1,7,0,7,-8,None,None]

print(Solution().maxLevelSum(root))