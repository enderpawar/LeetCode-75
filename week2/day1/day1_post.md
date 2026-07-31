# [LeetCode 75 Day 8] Binary Tree, DFS, Recursion

LeetCode 75 여덟 번째 날에는 이진 트리를 재귀적으로 탐색하는 두 문제를 풀었다. Maximum Depth of Binary Tree에서는 트리의 최대 깊이를 구했고, Leaf-Similar Trees에서는 두 트리의 말단 리프 값을 왼쪽부터 모아 순서를 비교했다.

두 문제 모두 DFS를 사용하지만 재귀 호출의 결과를 다루는 방식은 달랐다. 첫 번째 문제는 각 호출이 계산한 깊이를 반환받아 사용하고, 두 번째 문제는 탐색 중 발견한 리프 값을 리스트에 누적한다. 특히 두 번째 문제를 풀면서 하나의 재귀 호출 안에서 두 트리를 함께 움직이는 것과, 각 트리를 독립적으로 탐색하는 것의 차이를 정리할 수 있었다.

## 1. Maximum Depth of Binary Tree - 왼쪽과 오른쪽의 최대 깊이 구하기

이진 트리의 루트가 주어졌을 때 루트부터 가장 멀리 떨어진 리프까지의 노드 수를 반환하는 문제다. 빈 트리의 깊이는 0이고, 루트 노드 하나만 있다면 깊이는 1이다.

```python
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
```

현재 노드를 루트로 하는 트리의 최대 깊이는 다음과 같이 생각할 수 있다.

```text
현재 트리의 최대 깊이
= 현재 노드 1
+ 왼쪽과 오른쪽 서브트리 중 더 깊은 쪽
```

따라서 왼쪽 자식과 오른쪽 자식에 대해 `maxDepth()`를 재귀 호출하고, 두 반환값 중 큰 값에 현재 노드의 깊이 1을 더한다.

```python
1 + max(
    self.maxDepth(root.left),
    self.maxDepth(root.right)
)
```

재귀가 끝나려면 더 이상 내려갈 수 없는 경우가 필요하다. 자식이 없는 노드에서도 왼쪽과 오른쪽에 대해 재귀 호출은 이루어지는데, 그때 전달되는 값은 `None`이다. `root is None`이면 0을 반환하도록 한 이유가 여기에 있다.

```text
리프 노드의 깊이
= 1 + max(0, 0)
= 1
```

한쪽 자식만 있는 노드도 별도의 조건 없이 처리된다. 없는 쪽은 0을 반환하고, 존재하는 쪽의 깊이가 선택된다.

트리의 모든 노드를 한 번씩 방문하므로 시간 복잡도는 `O(n)`이다. 재귀 호출 스택에는 현재 탐색 중인 경로가 저장되므로 공간 복잡도는 트리의 높이를 `h`라고 할 때 `O(h)`다. 한쪽으로만 이어진 트리에서는 `O(n)`, 균형 잡힌 트리에서는 `O(log n)`이 된다.

## 2. Leaf-Similar Trees - 트리 구조가 아닌 리프 순서 비교하기

두 이진 트리의 말단 리프 값을 왼쪽에서 오른쪽 순서로 나열했을 때, 두 값의 순서가 같은지 확인하는 문제다.

예제의 두 트리는 내부 구조가 서로 다르지만 리프 순서는 모두 다음과 같다.

```text
[6, 7, 4, 9, 8]
```

따라서 두 트리는 leaf-similar이고 `True`를 반환한다. 이 문제에서 비교하는 것은 같은 위치에 있는 노드나 트리의 전체 구조가 아니라, 각 트리에서 독립적으로 얻은 리프 값의 순서다.

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def leafSimilar(self, root1, root2):
        leaf1 = []
        leaf2 = []

        def dfs(leaf_list, root):
            if root.left is None and root.right is None:
                leaf_list.append(root.val)
                return

            if root.left:
                dfs(leaf_list, root.left)

            if root.right:
                dfs(leaf_list, root.right)

        dfs(leaf1, root1)
        dfs(leaf2, root2)

        return leaf1 == leaf2
```

`leafSimilar()`은 LeetCode가 전달한 두 루트 노드를 받는 역할을 한다. 그 안의 `dfs()`는 한 번에 하나의 트리만 탐색하며, 발견한 리프 값을 전달받은 리스트에 추가한다.

리프 노드는 왼쪽 자식과 오른쪽 자식이 모두 없는 노드다.

```python
if root.left is None and root.right is None:
    leaf_list.append(root.val)
    return
```

여기서는 노드 객체인 `root`가 아니라 문제에서 비교하려는 값인 `root.val`을 저장한다. 리프를 발견한 뒤에는 더 탐색할 자식이 없으므로 `return`으로 현재 호출을 끝낸다.

리프가 아니라면 왼쪽을 먼저 탐색하고 그다음 오른쪽을 탐색한다.

```python
if root.left:
    dfs(leaf_list, root.left)

if root.right:
    dfs(leaf_list, root.right)
```

이 호출 순서 때문에 리프 값도 왼쪽에서 오른쪽 순서로 리스트에 들어간다. 두 트리의 탐색이 모두 끝나면 리스트 자체를 비교한다. 파이썬의 리스트 비교는 원소의 값뿐 아니라 순서도 함께 확인하므로 이 문제의 조건과 일치한다.

처음에는 `leafSimilar()` 안에서 `root1`과 `root2`를 함께 재귀 호출하는 방법을 생각했다. `root1`을 이동할 때 `root2`를 같은 자리에 동결하면 트리의 구조가 달라도 탐색할 수 있을 것 같았다.

```python
self.leafSimilar(root1.left, root2)
self.leafSimilar(root1.right, root2)
```

하지만 각 재귀 호출 안에서 `root2`의 탐색 코드도 다시 실행된다. 깊이가 1인 다음 트리를 생각하면 문제가 더 분명해진다.

```text
    1
   / \
  2   3
```

`root1`의 리프 2를 처리하는 호출에서 `root2` 전체를 탐색해 `[2, 3]`을 추가하고, `root1`의 리프 3을 처리하는 호출에서 다시 `root2` 전체를 탐색하면 결과가 다음처럼 중복된다.

```text
leaf2 = [2, 3, 2, 3]
```

이는 단순히 시간 복잡도가 나빠지는 문제가 아니다. 리프 목록 자체가 달라져 오답이 된다. 한 함수에서 두 트리를 함께 처리하려면 현재 어느 트리를 탐색 중인지 구분하는 별도의 상태가 필요하다. 이 문제에서는 각 트리에 같은 `dfs()`를 한 번씩 적용하는 편이 역할도 명확하고 중복 탐색도 없다.

구현 과정에서 내부 함수의 첫 번째 인자에 `self`를 넣기도 했다.

```python
def dfs(self, leaf_list, root):
```

그러나 이 `dfs()`는 `Solution` 클래스에 직접 정의된 메서드가 아니라 `leafSimilar()` 안에서 만든 지역 함수다. `dfs(leaf1, root1)`처럼 직접 호출할 때 인스턴스가 자동으로 전달되지 않으므로 `self`가 필요 없다. 인자를 그대로 두면 함수는 세 개의 인자를 요구하지만 두 개만 받게 되어 `TypeError`가 발생한다.

또한 `leaf1`과 `leaf2`는 전역변수가 아니라 `leafSimilar()` 안에서 생성해야 한다. 전역 리스트를 사용하면 다음 테스트를 실행할 때 이전 호출에서 저장한 값이 남을 수 있다. 함수가 호출될 때마다 새 리스트를 만들면 각 테스트가 독립적으로 실행된다.

두 트리의 노드 수를 각각 `n`, `m`이라고 하면 모든 노드를 한 번씩 방문하므로 시간 복잡도는 `O(n + m)`이다. 리프 목록에는 각 트리의 리프 수만큼 값이 저장되고 재귀 호출 스택에는 현재 경로가 저장된다. 리프 수를 `L1`, `L2`, 트리 높이를 `h1`, `h2`라고 하면 추가 공간은 `O(L1 + L2 + h1 + h2)`로 볼 수 있고, 최악의 경우 `O(n + m)`이다.

## 3. 스스로 묻고 답한 질문들

### Q. LeetCode 예제의 `null`을 파이썬 코드에 그대로 쓰면 왜 오류가 날까?

LeetCode가 입력을 보여줄 때 사용하는 배열 표기는 JSON 형식에 가깝다. JSON에서는 값이 없음을 `null`로 표현하지만, 파이썬에서는 `None`을 사용한다.

```python
# LeetCode 입력 표기
[1, 2, null]

# 파이썬 값
[1, 2, None]
```

다만 문제에 제출하는 함수가 실제로 받는 `root1`과 `root2`는 이 배열 자체가 아니다. LeetCode가 배열을 `TreeNode`로 구성한 뒤 루트 노드를 전달한다. 그래서 제출 코드에 예제 배열을 직접 선언할 필요는 없다.

### Q. 리프인지 확인할 때 `if root.left and root.right`를 사용하면 안 될까?

이 조건은 두 자식이 모두 존재하는지를 검사한다. 리프는 두 자식이 모두 존재하지 않는 노드이므로 의미가 반대다.

```python
root.left is None and root.right is None
```

또한 자식이 한쪽에만 있는 중간 노드도 리프가 아니다. `if root.left and root.right`의 `else`에서 리프로 처리하면 이런 노드를 잘못 수집하게 된다.

### Q. 두 트리의 리프를 같은 재귀 호출에서 한 쌍씩 비교하면 안 될까?

두 트리의 구조가 같다는 보장이 없기 때문에 어렵다. 같은 리프 순서를 가진 트리에서도 각 리프가 나타나는 깊이와 위치는 다를 수 있다. `root1.left`와 `root2.left`처럼 위치를 맞춰 내려가면 리프 순서가 같아도 구조가 다른 경우를 놓친다.

각 트리에서 왼쪽부터 리프 순서를 먼저 구한 뒤 두 결과를 비교하면 구조와 상관없이 문제에서 요구한 조건만 확인할 수 있다.

### Q. 내부 `dfs()`에도 `self`를 붙여야 하지 않을까?

`self`는 클래스의 인스턴스 메서드가 호출된 객체를 받는 매개변수다.

```python
class Solution:
    def leafSimilar(self, root1, root2):
        ...
```

여기서 `leafSimilar()`는 `Solution`의 메서드이므로 `self`가 필요하다. 반면 `leafSimilar()` 안에 정의한 `dfs()`는 단순한 지역 함수이므로 `self` 없이 필요한 값만 매개변수로 받으면 된다.

### Q. 두 문제는 모두 DFS인데 반환 방식은 왜 다를까?

Maximum Depth of Binary Tree에서는 각 서브트리의 깊이가 부모 호출의 계산에 바로 필요하다. 그래서 재귀 호출이 정수 깊이를 반환한다.

Leaf-Similar Trees에서는 탐색 전체에서 발견한 여러 리프 값을 순서대로 보관해야 한다. 각 호출이 같은 `leaf_list`를 공유하고, 리프를 발견할 때 값을 추가하는 방식이 자연스럽다.

즉, DFS라는 탐색 방식은 같아도 필요한 결과가 하나의 계산값인지, 여러 값을 순서대로 모은 결과인지에 따라 반환값과 누적 리스트 중 알맞은 방식을 선택할 수 있다.

## 정리하며

이번 두 문제를 통해 재귀 함수에서는 먼저 한 호출의 역할을 좁게 정하는 것이 중요하다는 점을 확인했다. `maxDepth()`의 한 호출은 현재 노드를 루트로 하는 트리의 최대 깊이를 반환하고, `dfs()`의 한 호출은 현재 노드 아래에서 리프를 찾아 전달받은 리스트에 저장한다.

특히 Leaf-Similar Trees에서는 두 트리를 함께 재귀 호출하는 것보다 각각 독립적으로 탐색한 결과를 비교해야 한다는 점이 핵심이었다. 한쪽 루트를 동결해도 다른 쪽의 재귀 호출마다 동결된 트리의 탐색이 반복되면 값이 중복된다. 재귀를 작성할 때는 단순히 다음 노드로 이동하는 것뿐 아니라, 각 호출 안에서 어떤 코드가 다시 실행되고 어떤 상태가 누적되는지도 함께 추적해야 한다.
