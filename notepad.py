# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# root = [3,9,20,null,null,15,7]

# class Solution:
#     def maxDepth(self, root: Optional[TreeNode]) -> int:

#         depth = 0
#         n = 0

#         while len(root) >= (2**n-1): # 파이썬에서는 ^가 거듭제곱이 아니다..!
#             depth+=1
#             n+=1
        
            
"""
너무 쉽잖아. 그냥 len(root) 배열의 길이만큼 해놓고 

각 레벨별로 가질 수 있는 노드의 개수 2^n -1 하면되는건데 뭘. 
--> 라는건 꿈이였고, TreeNode 형태라 안됨. 재귀 탐색하면서 if left, right 노드가 있으면 
depth + 1 해주는 식으로 구현해보자.
""" 


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
      def maxDepth(self, root: Optional[TreeNode]) -> int:
          if root is None:
              return 0

          return 1 + max(
              self.maxDepth(root.left),
              self.maxDepth(root.right)
          )
