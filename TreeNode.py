"""이진 트리 문제에서 재사용할 TreeNode와 레벨 순서 builder."""

from collections import deque
from typing import Iterable, Optional


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ):
        self.val = val
        self.left = left
        self.right = right


def build_tree(values: Iterable[Optional[int]]) -> Optional[TreeNode]:
    """LeetCode의 레벨 순서 배열을 이진 트리로 변환한다."""
    values = list(values)
    if not values or values[0] is None:
        return None

    root = TreeNode(values[0])
    queue = deque([root])
    index = 1

    while queue and index < len(values):
        node = queue.popleft()

        left_value = values[index]
        index += 1
        if left_value is not None:
            node.left = TreeNode(left_value)
            queue.append(node.left)

        if index >= len(values):
            break

        right_value = values[index]
        index += 1
        if right_value is not None:
            node.right = TreeNode(right_value)
            queue.append(node.right)

    return root
