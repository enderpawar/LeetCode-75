"""
199. 이진 트리의 오른쪽 모습 (Binary Tree Right Side View)

난이도: Medium

이진 트리의 root가 주어집니다.

여러분이 이 트리의 오른쪽에 서서 트리를 바라보고 있다고 상상해보세요.

이때 오른쪽에서 보이는 노드들의 값을 위에서 아래 순서대로 반환하세요.

예제 1
입력: root = [1,2,3,null,5,null,4]

출력: [1,3,4]

설명:
오른쪽에서 트리를 바라보면 1 → 3 → 4가 보입니다.

예제 2
입력: root = [1,2,3,4,null,null,null,5]

출력: [1,3,4,5]
예제 3
입력: root = [1,null,3]

출력: [1,3]
예제 4
입력: root = []

출력: []
제한사항
트리의 노드 개수는 0 ~ 100개입니다.
-100 <= Node.val <= 100

쉽게 말하면, 트리의 각 깊이(level)에서 가장 오른쪽에 있는 노드를 하나씩 뽑으면 됩니다.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque
from typing import Optional, List


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
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        result = []
        queue = deque([root])

        while queue: # 큐에 노드가 남아있는한 계속 실행
            level_size = len(queue)

            for i in range(level_size): # 현재 레벨 사이즈 만큼 순회. 이러면 맨 마지막 노드가 그거가 되겠지.
                node = queue.popleft()

                if i == level_size - 1:  #노드 인덱스가 마지막 인덱스 (최우측 노드) 라면?
                    result.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

        return result
            
root = build_tree([1, 2, 3, None, 5, None, 4])
print(Solution().rightSideView(root))

    