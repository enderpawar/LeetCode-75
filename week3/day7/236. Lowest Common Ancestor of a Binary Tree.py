"""
236. 이진 트리의 최소 공통 조상

이진 트리가 주어졌을 때, 트리 안의 두 노드 p, q의 최소 공통 조상(LCA, Lowest Common Ancestor) 을 찾으세요.

Wikipedia의 정의에 따르면 최소 공통 조상은 다음과 같습니다.

두 노드 p와 q를 모두 자손으로 가지는 노드 중에서 가장 아래에 있는 노드

여기서 노드는 자기 자신의 자손으로도 간주할 수 있습니다.

예제 1
입력:
root = [3,5,1,6,2,0,8,null,null,7,4]
p = 5
q = 1

출력:
3

설명:
노드 5와 1의 최소 공통 조상은 3입니다.

예제 2
입력:
root = [3,5,1,6,2,0,8,null,null,7,4]
p = 5
q = 4

출력:
5

설명:
노드 5와 4의 최소 공통 조상은 5입니다.

LCA의 정의에서는 노드 자신도 자신의 자손으로 간주할 수 있기 때문입니다.

즉, 5는 자기 자신인 5와 자신의 아래에 있는 4를 모두 포함하므로 최소 공통 조상이 됩니다.

예제 3
입력:
root = [1,2]
p = 1
q = 2

출력:
1

여기서도 1은 자기 자신인 p와 자식 노드인 2를 모두 포함하므로 최소 공통 조상은 1입니다.

# 의사코드

1.DFS로 풀되, 자식 하나만 검증이 아니라 왼쪽 서브 트리, 오른쪽 서브트리에 그게 있는지 살펴봐야할것 같은데?
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        # left, right로 놓고 탐색 다 되면 null로 둘까?
        # complete_state? 이거로 완료 여부 표시해야하나 complete 



        def dfs(node : 'TreeNode'):
            if node is None:
                return None

            left = dfs(node.left)
            right = dfs(node.right) # 서브트리에서 p or q를 찾으면 그 노드가 들어옴

            if left and right: # left, right 했는데 더 나은게 있다?
                return node

            if node == p or node == q:
                return node

            return left or right

        return dfs(root)

root = TreeNode(3)
p = TreeNode(5)
q = TreeNode(1)
root.left = p
root.right = q

print(Solution().lowestCommonAncestor(root, p, q).val)
