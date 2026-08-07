"""
문제 설명

단방향 연결 리스트(Singly Linked List)의 헤드 노드가 주어졌을 때, 
리스트의 연결 순서를 뒤집고(반전시키고), 뒤집힌 리스트의 헤드 노드를 반환하는 문제입니다.

예시 분석

예시 1:
입력: head = [1,2,3,4,5]
출력: [5,4,3,2,1]

설명: 1 -> 2 -> 3 -> 4 -> 5 형태의 연결 리스트를 뒤집어 5 -> 4 -> 3 -> 2 -> 1 형태로 만듭니다.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            
        return prev 