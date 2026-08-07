"""
BST 타입인 root 와 int val 이 주어진다.
val과 똑같은 value를 가진 노드를 출력 및 그 서브트리 출력하기. 

# 의사코드

1. 한 코드에 대해서 DFS를 수행해야할 것 같은데? 재귀 호출 식으로 if root.left / root right 면  거기로 가서 탐색하며 result에 넣으면 될듯
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
        
    result = []

    def searchBST(self, root, val):

        if root is None:
            return None

        if root.val == val: # 탐색을 이어가되 val 을 루트로 하는 서브 트리를 또 만들어야함.
            return root
             # 아아아아ㅏㅏ List 형태로 반환하는게 아니라 그냥 root를 반환하면 되는거였구나 헷갈렸다..

        if val < root.val:
            return self.searchBST(root.left,val)
        else:
            return self.searchBST(root.right,val)

#   현재 코드처럼 작성하면 안 되는 이유는:

#   self.searchBST(root.left, val)
#   self.searchBST(root.right, val)

#   재귀 호출이 찾은 노드를 반환해도 그 반환값을 저장하거나 다시 return하지 않아 사라지기 때문입니다.
        
