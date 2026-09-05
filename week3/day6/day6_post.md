[LeetCode 75 Day 20] 199. Binary Tree Right Side View

이번 문제는 트리를 레벨 단위로 순회하는 BFS를 다시 연습하는 문제였다. 이전에 풀었던 트리 문제들이 대부분 DFS 위주였다면, 이 문제는 "각 깊이에서 가장 오른쪽 노드만 뽑는다"는 조건 때문에 레벨 단위로 큐를 끊어서 처리하는 패턴을 제대로 이해하고 넘어가야 했다.

## 1. Binary Tree Right Side View - 레벨별 BFS로 오른쪽 끝 노드 뽑기

트리의 root가 주어질 때, 트리를 오른쪽에서 바라봤을 때 보이는 노드들의 값을 위에서 아래 순서로 반환하는 문제다. 즉 각 깊이(level)마다 가장 오른쪽에 있는 노드 하나씩을 모으면 된다.

```python
from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        result = []
        queue = deque([root])

        while queue:
            level_size = len(queue)

            for i in range(level_size):
                node = queue.popleft()

                if i == level_size - 1:
                    result.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

        return result
```

핵심은 큐에 "현재 레벨의 노드 개수"를 미리 `level_size`로 고정해두고, 그 개수만큼만 꺼내는 것이다. `for i in range(level_size)` 루프 안에서 자식 노드들을 큐에 새로 넣더라도, 이번 루프는 이미 `range(level_size)`로 횟수가 고정되어 있기 때문에 새로 들어온 자식들까지 같이 처리되지 않는다. 그래서 `i == level_size - 1`이 되는 순간이 정확히 "이번 레벨에서 마지막으로 꺼낸 노드", 즉 가장 오른쪽 노드를 가리키게 된다. 다음 레벨은 바깥의 `while queue`가 다시 `level_size`를 새로 계산하면서 이어서 처리해준다.

풀면서 걸렸던 부분은 다음과 같았다.

- 처음 작성한 코드에는 `typing` import가 빠져 있었고, `root` 변수에 실제 `TreeNode` 트리 대신 리스트(`[1,2,3,None,5,None,4]`)를 그대로 넣어서 `node.left` 접근에서 터지는 구조였다. 리스트 형태의 입력을 실제 트리 객체로 변환하는 `build_tree` 함수를 따로 만들고 나서야 코드가 의도대로 동작했다.
- `deque([root])`를 `deque(root)`로 잘못 써도 될 것 같다고 생각했는데, `deque(iterable)` 생성자는 인자를 순회 가능한 것으로 보고 풀어서 담기 때문에 `TreeNode` 객체를 그대로 넘기면 `TypeError: 'TreeNode' object is not iterable`가 난다. 트리는 배열처럼 원소를 여러 개 담고 있는 컨테이너가 아니라, `root` 변수 자체는 노드 1개만 가리키고 나머지 노드들은 `left`/`right` 포인터로 연결되어 있을 뿐이라는 걸 다시 확인했다.
- `level_size`가 `len(queue)`로 매 `while` 반복마다 새로 계산된다는 것, 그래서 큐가 처음에 root 1개로 시작해도 "모든 레벨이 미리 다 들어있는 상태"가 아니라 "현재 레벨만큼만 들어있는 상태"라는 점이 헷갈렸다.

시간 복잡도는 모든 노드를 한 번씩만 방문하므로 `O(n)`, 공간 복잡도는 큐가 가장 넓은 레벨의 노드 수만큼 쌓일 수 있으므로 `O(n)`이다.

### 더 개선한다면

BFS는 큐에 한 레벨 전체(최악의 경우 트리 폭만큼)를 들고 있어야 한다. 반면 오른쪽 자식을 먼저 방문하는 DFS로 풀면, 각 깊이에 처음 도달하는 노드가 항상 오른쪽 끝 노드가 되므로 별도의 `level_size` 계산 없이도 같은 결과를 얻을 수 있고, 공간은 큐의 폭 대신 트리의 높이만큼만 쓴다.

```python
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def dfs(node, depth):
            if node is None:
                return

            if depth == len(result):
                result.append(node.val)

            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)

        dfs(root, 0)
        return result
```

시간 복잡도는 여전히 `O(n)`으로 동일하지만, 공간 복잡도는 재귀 스택 깊이인 `O(h)`(h = 트리 높이)로 줄어든다. 균형 잡힌 트리라면 `O(log n)`까지 줄어드는 대신, 한쪽으로 치우친 트리에서는 여전히 `O(n)`이 될 수 있다는 점, 그리고 재귀 호출이라 파이썬 재귀 깊이 제한을 신경 써야 한다는 점이 트레이드오프다.

## 2. 스스로 묻고 답한 질문들

### Q. `for i in range(level_size)` 안에서 `i == level_size - 1`이 왜 가장 오른쪽 노드를 가리키나?

`level_size`는 그 순간 큐에 있던 "한 레벨 분량"의 노드 개수다. `i`는 0부터 `level_size - 1`까지 순서대로 증가하면서 큐에서 노드를 꺼내는데, 큐(deque)는 왼쪽에서 넣은 순서대로 왼쪽부터 빠지므로 같은 레벨 안에서는 왼쪽 노드부터 오른쪽 노드 순으로 꺼내진다. 그러니 `i`가 `level_size - 1`이 되는 마지막 반복에서 꺼낸 노드가 그 레벨의 가장 오른쪽 노드다.

### Q. `for` 하나로는 왜 안 되고 `while queue`로 한 번 더 감싸야 하나?

`for i in range(level_size)`는 시작할 때 정해진 횟수(그 시점의 레벨 크기)만큼만 돈다. 루프 안에서 자식 노드를 큐에 새로 넣어도 `range(level_size)`의 반복 횟수 자체는 바뀌지 않으므로, 그 `for`는 딱 한 레벨만 처리하고 끝난다. 트리의 나머지 레벨(자식들, 손자들...)까지 이어서 처리하려면 큐가 빌 때까지 레벨 단위 처리를 반복해야 하고, 그 반복을 담당하는 것이 바깥의 `while queue`다.

### Q. `queue = deque([root])`에서 왜 `root`가 원소 1개짜리로 취급되나?

트리는 리스트처럼 원소를 여러 개 담고 있는 자료구조가 아니다. `TreeNode` 객체 하나는 `val`, `left`, `right` 세 필드만 가진 단일 객체이고, `root` 변수는 그중에서도 트리 최상단 노드 1개만 가리킨다. 나머지 노드들은 `root` 안에 담겨 있는 게 아니라 `root.left`, `root.right`로 연결되어 있을 뿐이다. 그래서 `[root]`처럼 리스트로 감싸면 "원소가 1개(root)인 리스트"가 되어 `deque`에 정확히 노드 1개가 들어가고, BFS를 진행하면서 `node.left`/`node.right`를 큐에 추가해야 비로소 다음 레벨 노드들이 들어오게 된다.

### Q. `deque(root)`처럼 리스트로 감싸지 않고 바로 넘기면 안 되나?

안 된다. `deque(iterable)` 생성자는 인자로 받은 대상을 순회 가능한(iterable) 것으로 보고, 그 원소들을 하나씩 풀어서 담는다(`list(iterable)`과 같은 원리). 그런데 `TreeNode`는 리스트나 튜플처럼 반복 가능한 객체가 아니므로 `deque(root)`는 `TypeError: 'TreeNode' object is not iterable`로 즉시 에러가 난다. 설령 `TreeNode`가 억지로 iterable하게 구현되어 있다 해도, `deque` 생성자가 트리 구조를 재귀적으로 이해해서 모든 노드를 넣어주는 것은 아니므로 원하는 동작이 나오지 않는다.

## 정리하며

이번 문제를 통해 BFS에서 "레벨 단위로 끊어서 처리한다"는 게 코드로는 `level_size = len(queue)`를 매 반복마다 다시 계산하는 것으로 구현된다는 걸 명확히 정리했다. 또 `deque([root])`와 `deque(root)`의 차이, 그리고 트리가 배열이 아니라 노드들이 포인터로 연결된 구조라는 점을 다시 짚으면서 트리 자료구조에 대한 기본기를 다졌다. 다음에는 이 레벨별 BFS 패턴을 최소 깊이 찾기, 레벨별 평균 구하기 같은 변형 문제에도 적용해볼 계획이다.
