"""
236. Lowest Common Ancestor of a Binary Tree

비트마스크 상태
- 1: 현재 서브트리에서 p를 찾음
- 2: 현재 서브트리에서 q를 찾음
- 3: 현재 서브트리에서 p와 q를 모두 찾음
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(
        self,
        root: 'TreeNode',
        p: 'TreeNode',
        q: 'TreeNode',
    ) -> 'TreeNode':
        answer = None

        def dfs(node: 'TreeNode') -> int:
            nonlocal answer

            if node is None:
                return 0

            state = dfs(node.left) | dfs(node.right)

            if node is p:
                state |= 1
            if node is q:
                state |= 2

            if state == 3 and answer is None:
                answer = node

            return state

        dfs(root)
        return answer


root = TreeNode(3)
p = TreeNode(5)
q = TreeNode(1)
root.left = p
root.right = q

print(Solution().lowestCommonAncestor(root, p, q).val)
