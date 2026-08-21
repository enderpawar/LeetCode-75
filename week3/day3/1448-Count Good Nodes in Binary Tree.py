"""
1448. 이진 트리에서 Good Node 개수 세기

이진 트리의 루트 노드 root가 주어진다.

트리의 어떤 노드 X가 good node가 되려면,

루트에서 X까지 가는 경로에 있는 노드들 중에서
X보다 큰 값을 가진 노드가 하나도 없어야 한다.

즉, 현재 노드의 값이 루트부터 지금까지 나온 값들의 최댓값 이상이면 good node라고 보면 돼.

good node의 총 개수를 반환하라.

예제 1
Input: root = [3,1,4,3,null,1,5]
Output: 4

설명:

루트 노드 3은 항상 good node
노드 4
경로: 3 → 4
4보다 큰 값이 없음 → good
노드 5
경로: 3 → 4 → 5
5보다 큰 값이 없음 → good
왼쪽 아래 노드 3
경로: 3 → 1 → 3
현재 값 3보다 큰 값이 없음 → good

따라서 총 4개.

예제 2
Input: root = [3,3,null,4,2]
Output: 3

노드 2의 경로는

3 → 3 → 2

인데, 앞에 3이 있고

3 > 2

이므로 2는 good node가 아니다.

따라서 정답은 3.

예제 3
Input: root = [1]
Output: 1

루트는 항상 good node이므로 정답은 1.

제약 조건
트리의 노드 개수: 1 ~ 10^5
각 노드의 값: -10^4 ~ 10^4

# 의사코드

- good Node? 현재 노드의 값이 루트부터 지금까지 나온 값들의 최댓값 이상이여야 한다.
 그니깐 지금까지 나온 경로들 중에 X보다 큰게 없어야함.
- 걍 Max = 최댓값 이런식으로 현재의 Good Node를 가지고 가면 되지 않을까?
- 그리고 gn_cnt를 따로 마련해서 현재까지 Good Node로 취급된 것들을 기록하면 되지.
"""
root = [3,1,4,3,None,1,5]

# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right


class Solution(object):
    

    def goodNodes(self, root):

        GN_cnt = 0

        def DFS(node, path_max):
            """
            :type root: TreeNode
            :rtype: int
            """
            if node is None :
                return 0
            
            crt_Node = node.val

            if node.val >= path_max:
                path_max = crt_Node
                nonlocal GN_cnt
                GN_cnt += 1

            if node.left is not None:
                 DFS(node.left,path_max) # 각 path_max로 넘겨줘야함. 각 경로별 지역 변수가 만들어져야함.
            if node.right is not None:
                 DFS(node.right,path_max)

        DFS(root,float('-inf'))

        return GN_cnt
            # 재귀 형식으로 DFS를 구현해보자.

            # 로직은 어렵지 않은데 파이썬에 익숙하지 않아서 시간 오래잡아먹었다...        
        