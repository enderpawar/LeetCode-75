# [LeetCode 75 Day 17] 1448. Count Good Nodes in Binary Tree

Day 17에서는 다시 이진 트리 DFS로 돌아왔다. 다만 Day 8에서 다룬 최대 깊이나 리프 비교와 달리, 이번에는 "루트에서 지금 노드까지의 경로"라는 값을 계속 들고 내려가야 하는 문제였다. 알고리즘의 아이디어 자체는 의사코드 단계에서 금방 떠올랐는데, 그 아이디어를 파이썬 함수로 어떻게 표현할지에서 오래 붙잡혔다. 로직은 어렵지 않았는데 파이썬 문법에 익숙하지 않아서 시간이 오래 걸린 문제다.

## 1. Count Good Nodes in Binary Tree - 경로의 최댓값을 들고 내려가기

이진 트리에서 어떤 노드 X가 good node가 되려면, 루트에서 X까지 가는 경로에 있는 노드들 중 X보다 큰 값이 하나도 없어야 한다. 트리 전체에서 good node의 개수를 세는 문제다.

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        GN_cnt = 0

        def DFS(node, path_max):
            nonlocal GN_cnt

            if node is None:
                return

            if node.val >= path_max:
                path_max = node.val
                GN_cnt += 1

            DFS(node.left, path_max)
            DFS(node.right, path_max)

        DFS(root, float('-inf'))
        return GN_cnt
```

처음에 의사코드를 적을 때는 "지금까지 나온 값들의 최댓값을 들고 있다가, 현재 노드가 그 값 이상이면 good node"라는 생각까지는 바로 나왔다. 문제는 그 "들고 있다가"를 코드로 옮기는 방법이었다. 처음에는 최댓값을 전역 변수나 클래스 속성으로 두고 트리를 훑으면 될 거라 생각했는데, 그렇게 하면 왼쪽 서브트리를 다 본 뒤 오른쪽으로 넘어갈 때도 같은 변수 하나를 계속 나눠 쓰게 된다. "루트에서 X까지의 경로"는 노드마다 다른 값이어야 하는데, 하나뿐인 변수로는 그걸 표현할 수 없었다.

해결책은 이 값을 함수의 **매개변수**로 만드는 것이었다. `DFS(node, path_max)`처럼 인자로 받으면, `DFS(node.left, path_max)`와 `DFS(node.right, path_max)`는 서로 다른 호출이 되어 각자 자기만의 `path_max` 사본을 갖는다. 왼쪽 호출이 그 값을 어떻게 바꾸든 오른쪽 호출에는 영향을 주지 않는다. `goodNodes(self, root)`라는 원래 시그니처는 그대로 두고 싶어서, 안에 인자 두 개짜리 `DFS`를 지역 함수로 선언하고 `goodNodes`는 이 함수를 초기값과 함께 한 번 호출한 뒤 결과만 돌려주는 구조로 만들었다.

반대로 개수를 세는 `GN_cnt`는 여러 재귀 호출에 걸쳐 계속 누적돼야 하는 값이다. `DFS`가 `goodNodes`의 지역 변수인 `GN_cnt`를 안에서 바꾸려면 `nonlocal GN_cnt` 선언이 필요하다. 이게 없으면 파이썬은 `GN_cnt += 1`이라는 대입문을 보는 순간 `GN_cnt`를 `DFS`만의 새 지역 변수로 확정해버려서 `UnboundLocalError`가 난다. `nonlocal`은 "이 이름은 내가 선언한 게 아니라 바깥 함수의 것을 그대로 쓰겠다"고 알려주는 선언이다.

시간 복잡도는 `O(n)`이다. 모든 노드를 한 번씩 방문한다. 공간 복잡도는 재귀 호출 스택 깊이만큼인 `O(h)`이고, `h`는 트리의 높이다. 한쪽으로만 이어진 트리에서는 `O(n)`, 균형 잡힌 트리에서는 `O(log n)`이 된다.

풀면서 걸렸던 부분은 다음과 같았다.

- 처음에는 재귀 호출을 `self.DFS(node.left)`처럼 썼다. `DFS`는 `goodNodes` 안에 선언한 지역 함수일 뿐 클래스 메서드가 아닌데, 둘을 혼동했다.
- `path_max`를 갱신해놓고도 정작 자식 호출에 인자로 넘기는 걸 빠뜨려서, 한동안 `DFS(node.left)`처럼 인자가 하나 모자란 채로 호출했다.
- LeetCode에서 실행했을 때 `nonlocal` 줄에서 `SyntaxError: invalid syntax`가 났다. 코드 자체는 문제가 없었고, 원인은 언어 선택이 Python2로 되어 있었던 것이었다. `nonlocal`은 Python3에만 있는 키워드라 Python2는 그 이름 자체를 못 읽는다. Python3로 바꾸니 바로 해결됐다.

### 더 개선한다면

지금 코드는 `nonlocal`로 바깥 함수의 변수를 직접 바꾸는 방식이라 동작은 하지만, `DFS`가 만들어내는 결과가 오직 부수효과(`GN_cnt`를 바꾸는 것)로만 드러난다. `DFS` 호출 하나만 떼어놓고 보면 "이 서브트리 안에 good node가 몇 개 있는지"를 스스로 알려주지 않는다. 이걸 각 호출이 자기 서브트리의 개수를 직접 `return`하고, 그 값을 부모가 더해서 위로 올려보내는 방식으로 바꾸면 `nonlocal`도 공유 변수도 필요 없어진다.

```python
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def DFS(node, path_max):
            if node is None:
                return 0

            count = 1 if node.val >= path_max else 0
            path_max = max(path_max, node.val)

            return count + DFS(node.left, path_max) + DFS(node.right, path_max)

        return DFS(root, float('-inf'))
```

시간·공간 복잡도는 그대로 `O(n)`, `O(h)`다. 달라진 건 상태를 어디에 두느냐뿐이다. 각 호출이 정수 하나를 돌려주고 그걸 셋(자기 자신, 왼쪽, 오른쪽) 더하는 형태라, 재귀 호출 하나하나가 "이 서브트리의 답"이라는 분명한 의미를 갖는다. 세 값을 더하는 연산이 매 호출마다 하나씩 더 생기긴 하지만 상수 시간이라 전체 복잡도에는 영향이 없다.

## 2. 스스로 묻고 답한 질문들

### Q. 최댓값을 전역 변수나 클래스 속성으로 관리하면 왜 안 되는가?

전역 변수나 클래스 속성은 트리 전체에서 딱 하나만 존재한다. 그런데 "루트에서 X까지의 경로 최댓값"은 노드마다 다른 값이어야 한다. 왼쪽 서브트리를 탐색하며 그 값을 바꿔놓으면, 나중에 오른쪽 서브트리로 넘어갔을 때도 바뀐 값이 그대로 남아 있어서 경로가 뒤섞인다. 함수의 매개변수로 넘기면 호출마다 독립된 값이 생기기 때문에 이 문제가 사라진다.

### Q. 함수 안에서 변수에 값을 대입했을 뿐인데 왜 `UnboundLocalError`가 나는가?

파이썬은 함수를 실행하기 전에 그 함수 안 어딘가에 `이름 = 값` 형태의 대입이 있는지 먼저 훑는다. 하나라도 있으면 그 이름은 함수 전체에서 지역 변수로 취급된다. 대입이 함수의 중간이나 `if` 문 안에 있어도 마찬가지다. 그래서 `GN_cnt += 1`이라는 대입문이 있는 순간, 그 위에서 `GN_cnt`를 읽으려는 코드도 이미 "아직 값이 없는 지역 변수"를 읽는 셈이 되어 에러가 난다.

### Q. `nonlocal`은 `global`과 뭐가 다른가?

`global`은 모듈 최상단의 전역 변수를 함수 안에서 바꾸겠다는 선언이고, `nonlocal`은 자신을 둘러싼 바깥 **함수**의 지역 변수를 바꾸겠다는 선언이다. 이 문제처럼 함수 안에 함수를 선언하는 구조(클로저)에서, 안쪽 함수가 바깥 함수의 변수를 읽는 건 선언 없이도 되지만 값을 바꾸려면 `nonlocal`이 필요하다.

### Q. 로컬에서는 되던 코드가 왜 LeetCode에서는 `SyntaxError`가 났는가?

`nonlocal`이라는 키워드 자체가 Python3에만 있어서다. LeetCode는 언어를 Python(2)과 Python3 중에 고를 수 있는데, Python2가 선택된 상태였다. 로컬 환경의 `python` 명령은 Python3를 가리키고 있어서 같은 코드가 문제없이 돌아갔고, 언어 선택을 Python3로 바꾸자 바로 해결됐다. 알고리즘은 처음부터 맞았는데 실행 환경 설정 때문에 막혔던 경우다.

## 정리하며

이번 문제를 풀면서 가장 크게 잡힌 건 재귀 호출에서 "아래로 내려보내는 값"과 "위로 올려보내는 값"을 구분하는 감각이다. 경로의 최댓값처럼 호출마다 달라야 하는 값은 매개변수로 내려보내고, 개수처럼 여러 호출의 결과를 합쳐야 하는 값은 `nonlocal`로 옆에서 누적하거나 `return`으로 위로 올려보내는 두 가지 방법이 있다는 것도 정리됐다. 함수 안에서 대입이 있으면 그 이름이 통째로 지역 변수가 된다는 파이썬의 스코프 규칙, 그리고 `nonlocal`이 Python3 전용이라 언어 설정에 따라 같은 코드도 다르게 동작할 수 있다는 점도 이번에 확실히 짚고 넘어갔다.
