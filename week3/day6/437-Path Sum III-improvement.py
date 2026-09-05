"""
437. Path Sum III - 개선 버전 (prefix sum + 해시맵, O(n))

기존 풀이(preorder + dfs)는 트리의 모든 노드를 시작점으로 삼아 매번 아래로 다시
훑기 때문에 O(n^2)이 걸린다. prefix sum을 이용하면 각 노드를 한 번씩만 방문하면서
O(n)에 풀 수 있다.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


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


from typing import Optional


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # prefix_sums[s] = 루트에서부터 현재 경로 위에서, 누적합이 s인 지점이 몇 번 나왔는지 세는 카운터.
        # running_sum - targetSum이 이미 나온 적 있는 누적합이면,
        # 그 지점 바로 다음 노드부터 지금 노드까지의 구간 합이 targetSum이라는 뜻.
        prefix_sums = {0: 1}
        cnt = 0

        def dfs(node: Optional[TreeNode], running_sum: int):
            nonlocal cnt
            if node is None:
                return

            running_sum += node.val
            cnt += prefix_sums.get(running_sum - targetSum, 0)

            prefix_sums[running_sum] = prefix_sums.get(running_sum, 0) + 1
            dfs(node.left, running_sum)
            dfs(node.right, running_sum)
            # 이 노드의 서브트리 탐색이 끝났으니, 다른 가지에 영향 안 주도록 되돌려놓기
            prefix_sums[running_sum] -= 1

        dfs(root, 0)
        return cnt


root1 = build_tree([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1])
print(Solution().pathSum(root1, 8))  # 3

root2 = build_tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1])
print(Solution().pathSum(root2, 22))  # 3

root3 = build_tree([1, None, 2, None, 3, None, 4, None, 5])
print(Solution().pathSum(root3, 3))  # 2
