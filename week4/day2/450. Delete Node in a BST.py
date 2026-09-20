"""
450. 이진 탐색 트리에서 노드 삭제

Medium 이진 탐색 트리

이진 탐색 트리(BST)의 루트 노드 root와 정수 key가 주어집니다.

BST에서 값이 key인 노드를 삭제하고, 삭제 후의 BST의 루트 노드 참조(변경되었을 수 있음) 를 반환하세요.

노드 삭제 과정은 기본적으로 다음 두 단계로 나눌 수 있습니다.

삭제할 노드를 탐색합니다.

해당 노드를 찾았다면 삭제합니다.

# 의사코드 

- 일단 BST니까 왼쪽 자식 노드가 무조건 작아야함.
- key를 기준으로, DFS로 하는게 더 나을것 같은데? 
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deleteNode(self, root: TreeNode | None, key: int) -> TreeNode | None:

        def dfs(node, key):
            if node is None:
                return  
            
            if key < node.val: # 부모 노드보다 key가 작으면 왼쪽 노드 탐색
                node.left = dfs(node.left, key)

            if key > node.val: # 이하 동문
                node.right = dfs(node.right, key)

            if key == node.val: # 여기가 이제 핵심인데..node = node.left or right로 처리하고 
                if node.left is None:
                    return node.right

                # 2. 오른쪽 자식이 없는 경우
                if node.right is None:
                    return node.left

                # 3. 자식이 둘 다 있는 경우
                # 오른쪽 서브트리에서 가장 작은 노드 찾기
                successor = node.right

                while successor.left:
                    successor = successor.left

                # 현재 노드의 값을 후계자 값으로 변경
                node.val = successor.val

                # 기존 후계자 노드 삭제
                node.right = dfs(node.right, successor.val)

            return node
        
        return dfs(root,key)