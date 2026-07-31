# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


"""
각 leaf가 같은지 른지 판단하는 문제인데..
재귀 탐색으로 하면 될것 같은데..
"""


# class Solution:
    
#     def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

#         if root1.left 
#             self.leafSimilar(root1.left,root2)
#         if root1.right :
#             self.leafSimilar(root1.right,root2)
#         else: 
#             leaf1.append(root1.val)
            
#         if root2.left is None and root2.right is None:
#             self.leafSimilar(root1,root2.left)
#             self.leafSimilar(root1,root2.right)
#         else:
#             leaf2.append(root2.val)

#         if(leaf1 == leaf2):
#             return True
#         else:
#             return False        
"""
이렇게 하면 안되고, 별도 DFS를 정의해서 해줘야해. 첫 시도는 그냥 root1이든 root2든 동결시켜서 계속 호출해보자 이거였는데 
이 경우에는 만약 root1 이나 root가 레벨이 1이라면 [2,3,2,3...] 이런식으로 쌓일 수가 있음. 그래서 별도 dfs가 정의되어야한다.
"""


class Solution(object):
    def leafSimilar(self, root1, root2):
        leaf1 = []
        leaf2 = []
        def dfs(self, leaf_list, root):
            if root.left is None and root.right is None:
                leaf_list.append(root.val)
            else:
                if root.left:
                    dfs(leaf_list,root.left) #dfs는 클래스의 메서드가 아니라 leafSimilar의 내부 함수 이므로 self 가 필요없다.
                if root.right:
                    dfs(leaf_list,root.right)
        dfs(leaf1,root1)
        dfs(leaf2,root2)
        return leaf1 == leaf2