"""
1161. Maximum Level Sum of a Binary Tree

DFS로 각 깊이의 합을 누적한다.
재귀 깊이 제한을 피하기 위해 명시적인 스택을 사용한다.
"""


class Solution:
    def maxLevelSum(self, root: "TreeNode") -> int:
        level_sums = []
        stack = [(root, 0)]

        while stack:
            node, level = stack.pop()

            if level == len(level_sums):
                level_sums.append(node.val)
            else:
                level_sums[level] += node.val

            if node.right:
                stack.append((node.right, level + 1))
            if node.left:
                stack.append((node.left, level + 1))

        return level_sums.index(max(level_sums)) + 1


if __name__ == "__main__":
    import sys
    from pathlib import Path

    project_root = Path(__file__).resolve().parents[2]
    sys.path.append(str(project_root))

    from TreeNode import build_tree

    root = build_tree(
        [989, None, 10250, 98693, -89388, None, None, None, -32127]
    )
    print(Solution().maxLevelSum(root))
