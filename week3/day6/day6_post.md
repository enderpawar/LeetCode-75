[LeetCode 75 Day 20] 199. Binary Tree Right Side View & 437. Path Sum III

이번 day6에서는 트리 순회를 두 가지 다른 각도에서 연습했다. 199번은 레벨 단위로 큐를 끊어서 처리하는 BFS 패턴이었고, 437번은 재귀 함수 하나에 "경로를 이어가는 것"과 "여기서 새로 시작하는 것"이라는 서로 다른 책임을 같이 욱여넣었다가 중복 카운트 버그를 겪으면서, 재귀 구조를 어떻게 나눠야 하는지를 다시 생각해보게 된 문제였다.

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

## 2. Path Sum III - 아무 노드에서나 시작해 아래로 내려가는 경로 합 세기

이진 트리의 root와 정수 targetSum이 주어졌을 때, 경로가 루트에서 시작하거나 리프에서 끝날 필요 없이, 부모에서 자식 방향으로만 내려가면서 노드 값을 더한 합이 targetSum이 되는 경로의 개수를 구하는 문제다.

```python
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        cnt = 0

        # node를 시작점으로 고정하고, 거기서부터 아래로 내려가며 합을 누적한다.
        # "여기서 새로 시작"이라는 개념이 없어서, 이전처럼 중복으로 세는 일이 없다.
        def dfs(node: Optional[TreeNode], sum: int):
            nonlocal cnt
            if node is None:
                return

            sum += node.val

            if sum == targetSum:
                cnt += 1

            dfs(node.left, sum)
            dfs(node.right, sum)

        # 트리의 모든 노드를 한 번씩 방문하면서, 각 노드를 시작점 삼아 dfs를 새로 돌린다.
        def preorder(node: Optional[TreeNode]):
            if node is None:
                return

            dfs(node, 0)
            preorder(node.left)
            preorder(node.right)

        preorder(root)

        return cnt
```

경로가 루트가 아니라 어떤 노드에서 시작해도 되기 때문에, 트리의 모든 노드를 한 번씩 "잠재적 시작점"으로 취급해야 한다. 그래서 함수를 역할별로 둘로 나눴다. `preorder`는 트리를 그냥 순회만 하면서 노드를 하나씩 방문하고, 그 노드를 방문할 때마다 `dfs(node, 0)`을 딱 한 번 호출해서 "이 노드를 시작점으로 삼았을 때의 경로 합"을 센다. `dfs` 자신은 오직 "이미 정해진 시작점에서부터 이어지는 합"만 누적할 뿐, 자기 안에서 또 새로운 시작점을 만들지 않는다. 이렇게 책임을 나누고 나니 각 노드가 시작점으로 취급되는 시점이 `preorder`가 그 노드를 지나가는 순간, 딱 한 번으로 고정됐다.

풀면서 걸렸던 부분은 다음과 같았다.

- `cnt += 1`을 `cnt +`라고 쓰다가 그냥 SyntaxError가 났고, `nonlocal cnt`를 빼먹어서 `dfs` 안에서 바깥의 `cnt`를 수정하려다 에러가 나기도 했다.
- `node`가 `None`인지 확인하지 않고 바로 `node.val`부터 접근하려 해서, `Optional[TreeNode]` 타입에 대해 Pylance가 `val은 "None"의 알려진 특성이 아님`이라는 경고를 띄웠다. 실제로 빈 트리(`root=None`)가 들어오면 `AttributeError`로 터지는 코드였다.
- 가장 오래 걸린 부분은 따로 있었다. 처음엔 자식으로 내려갈 때 `dfs(child, sum)`(경로 이어가기)과 `dfs(child, 0)`(그 자식에서 새로 시작하기)을 같은 함수 안에서 같이 호출했다. `[1,null,2,null,3,null,4,null,5]`, `targetSum=3` 같은 한 줄짜리 체인 트리로 테스트해보니 정답은 `2`(`{3}` 단독, `{1,2}`)여야 하는데 `3`이 나왔다. 추적해보니 "3번 노드 혼자인 경로"가 서로 다른 두 실행 경로(2번 노드를 거쳐 이어오다가 3번에서 새로 시작한 경우, 2번 노드에서 새로 시작해서 3번까지 이어온 뒤 다시 3번에서 새로 시작한 경우)를 통해 중복으로 세어지고 있었다.

시간 복잡도는 `preorder`가 노드를 한 번씩 방문할 때마다 `dfs`가 그 아래 서브트리를 다시 훑기 때문에 최악의 경우(한쪽으로 치우친 트리) `O(n^2)`이고, 공간 복잡도는 재귀 호출 스택 깊이인 `O(h)`(h = 트리 높이)이다.

### 더 개선한다면

`preorder`로 매 노드를 시작점 삼아 다시 훑는 대신, prefix sum(누적합)을 해시맵에 기록해두면 각 노드를 한 번씩만 방문하고도 같은 답을 구할 수 있다. 루트에서부터 현재 노드까지의 누적합을 `running_sum`이라 하면, `running_sum - targetSum`이 과거에 등장했던 누적합이라는 것은 그 지점 바로 다음부터 지금 노드까지의 구간 합이 정확히 `targetSum`이라는 뜻이다.

```python
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        prefix_sums = {0: 1}
        cnt = 0

        def dfs(node: Optional[TreeNode], running_sum: int):
            nonlocal cnt
            if node is None:
                return

            running_sum += node.val
            cnt += prefix_sums.get(running_sum - targetSum, 0)

            prefix_sums[running_sum] = prefix_sums.get(running_sum, 0) + 1
            dfs(node.left, running_sum)
            dfs(node.right, running_sum)
            # 이 노드의 서브트리 탐색이 끝났으니, 다른 가지에 영향 안 주도록 되돌려놓는다.
            prefix_sums[running_sum] -= 1

        dfs(root, 0)
        return cnt
```

시간 복잡도는 `O(n)`으로 줄어들지만, 각 노드에서 재귀를 빠져나올 때 `prefix_sums[running_sum] -= 1`로 되돌려놓는 걸 잊으면 형제 가지(sibling branch)끼리 서로 영향을 줘서 다시 틀린 답이 나온다. 즉 속도를 얻는 대신, 언제 되돌려놓아야 하는지를 더 신경 써야 하는 트레이드오프가 있다. 공간 복잡도는 재귀 스택 `O(h)`에 더해 `prefix_sums` 딕셔너리도 현재 경로 위에 있는 노드 수만큼(`O(h)`)만 쌓인다.

## 3. 스스로 묻고 답한 질문들

### Q. `for i in range(level_size)` 안에서 `i == level_size - 1`이 왜 가장 오른쪽 노드를 가리키나?

`level_size`는 그 순간 큐에 있던 "한 레벨 분량"의 노드 개수다. `i`는 0부터 `level_size - 1`까지 순서대로 증가하면서 큐에서 노드를 꺼내는데, 큐(deque)는 왼쪽에서 넣은 순서대로 왼쪽부터 빠지므로 같은 레벨 안에서는 왼쪽 노드부터 오른쪽 노드 순으로 꺼내진다. 그러니 `i`가 `level_size - 1`이 되는 마지막 반복에서 꺼낸 노드가 그 레벨의 가장 오른쪽 노드다.

### Q. `for` 하나로는 왜 안 되고 `while queue`로 한 번 더 감싸야 하나?

`for i in range(level_size)`는 시작할 때 정해진 횟수(그 시점의 레벨 크기)만큼만 돈다. 루프 안에서 자식 노드를 큐에 새로 넣어도 `range(level_size)`의 반복 횟수 자체는 바뀌지 않으므로, 그 `for`는 딱 한 레벨만 처리하고 끝난다. 트리의 나머지 레벨(자식들, 손자들...)까지 이어서 처리하려면 큐가 빌 때까지 레벨 단위 처리를 반복해야 하고, 그 반복을 담당하는 것이 바깥의 `while queue`다.

### Q. `queue = deque([root])`에서 왜 `root`가 원소 1개짜리로 취급되나?

트리는 리스트처럼 원소를 여러 개 담고 있는 자료구조가 아니다. `TreeNode` 객체 하나는 `val`, `left`, `right` 세 필드만 가진 단일 객체이고, `root` 변수는 그중에서도 트리 최상단 노드 1개만 가리킨다. 나머지 노드들은 `root` 안에 담겨 있는 게 아니라 `root.left`, `root.right`로 연결되어 있을 뿐이다. 그래서 `[root]`처럼 리스트로 감싸면 "원소가 1개(root)인 리스트"가 되어 `deque`에 정확히 노드 1개가 들어가고, BFS를 진행하면서 `node.left`/`node.right`를 큐에 추가해야 비로소 다음 레벨 노드들이 들어오게 된다.

### Q. `deque(root)`처럼 리스트로 감싸지 않고 바로 넘기면 안 되나?

안 된다. `deque(iterable)` 생성자는 인자로 받은 대상을 순회 가능한(iterable) 것으로 보고, 그 원소들을 하나씩 풀어서 담는다(`list(iterable)`과 같은 원리). 그런데 `TreeNode`는 리스트나 튜플처럼 반복 가능한 객체가 아니므로 `deque(root)`는 `TypeError: 'TreeNode' object is not iterable`로 즉시 에러가 난다. 설령 `TreeNode`가 억지로 iterable하게 구현되어 있다 해도, `deque` 생성자가 트리 구조를 재귀적으로 이해해서 모든 노드를 넣어주는 것은 아니므로 원하는 동작이 나오지 않는다.

### Q. 함수 안에 정의한 또 다른 내부 함수를 그냥 이름으로 호출해도 되나?

된다. 파이썬은 클로저를 지원해서, 내부 함수는 자기 자신이나 같은 스코프에 정의된 다른 내부 함수를 이름만으로 참조할 수 있다. `pathSum` 안에서 `dfs`가 자기 자신을 재귀 호출하는 것도, `preorder`가 `dfs`를 호출하는 것도 같은 원리다. 다만 바깥 함수의 변수를 안에서 **읽기만** 한다면 그냥 참조하면 되지만, `cnt += 1`처럼 **재할당**하려면 `nonlocal`을 붙여야 한다. 안 붙이면 파이썬은 그 이름을 내부 함수의 새 지역변수로 취급해서 "할당 전에 참조했다"는 에러를 낸다.

### Q. `Optional[TreeNode]` 타입인데 왜 `node.val`에 접근하면 경고가 뜨나?

`Optional[TreeNode]`는 "`TreeNode`이거나 `None`일 수 있다"는 뜻이다. 타입 체커는 코드를 실제로 실행해보는 게 아니라 선언된 타입만 보고 정적으로 판단하기 때문에, `node`가 `None`이 아님을 증명하는 코드(`if node is None: return`) 없이 바로 `.val`에 접근하면 "`None`일 수도 있는데 그 속성은 없다"고 경고한다. 실제로 이 경고 덕분에 빈 트리 입력을 처리 못 하는 버그를 미리 발견할 수 있었다.

### Q. `dfs(child, sum)`과 `dfs(child, 0)`을 같은 함수 안에서 같이 부르면 왜 중복 카운트가 생기나?

"경로를 이어간다"와 "여기서 새로 시작한다"는 서로 다른 책임인데, 하나의 재귀 함수가 매 호출마다 이 둘을 동시에 만들어내기 때문이다. 어떤 노드에 도달하는 실행 경로가 여러 갈래(이어가기/새로 시작하기 조합)로 나뉘어 있으면, 그 노드에서 다시 "새로 시작하기"를 호출할 때마다 매 갈래마다 한 번씩, 즉 조상 노드 수만큼 반복해서 같은 시작점을 다시 계산하게 된다. 반면 "새로 시작하기"를 트리 전체를 순회하는 `preorder` 쪽으로 완전히 옮기면, 그 순회 자체가 각 노드를 정확히 한 번만 지나가므로 시작점 계산도 한 번으로 고정된다.

## 정리하며

199번에서는 BFS에서 "레벨 단위로 끊어서 처리한다"는 게 코드로는 `level_size = len(queue)`를 매 반복마다 다시 계산하는 것으로 구현된다는 걸 정리했고, 437번에서는 재귀 함수 하나에 서로 다른 책임을 같이 넣으면 호출 경로가 갈라지면서 같은 계산이 중복될 수 있다는 걸 직접 겪어봤다. "경로를 이어가는 함수"와 "새로 시작점을 만드는 함수"를 분리하고 나서야 문제가 풀렸고, 그 과정에서 prefix sum으로 O(n)까지 최적화하는 방법도 함께 정리했다. 다음에는 이 prefix sum 패턴을 부분합 관련 다른 트리/배열 문제에도 적용해볼 계획이다.
