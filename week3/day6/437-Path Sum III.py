"""
이진 트리의 root와 정수 targetSum이 주어졌을 때, 경로를 따라 있는 노드 값들의 합이 
targetSum이 되는 경로의 개수를 반환하세요.

경로는 루트에서 시작하거나 리프 노드에서 끝날 필요는 없습니다. 
하지만 반드시 아래 방향으로만, 즉 부모 노드에서 자식 노드 방향으로 이동해야 합니다.

예시 1:

입력: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
출력: 3

설명: 합이 8이 되는 경로는 총 3개입니다.

예시 2:

입력: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
출력: 3

# 의사코드

그러니까 한 루트 노드 -> 하위 루트 노드까지 가는 경로 중 노드를 전부 더했을때 target Sum까지
가는 경우 수를 구해라 이건데.

return cnt를 하고, 재귀형식으로 구현하되 if crt_sum이 targetSum과 같아지면 
탐색을 멈추...면 안되지. 만약 -2 +4 와 같은 경우가 나오면 어떡할거야. 멈추지 말고 조용히 cnt를 올리자 

근데 가장 고민되는건 이거야. 루트 -> 하단 경로 / 하위 leaf node-> 그 하위 leaf Node를 나눠야하는데

어떻게 하지? crt_sum == target_sum 인지 비교하기 위해선 N 크기 공간할당을해서 인덱스별로 하게끔 해야하나
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional

from collections import deque

def build_tree(values):
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while queue and i < len(values):
        node = queue.popleft()
        if i < len(values):
            if values[i] is not None:
                node.left = TreeNode(values[i])
                queue.append(node.left)
            i += 1
        if i < len(values):
            if values[i] is not None:
                node.right = TreeNode(values[i])
                queue.append(node.right)
            i += 1
    return root

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        cnt = 0

        # node를 시작점으로 고정하고, 거기서부터 아래로 내려가며 합을 누적.
        # "여기서 새로 시작"이라는 개념이 없어서, 예전처럼 중복으로 세는 일이 없음.
        def dfs(node: Optional[TreeNode], sum: int):
            nonlocal cnt
            if node is None:
                return

            sum += node.val

            if sum == targetSum:
                cnt += 1

            dfs(node.left, sum)
            dfs(node.right, sum)

        # 트리의 모든 노드를 한 번씩 방문하면서, 각 노드를 시작점 삼아 dfs를 새로 돌림.
        def preorder(node: Optional[TreeNode]):
            if node is None:
                return

            dfs(node, 0)
            preorder(node.left)
            preorder(node.right)

        preorder(root)

        return cnt


root1 = build_tree([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1])
print(Solution().pathSum(root1, 8))  # 3

root2 = build_tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1])
print(Solution().pathSum(root2, 22))  # 3

root3 = build_tree([1, None, 2, None, 3, None, 4, None, 5])
print(Solution().pathSum(root3, 3))  # 2
