"""
더 개선한 버전: nonlocal로 바깥 변수를 직접 바꾸는 대신,
각 재귀 호출이 자기 서브트리의 good node 개수를 return으로 위로 올려보낸다.
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def DFS(node, path_max):
            if node is None:
                return 0

            count = 1 if node.val >= path_max else 0
            path_max = max(path_max, node.val)

            return count + DFS(node.left, path_max) + DFS(node.right, path_max)

        return DFS(root, float('-inf'))


# 예제 1: root = [3,1,4,3,null,1,5] -> 4
root = TreeNode(3,
                 TreeNode(1, TreeNode(3), None),
                 TreeNode(4, TreeNode(1), TreeNode(5)))

print(Solution().goodNodes(root))
