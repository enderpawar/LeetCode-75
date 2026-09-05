"""
199. Binary Tree Right Side View - DFS(오른쪽 우선 방문) 버전

BFS로 큐에 레벨 전체를 담아두는 대신, 오른쪽 자식을 먼저 방문하는 DFS로 풀면
각 깊이에서 "가장 먼저 도착한 노드"가 곧 오른쪽에서 보이는 노드가 된다.
"""
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(values):
    if not values or values[0] is None:
        return None

    from collections import deque

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
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def dfs(node, depth):
            if node is None:
                return

            if depth == len(result):
                result.append(node.val)

            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)

        dfs(root, 0)
        return result


root = build_tree([1, 2, 3, None, 5, None, 4])
print(Solution().rightSideView(root))

root2 = build_tree([1, 2, 3, 4, None, None, None, 5])
print(Solution().rightSideView(root2))
