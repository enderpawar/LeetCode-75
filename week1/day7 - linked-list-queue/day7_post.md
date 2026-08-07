# [LeetCode 75 Day 7] LinkedList, Queue

LeetCode 75 일곱 번째 날에는 최근 요청만 남기는 문제와 단방향 연결 리스트의 순서를 뒤집는 문제를 풀었다. 하나는 큐에서 오래된 값을 제거하고, 다른 하나는 노드 사이의 연결 방향을 바꾸는 문제다.

두 문제의 모양은 다르지만 공통점이 있었다. 자료구조에 값을 넣는 것만으로는 충분하지 않고, 이제 필요하지 않은 값은 어디에서 제거할지, 다음으로 이동할 위치는 어떻게 잃어버리지 않을지를 직접 관리해야 했다. 이번에는 `deque`의 연산과 연결 리스트의 포인터 변경 순서를 중심으로 정리했다.

## 1. Number of Recent Calls - 최근 3000밀리초의 요청만 남기기

`ping(t)`가 호출될 때마다 현재 시각 `t`를 기록하고, `[t - 3000, t]` 범위에 들어오는 요청의 개수를 반환하는 문제다. `t`는 호출될 때마다 반드시 증가한다.

```python
from collections import deque


class RecentCounter:
    def __init__(self):
        self.queue = deque()

    def ping(self, t: int) -> int:
        self.queue.append(t)

        while self.queue and self.queue[0] < t - 3000:
            self.queue.popleft()

        return len(self.queue)
```

요청 시각이 오름차순으로 들어오므로 `queue`의 앞에는 항상 가장 오래된 요청이 있다. 새 요청을 오른쪽 끝에 추가한 뒤, 현재 범위보다 오래된 요청을 왼쪽 끝에서 하나씩 제거하면 된다.

여기서 제거 조건은 다음과 같다.

```python
self.queue[0] < t - 3000
```

유효 범위가 양 끝을 포함하는 `[t - 3000, t]`이기 때문에 시각이 정확히 `t - 3000`인 요청은 남겨야 한다. 따라서 `<=`가 아니라 `<`를 사용한다.

예제의 흐름을 따라가면 경계값이 어떻게 처리되는지 확인할 수 있다.

```text
ping(1)    → [1]                 → 1
ping(100)  → [1, 100]            → 2
ping(3001) → [1, 100, 3001]      → 3
ping(3002) → [100, 3001, 3002]   → 3
```

`ping(3001)`에서는 범위가 `[1, 3001]`이므로 시각 1의 요청도 포함된다. 다음 `ping(3002)`에서는 범위가 `[2, 3002]`로 바뀌기 때문에 시각 1만 제거된다.

리스트에서도 앞의 값을 지울 수 있지만, `pop(0)`을 사용하면 뒤에 있는 원소들을 모두 한 칸씩 당겨야 해서 `O(n)`이 걸린다. `deque.popleft()`는 왼쪽 끝의 값을 `O(1)`에 제거하므로 이 문제에 알맞다.

각 요청은 한 번 추가되고 최대 한 번 제거된다. 한 번의 `ping()`에서 여러 요청이 빠질 수 있지만, 전체 호출을 기준으로 보면 요청 `n`개의 총 처리 시간은 `O(n)`이다. 따라서 `ping()`의 분할 상환 시간 복잡도는 `O(1)`이고, 큐에는 아직 유효한 요청만 저장하므로 공간 복잡도는 `O(k)`다. 여기서 `k`는 현재 3000밀리초 범위 안에 있는 요청 수이며, 최악의 경우 전체 요청 수 `n`과 같을 수 있다.

## 2. Reverse Linked List - 다음 노드를 잃지 않고 연결 방향 바꾸기

단방향 연결 리스트의 `head`가 주어졌을 때 모든 연결 방향을 뒤집고, 뒤집힌 리스트의 새로운 머리 노드를 반환하는 문제다.

```python
from typing import Optional


# LeetCode에서 제공하는 노드 정의
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(
        self, head: Optional[ListNode]
    ) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        return prev
```

`prev`는 이미 방향을 뒤집은 앞쪽 리스트의 머리를 가리키고, `curr`은 지금 처리할 노드를 가리킨다. 반복문에서는 다음 네 단계를 순서대로 실행한다.

1. `curr.next`를 `next_node`에 보관한다.
2. `curr.next`가 이전 노드인 `prev`를 가리키게 한다.
3. `prev`를 현재 노드까지 전진시킨다.
4. `curr`을 미리 보관한 다음 노드로 옮긴다.

`1 → 2 → 3`을 뒤집는 과정은 다음과 같다.

```text
시작
prev = None
curr = 1 → 2 → 3

1 처리
prev = 1 → None
curr = 2 → 3

2 처리
prev = 2 → 1 → None
curr = 3

3 처리
prev = 3 → 2 → 1 → None
curr = None
```

가장 중요한 부분은 연결을 바꾸기 전에 `next_node = curr.next`를 실행하는 것이다. 먼저 `curr.next = prev`로 덮어쓰면 원래 다음 노드를 가리키던 연결이 사라진다. 그러면 아직 처리하지 않은 나머지 리스트로 이동할 방법이 없어진다.

반복이 끝나는 순간 `curr`은 `None`이고, `prev`는 마지막으로 처리한 노드를 가리킨다. 원래 리스트의 마지막 노드가 뒤집힌 리스트의 첫 노드가 되므로 `prev`를 반환한다.

빈 리스트에서는 `curr`이 처음부터 `None`이어서 반복문을 실행하지 않고 `prev`, 즉 `None`을 반환한다. 노드가 하나뿐인 경우에는 그 노드의 `next`를 `None`으로 둔 채 `prev`가 해당 노드를 가리키게 되므로 그대로 반환된다.

모든 노드를 한 번씩 방문하므로 시간 복잡도는 `O(n)`이다. 노드를 새로 만들지 않고 포인터 역할을 하는 변수만 사용하므로 추가 공간 복잡도는 `O(1)`이다.

## 3. 스스로 묻고 답한 질문들

### Q. `deque`는 큐일까, 스택일까?

`deque`는 double-ended queue의 줄임말로, 양쪽 끝에서 값을 추가하고 제거할 수 있는 자료구조다. 어떤 연산을 선택하느냐에 따라 큐처럼 쓸 수도 있고 스택처럼 쓸 수도 있다.

```python
from collections import deque

values = deque()

# 오른쪽 끝
values.append(1)       # 오른쪽에 추가
right = values.pop()   # 오른쪽에서 제거하고 반환

# 왼쪽 끝
values.appendleft(2)   # 왼쪽에 추가
left = values.popleft()  # 왼쪽에서 제거하고 반환
```

큐는 먼저 들어온 값을 먼저 꺼내는 FIFO 방식이다.

```python
queue = deque()
queue.append(1)
queue.append(2)
queue.popleft()  # 1
```

스택은 마지막에 들어온 값을 먼저 꺼내는 LIFO 방식이다.

```python
stack = deque()
stack.append(1)
stack.append(2)
stack.pop()  # 2
```

이번 문제에서는 새 요청을 `append()`로 오른쪽에 넣고 가장 오래된 요청을 `popleft()`로 왼쪽에서 꺼내므로 큐로 사용했다.

### Q. 이번 풀이에서 사용한 것 외에 `deque`에는 어떤 연산이 있을까?

`extend(iterable)`과 `extendleft(iterable)`은 여러 값을 한꺼번에 추가한다. 다만 `extendleft()`는 전달받은 값을 하나씩 왼쪽에 넣기 때문에 결과 순서가 뒤집힌다.

```python
values = deque([2, 3])
values.extend([4, 5])       # deque([2, 3, 4, 5])
values.extendleft([0, 1])   # deque([1, 0, 2, 3, 4, 5])
```

`rotate(n)`은 원소를 회전시킨다. 양수면 오른쪽으로, 음수면 왼쪽으로 이동한다. `reverse()`는 원소의 순서를 제자리에서 뒤집고, `clear()`는 모든 원소를 제거한다.

```python
values = deque([1, 2, 3])
values.rotate(1)   # deque([3, 1, 2])
values.rotate(-1)  # deque([1, 2, 3])
values.reverse()   # deque([3, 2, 1])
values.clear()     # deque([])
```

값을 찾거나 수정할 때는 `count(x)`, `index(x)`, `insert(i, x)`, `remove(x)`를 사용할 수 있다. `copy()`는 같은 원소를 가진 얕은 복사본을 만든다.

```python
values = deque([1, 2, 2, 3])

values.count(2)       # 2
values.index(2)       # 1, 처음 발견한 위치
values.insert(1, 9)   # deque([1, 9, 2, 2, 3])
values.remove(2)      # 첫 번째 2를 제거
copied = values.copy()
```

`len(values)`로 현재 원소 수를 구하고, `values[0]`과 `values[-1]`로 양 끝의 값을 읽을 수도 있다. 생성할 때 `maxlen`을 지정하면 최대 길이가 고정되며, 가득 찬 뒤 반대쪽에 새 값을 추가하면 다른 쪽 끝의 값이 자동으로 빠진다.

```python
recent = deque(maxlen=3)
recent.extend([1, 2, 3])
recent.append(4)       # deque([2, 3, 4], maxlen=3)
recent.maxlen          # 3
```

다만 `deque`는 양 끝의 추가와 제거에 맞춘 자료구조다. 중간 위치를 찾는 `index()`, 중간에 넣는 `insert()`, 특정 값을 찾은 뒤 지우는 `remove()` 등은 원소를 탐색해야 하므로 최악의 경우 `O(n)`이 걸린다. 중간 인덱스를 자주 조회해야 한다면 리스트가 더 알맞다.

### Q. 오래된 요청을 제거할 때 `if`가 아니라 `while`을 쓰는 이유는 무엇일까?

새로운 `t`가 이전 값보다 크게 뛰면 한 번의 호출에서 여러 요청이 범위를 벗어날 수 있기 때문이다. `if`는 가장 오래된 요청 하나만 제거하지만, `while`은 큐의 맨 앞이 유효 범위에 들어올 때까지 모든 오래된 요청을 제거한다.

```text
현재 queue = [1, 100, 200]
새 요청 t = 5000
유효 범위 = [2000, 5000]

1, 100, 200을 모두 제거해야 함
```

### Q. `self.queue` 대신 `queue`라는 지역 변수를 만들면 안 될까?

`ping()`이 끝난 뒤에도 이전 요청 기록이 남아 있어야 하므로 인스턴스 변수인 `self.queue`에 저장해야 한다. 지역 변수는 메서드를 호출할 때마다 새로 만들어지고 호출이 끝나면 유지되지 않는다.

### Q. `Optional[ListNode]`는 무슨 뜻일까?

값이 `ListNode`일 수도 있고 `None`일 수도 있다는 타입 힌트다. 입력 `head`는 빈 연결 리스트일 때 `None`이 될 수 있고, 반환값도 같은 이유로 `None`이 될 수 있다.

LeetCode에서는 `ListNode` 정의를 미리 제공한다. 같은 코드를 로컬 파일에서 독립적으로 실행하려면 `Optional`을 임포트하는 것뿐 아니라 주석으로 표시된 `ListNode` 클래스도 직접 정의해야 한다.

### Q. `next` 대신 `next_node`라는 이름을 사용한 이유는 무엇일까?

파이썬에는 반복자에서 다음 값을 가져오는 내장 함수 `next()`가 있다. 지역 변수 이름을 `next`로 정해도 문법 오류는 아니지만, 그 범위 안에서는 내장 함수 이름을 가리게 된다. `next_node`라고 적으면 연결 리스트의 다음 노드라는 의미도 더 분명하다.

### Q. 재귀 호출로도 연결 리스트를 뒤집을 수 있을까?

가능하지만, 재귀 풀이에서는 노드마다 호출 스택에 상태를 보관하므로 추가 공간이 `O(n)` 필요하다. 파이썬에는 재귀 깊이 제한도 있다. 이번 반복문 풀이는 연결 방향을 직접 바꾸면서 변수 몇 개만 사용하므로 추가 공간이 `O(1)`이다.

## 정리하며

Day 7에서는 자료구조 안에서 값이 흘러가는 방향을 직접 관리했다. Number of Recent Calls에서는 새 값은 오른쪽에 넣고 오래된 값은 왼쪽에서 제거했다. Reverse Linked List에서는 아직 처리하지 않은 다음 노드를 먼저 저장한 뒤, 현재 노드의 연결을 이전 노드 쪽으로 돌렸다.

두 풀이 모두 연산 순서가 정답에 직접 영향을 준다. 큐에서는 유효 범위의 경계값을 남긴 뒤 오래된 요청을 모두 제거해야 하고, 연결 리스트에서는 원래의 다음 노드를 잃기 전에 먼저 보관해야 한다. `deque`의 양 끝 연산과 `prev`, `curr`, `next_node`의 역할을 실행 순서대로 따라가면서 각 줄이 필요한 이유를 구체적으로 확인할 수 있었다.
