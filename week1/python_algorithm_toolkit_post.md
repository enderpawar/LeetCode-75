# [Python Algorithm] Built-in Functions, Data Structures, Templates

LeetCode 75 Week 1을 풀면서 `range()`, `sum()`, 문자열 슬라이싱, `dict.get()`, 집합, `deque`처럼 자주 쓰는 기능이 하나씩 등장했다. 문제의 핵심 알고리즘을 알고 있어도 함수의 반환값이나 자료구조의 연산 비용을 정확히 모르면 코드가 불필요하게 길어지거나 시간 초과가 날 수 있었다.

이번 글에서는 Week 1에서 사용한 기능을 출발점으로 삼되, 이후 배열, 문자열, 해시, 그래프, 최단 경로, 동적 계획법 문제에서 반복해서 사용할 Python 도구까지 범위를 넓혀 정리했다. 모든 Python 문법을 나열하기보다는 알고리즘 문제를 풀 때 실제로 자주 꺼내 쓰는 기능, 사용 방법, 시간 복잡도, 주의점을 한곳에 모으는 데 집중했다.

## 1. 입력과 출력

LeetCode에서는 메서드의 인자로 입력이 들어오므로 직접 입력을 받을 일이 거의 없다. 반면 백준과 같은 플랫폼에서는 문자열로 들어온 입력을 원하는 타입으로 변환해야 한다.

### `input()`과 `sys.stdin.readline()`

```python
name = input()
```

`input()`은 한 줄을 읽고 마지막 줄바꿈 문자를 제거한 문자열을 반환한다. 입력량이 많다면 `sys.stdin.readline()`이 더 빠르다.

```python
import sys

line = sys.stdin.readline().rstrip()
```

`readline()`은 줄 끝의 `\n`까지 읽으므로 필요하면 `rstrip()`으로 제거한다. 숫자를 바로 변환할 때는 공백과 줄바꿈을 `int()`가 처리하므로 `rstrip()`이 없어도 된다.

```python
import sys

n = int(sys.stdin.readline())
```

### `split()`과 `map()`

공백으로 구분된 정수는 다음 형태가 가장 자주 쓰인다.

```python
a, b = map(int, input().split())
numbers = list(map(int, input().split()))
```

`split()`은 문자열을 나눈 리스트를 만들고, `map(int, ...)`은 각 문자열에 `int()`를 적용한다. `map` 객체는 필요한 값을 지연해서 만들기 때문에 인자 언패킹에는 그대로 사용할 수 있지만, 인덱싱하거나 여러 번 순회하려면 `list()`로 변환해야 한다.

```python
values = map(int, ["1", "2", "3"])

# values[0]  # TypeError: map 객체는 인덱싱할 수 없음
numbers = list(values)  # [1, 2, 3]
```

여러 줄을 한 번에 읽어야 할 때는 전체 입력을 토큰 단위로 나눌 수도 있다.

```python
import sys

tokens = iter(sys.stdin.buffer.read().split())
n = int(next(tokens))
numbers = [int(next(tokens)) for _ in range(n)]
```

### `print()`, 언패킹, `join()`

```python
answer = [1, 2, 3]

print(*answer)             # 1 2 3
print(*answer, sep=",")    # 1,2,3
print(" ".join(map(str, answer)))  # 1 2 3
```

`print(*answer)`는 리스트의 원소를 각각의 인자로 풀어 전달한다. `join()`은 문자열만 이어 붙일 수 있으므로 정수 리스트는 먼저 `map(str, answer)`로 변환한다. 출력할 줄이 매우 많다면 한 줄씩 `print()`하기보다 문자열을 모아 한 번에 출력하는 편이 빠르다.

```python
lines = ["YES", "NO", "YES"]
print("\n".join(lines))
```

## 2. 반복과 순회에 쓰는 기본 함수

### `range()`

`range(start, stop, step)`은 `start`부터 시작해 `stop` 직전까지 `step`만큼 변하는 정수를 만든다.

```python
list(range(5))          # [0, 1, 2, 3, 4]
list(range(2, 6))       # [2, 3, 4, 5]
list(range(5, 0, -1))   # [5, 4, 3, 2, 1]
```

마지막 값 `stop`은 포함되지 않는다. 역순 반복에서는 음수 `step`이 필요하다.

```python
for i in range(len(numbers) - 1, -1, -1):
    print(numbers[i])
```

반복 횟수만 중요하고 인덱스를 사용하지 않을 때는 `_`를 쓴다.

```python
for _ in range(3):
    do_something()
```

### `enumerate()`

값과 인덱스가 모두 필요하면 `range(len(...))`보다 `enumerate()`가 의도를 더 잘 드러낸다.

```python
for index, value in enumerate(numbers):
    print(index, value)

for index, value in enumerate(numbers, start=1):
    print(index, value)
```

### `zip()`

여러 순회 가능한 객체의 같은 위치에 있는 값을 묶는다.

```python
names = ["A", "B", "C"]
scores = [90, 80, 70]

for name, score in zip(names, scores):
    print(name, score)
```

기본 `zip()`은 가장 짧은 입력이 끝나면 멈춘다. 길이가 달라도 끝까지 묶어야 한다면 `itertools.zip_longest()`를 사용한다.

```python
from itertools import zip_longest

list(zip_longest([1, 2], ["a"], fillvalue=None))
# [(1, "a"), (2, None)]
```

2차원 리스트를 전치할 때도 사용할 수 있다.

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
]

transposed = [list(row) for row in zip(*matrix)]
# [[1, 4], [2, 5], [3, 6]]
```

### `reversed()`와 슬라이싱

```python
numbers = [1, 2, 3]

list(reversed(numbers))  # [3, 2, 1]
numbers[::-1]            # [3, 2, 1]
```

`reversed(numbers)`는 역순 반복자를 반환하고 원본을 바꾸지 않는다. `numbers[::-1]`은 역순의 새 리스트를 만든다. 리스트 자체를 제자리에서 뒤집으려면 `numbers.reverse()`를 사용한다.

### `any()`와 `all()`

`any()`는 하나라도 참이면 `True`, `all()`은 모두 참이면 `True`를 반환한다.

```python
numbers = [2, 4, 5]

any(number % 2 == 1 for number in numbers)  # True
all(number > 0 for number in numbers)       # True
```

빈 반복 객체에 대해 `any([])`는 `False`, `all([])`는 `True`다.

## 3. 숫자 계산에 자주 쓰는 내장 함수

```python
numbers = [3, -1, 7, 2]

len(numbers)       # 4
sum(numbers)       # 11
min(numbers)       # -1
max(numbers)       # 7
abs(-5)            # 5
```

`sum()`, `min()`, `max()`는 원소를 순회하므로 리스트 길이를 `n`이라고 할 때 `O(n)`이다. 같은 반복문 안에서 매번 호출하면 의도치 않게 `O(n²)`이 될 수 있다.

```python
# 매번 max(numbers)를 다시 계산함
for number in numbers:
    if number == max(numbers):
        print(number)

# 한 번만 계산
maximum = max(numbers)
for number in numbers:
    if number == maximum:
        print(number)
```

### `divmod()`, 몫과 나머지

```python
quotient, remainder = divmod(17, 5)
# quotient = 3, remainder = 2

17 // 5  # 3
17 % 5   # 2
```

좌표를 행과 열로 바꾸거나 시간을 시·분·초로 분리할 때 편리하다.

```python
row, column = divmod(index, width)
```

### `pow()`

```python
pow(2, 10)       # 1024
pow(2, 10, 1000) # 24
```

세 번째 인자를 사용한 `pow(base, exponent, mod)`는 큰 거듭제곱을 전부 만든 뒤 나누지 않고 모듈러 거듭제곱을 효율적으로 계산한다.

### 올림 나눗셈과 반올림

양의 정수 `a`를 양의 정수 `b`로 나눈 값을 올림할 때는 다음 공식을 자주 사용한다.

```python
ceiling = (a + b - 1) // b
```

부호와 관계없이 일반적인 정수 올림 나눗셈이 필요하면 `-(-a // b)` 형태를 사용할 수 있다.

```python
ceiling = -(-a // b)
```

`round()`는 정확히 `.5`일 때 항상 위쪽 정수로 올리는 함수가 아니다. Python은 가장 가까운 짝수 쪽을 선택하는 방식을 사용한다.

```python
round(2.5)  # 2
round(3.5)  # 4
round(3.14159, 2)  # 3.14
```

문제에서 요구하는 반올림 규칙이 무엇인지 확인한 뒤 `round()`, `math.floor()`, `math.ceil()` 가운데 맞는 것을 선택해야 한다.

### 무한대

최솟값을 갱신할 때 충분히 큰 임의의 정수 대신 무한대를 사용할 수 있다.

```python
distance = float("inf")
negative_infinity = float("-inf")
```

### 진법 변환과 비트 연산

문자열을 특정 진법의 정수로 바꾸거나 정수를 2진수, 8진수, 16진수 문자열로 표현할 수 있다.

```python
int("1011", 2)  # 11
int("ff", 16)   # 255

bin(11)  # "0b1011"
oct(11)  # "0o13"
hex(255) # "0xff"
```

접두사가 필요 없다면 슬라이싱한다.

```python
binary = bin(11)[2:]  # "1011"
```

기본 비트 연산자는 다음과 같다.

```python
a = 0b1010
b = 0b1100

a & b   # AND: 0b1000
a | b   # OR:  0b1110
a ^ b   # XOR: 0b0110
~a      # NOT
a << 1  # 왼쪽 이동: 0b10100
a >> 1  # 오른쪽 이동: 0b0101
```

`1 << index`는 `index`번 비트만 켠 값이다.

```python
mask = 0
mask |= 1 << 3            # 3번 비트 켜기
is_set = mask & (1 << 3)  # 3번 비트 확인
mask &= ~(1 << 3)         # 3번 비트 끄기
mask ^= 1 << 3            # 3번 비트 뒤집기
```

정수에 켜진 비트 수는 `bit_count()`로 셀 수 있다.

```python
(0b101101).bit_count()  # 4
```

`x & (x - 1)`은 가장 낮은 위치의 켜진 비트 하나를 지운다. 양의 정수가 2의 거듭제곱인지 확인할 때도 사용할 수 있다.

```python
is_power_of_two = x > 0 and (x & (x - 1)) == 0
```

## 4. 리스트와 튜플

### 리스트 생성과 컴프리헨션

```python
zeros = [0] * 5
squares = [number * number for number in range(5)]
evens = [number for number in range(10) if number % 2 == 0]
```

2차원 리스트를 만들 때는 같은 내부 리스트를 공유하지 않도록 주의해야 한다.

```python
# 잘못된 방식: 세 행이 같은 리스트를 가리킴
board = [[0] * 3] * 3
board[0][0] = 1
# [[1, 0, 0], [1, 0, 0], [1, 0, 0]]

# 올바른 방식: 행마다 새 리스트 생성
board = [[0] * 3 for _ in range(3)]
```

### 추가와 삭제

```python
numbers = [1, 2]

numbers.append(3)       # [1, 2, 3]
numbers.extend([4, 5])  # [1, 2, 3, 4, 5]
numbers.insert(1, 9)    # [1, 9, 2, 3, 4, 5]

last = numbers.pop()    # 마지막 값 제거 후 반환
value = numbers.pop(1)  # 1번 인덱스 값 제거 후 반환
numbers.remove(3)       # 값 3을 처음 발견한 위치에서 제거
numbers.clear()         # 모든 원소 제거
```

`append([4, 5])`는 리스트 자체를 원소 하나로 넣고, `extend([4, 5])`는 4와 5를 각각 추가한다.

```python
values = [1]
values.append([2, 3])  # [1, [2, 3]]

values = [1]
values.extend([2, 3])  # [1, 2, 3]
```

리스트 끝의 `append()`와 `pop()`은 분할 상환 `O(1)`이다. 앞이나 중간에 값을 넣고 지우면 뒤 원소들을 이동해야 하므로 `O(n)`이다.

### 검색과 개수

```python
numbers = [4, 2, 2, 7]

2 in numbers       # True
9 not in numbers   # True
numbers.count(2)   # 2
numbers.index(7)   # 3
```

리스트의 `in`, `count()`, `index()`는 앞에서부터 값을 찾으므로 `O(n)`이다. 포함 여부를 반복 검사한다면 집합으로 바꾸는 것이 유리할 수 있다.

### 슬라이싱

```python
numbers = [0, 1, 2, 3, 4, 5]

numbers[1:4]   # [1, 2, 3]
numbers[:3]    # [0, 1, 2]
numbers[3:]    # [3, 4, 5]
numbers[::2]   # [0, 2, 4]
numbers[::-1]  # [5, 4, 3, 2, 1, 0]
```

슬라이싱은 `start`를 포함하고 `stop`을 포함하지 않는다. 리스트 슬라이싱은 선택한 원소 수만큼의 새 리스트를 만들기 때문에 시간과 공간이 모두 `O(k)`다.

### 튜플과 언패킹

튜플은 생성된 뒤 원소를 바꿀 수 없는 자료구조다. 좌표, 간선, 여러 반환값처럼 하나의 묶음으로 유지할 값에 자주 사용한다.

```python
point = (3, 5)
x, y = point

a, b = b, a  # 임시 변수 없이 교환
```

튜플은 해시 가능한 원소로만 구성되면 딕셔너리 키나 집합 원소로 사용할 수 있다.

```python
visited = {(0, 0), (1, 2)}
```

## 5. 문자열

문자열은 수정할 수 없는 불변 객체다. 특정 문자를 바꾸려면 새 문자열을 만들거나 리스트로 변환한 뒤 다시 합쳐야 한다.

```python
text = "code"
characters = list(text)
characters[0] = "m"
result = "".join(characters)  # "mode"
```

### 분리하고 합치기

```python
text = "  learn   python  "

text.split()       # ["learn", "python"]
text.split(" ")    # 빈 문자열도 포함될 수 있음
"-".join(["a", "b", "c"])  # "a-b-c"
```

인자 없는 `split()`은 연속된 공백을 하나의 구분처럼 처리하고 앞뒤 공백도 무시한다. `" ".split(" ")`처럼 구분자를 직접 전달하면 동작이 다르다.

### 공백과 문자 제거

```python
text = "  hello\n"

text.strip()   # "hello"
text.lstrip()  # "hello\n"
text.rstrip()  # "  hello"
```

인자를 전달하면 문자열의 정확한 접두사나 접미사가 아니라, 양 끝에 있는 해당 문자들의 집합을 제거한다.

```python
"www.example.com".strip("w.com")  # "example"
```

정확한 접두사와 접미사를 제거하려면 `removeprefix()`와 `removesuffix()`를 사용한다.

```python
"unhappy".removeprefix("un")       # "happy"
"report.txt".removesuffix(".txt")  # "report"
```

### 찾기와 검사

```python
text = "algorithm"

text.find("go")       # 2
text.find("python")   # -1
text.index("go")      # 2
text.count("o")       # 1
text.startswith("algo")  # True
text.endswith("thm")     # True
```

`find()`는 없으면 `-1`을 반환하지만, `index()`는 `ValueError`를 발생시킨다.

```python
"123".isdigit()      # True
"abc".isalpha()      # True
"abc123".isalnum()   # True
"   ".isspace()      # True
"ABC".isupper()      # True
"abc".islower()      # True
```

### 치환과 대소문자

```python
"banana".replace("a", "o")  # "bonono"
"Python".lower()             # "python"
"Python".upper()             # "PYTHON"
"hello world".title()        # "Hello World"
```

이 메서드들은 원본 문자열을 바꾸지 않고 새 문자열을 반환한다.

### 문자 코드

```python
ord("A")  # 65
chr(65)   # "A"
```

알파벳을 0부터 25까지의 인덱스로 바꿀 때 사용할 수 있다.

```python
index = ord(character) - ord("a")
character = chr(index + ord("a"))
```

## 6. 딕셔너리와 집합

### 딕셔너리

딕셔너리는 `키 → 값` 관계를 저장한다. 빈도수, 마지막으로 본 위치, 노드별 거리처럼 값에 다른 정보를 연결할 때 사용한다.

```python
counts = {}

for number in numbers:
    counts[number] = counts.get(number, 0) + 1
```

`get(key, default)`은 키가 있으면 값을, 없으면 기본값을 반환한다. 조회만 할 뿐 딕셔너리를 직접 수정하지는 않는다. 위 코드는 반환값에 1을 더한 뒤 `counts[number]`에 다시 대입하기 때문에 갱신된다.

```python
counts.keys()    # 키를 보는 뷰
counts.values()  # 값을 보는 뷰
counts.items()   # (키, 값) 쌍을 보는 뷰
```

```python
for key, value in counts.items():
    print(key, value)
```

그 밖에 자주 쓰는 메서드는 다음과 같다.

```python
data = {"a": 1}

data.setdefault("b", 0)  # 키가 없으면 b: 0을 추가하고 0 반환
value = data.pop("a")     # 키를 제거하고 값 반환
data.update({"c": 3})     # 여러 키와 값 갱신
```

딕셔너리의 키 조회, 삽입, 삭제는 평균 `O(1)`이다. 최악의 이론적 경우는 `O(n)`이지만 일반적인 알고리즘 복잡도 분석에서는 평균 `O(1)`로 본다.

### 집합

집합은 중복 없는 값을 저장하고 포함 여부를 평균 `O(1)`에 검사한다.

```python
seen = set()

seen.add(3)
seen.add(3)       # 중복 추가는 변화 없음
seen.remove(3)    # 없으면 KeyError
seen.discard(3)   # 없어도 오류 없음
```

집합 연산은 다음과 같다.

```python
a = {1, 2, 3}
b = {3, 4}

a | b   # 합집합: {1, 2, 3, 4}
a & b   # 교집합: {3}
a - b   # 차집합: {1, 2}
a ^ b   # 대칭 차집합: {1, 2, 4}

a <= b  # a가 b의 부분 집합인지
a >= b  # a가 b의 상위 집합인지
```

빈 집합은 `{}`가 아니라 `set()`으로 만든다. `{}`는 빈 딕셔너리다.

### `Counter`와 `defaultdict`

빈도수를 셀 때는 `collections.Counter`를 사용할 수 있다.

```python
from collections import Counter

counts = Counter(["a", "b", "a"])
counts["a"]           # 2
counts["missing"]     # 0
counts.most_common(1) # [("a", 2)]
```

`Counter`끼리는 빈도수 기준의 덧셈, 뺄셈, 교집합, 합집합도 가능하다. 결과에서 0 이하의 빈도는 제거된다.

```python
left = Counter("aab")
right = Counter("abb")

left + right  # Counter({"a": 3, "b": 3})
left - right  # Counter({"a": 1})
left & right  # 각 키의 최솟값
left | right  # 각 키의 최댓값
```

`defaultdict`는 없는 키를 조회할 때 기본값을 자동으로 만든다. 그래프의 인접 리스트나 그룹핑에 편리하다.

```python
from collections import defaultdict

graph = defaultdict(list)
graph[1].append(2)
graph[1].append(3)

groups = defaultdict(int)
groups["a"] += 1
```

단순 빈도수라면 `Counter`, 키마다 리스트를 모은다면 `defaultdict(list)`, 기본 동작을 명시적으로 보이고 싶다면 일반 딕셔너리와 `get()`을 선택할 수 있다.

## 7. 정렬과 이진 탐색

### `sort()`와 `sorted()`

```python
numbers = [3, 1, 2]

numbers.sort()          # 원본을 정렬, 반환값은 None
new_numbers = sorted(numbers)  # 새 리스트 반환
```

두 방식 모두 일반적인 시간 복잡도는 `O(n log n)`이다. `list.sort()`는 원본을 바꾸고, `sorted()`는 모든 반복 가능한 객체를 받아 정렬된 새 리스트를 만든다.

```python
words = ["bbb", "a", "cc"]

words.sort(key=len)                  # 길이 기준
words.sort(key=lambda word: (len(word), word))  # 길이, 사전순
words.sort(reverse=True)             # 내림차순
```

튜플을 키로 반환하면 첫 번째 기준이 같을 때 두 번째 기준을 사용한다. 일부 기준만 내림차순으로 만들고 싶다면 숫자에 음수를 붙이는 방식이 자주 쓰인다.

```python
records = [("A", 90), ("B", 80), ("C", 90)]
records.sort(key=lambda item: (-item[1], item[0]))
# 점수는 내림차순, 이름은 오름차순
```

### `min()`과 `max()`의 `key`

```python
words = ["algorithm", "py", "code"]

shortest = min(words, key=len)  # "py"
longest = max(words, key=len)   # "algorithm"
```

`key`는 비교에 사용할 값을 계산할 뿐, 반환값은 원래 원소다.

### `bisect`

정렬된 리스트에서 이진 탐색으로 삽입 위치를 찾는다.

```python
from bisect import bisect_left, bisect_right, insort

numbers = [1, 2, 2, 2, 4]

bisect_left(numbers, 2)   # 1
bisect_right(numbers, 2)  # 4
```

`bisect_left()`는 같은 값들의 가장 왼쪽, `bisect_right()`는 가장 오른쪽 다음 위치를 반환한다. 따라서 특정 값의 개수도 구할 수 있다.

```python
count_two = bisect_right(numbers, 2) - bisect_left(numbers, 2)
```

탐색은 `O(log n)`이지만 리스트 중간에 실제로 삽입하는 `insort()`는 뒤 원소들을 이동해야 하므로 전체 `O(n)`이다.

```python
insort(numbers, 3)
```

## 8. Stack, Queue, Deque, Heap

### 리스트로 스택 구현하기

스택은 마지막에 넣은 값을 먼저 꺼내는 LIFO 구조다. Python에서는 리스트의 오른쪽 끝을 사용하면 된다.

```python
stack = []

stack.append(10)  # push
stack.append(20)
top = stack[-1]   # 제거하지 않고 확인
value = stack.pop()  # 20
```

`append()`와 마지막 원소 `pop()`은 분할 상환 `O(1)`이다.

### `deque`로 큐 구현하기

큐는 먼저 넣은 값을 먼저 꺼내는 FIFO 구조다.

```python
from collections import deque

queue = deque()

queue.append(10)
queue.append(20)
front = queue[0]
value = queue.popleft()  # 10
```

리스트의 `pop(0)`은 `O(n)`이지만 `deque.popleft()`는 `O(1)`이다. 양쪽 끝에서 값을 다룰 때는 `deque`를 사용한다.

```python
values = deque([2, 3])

values.append(4)
values.appendleft(1)
values.pop()
values.popleft()
values.extend([5, 6])
values.extendleft([0, -1])  # 전달 순서가 뒤집혀 왼쪽에 추가됨
values.rotate(1)            # 오른쪽으로 한 칸 회전
values.rotate(-1)           # 왼쪽으로 한 칸 회전
```

### `heapq`로 우선순위 큐 구현하기

`heapq`는 가장 작은 값을 빠르게 꺼내는 최소 힙이다.

```python
import heapq

heap = []

heapq.heappush(heap, 3)
heapq.heappush(heap, 1)
heapq.heappush(heap, 2)

smallest = heap[0]          # 제거하지 않고 최솟값 확인
value = heapq.heappop(heap) # 1
```

삽입과 삭제는 `O(log n)`, 최솟값 확인은 `O(1)`이다. 기존 리스트를 힙으로 바꾸는 `heapify()`는 `O(n)`이다.

```python
numbers = [5, 2, 8, 1]
heapq.heapify(numbers)
```

전체를 정렬하지 않고 가장 작거나 큰 `k`개만 구할 때는 `nsmallest()`와 `nlargest()`를 사용할 수 있다.

```python
heapq.nsmallest(2, [5, 1, 4, 2, 3])  # [1, 2]
heapq.nlargest(2, [5, 1, 4, 2, 3])   # [5, 4]
```

`k`가 전체 길이에 비해 작을 때 유용하다. 전체 순서가 필요하다면 `sorted()`가 더 자연스럽다.

최대 힙이 필요할 때는 값의 부호를 바꾸어 저장하는 방식이 여러 Python 실행 환경에서 호환된다.

```python
max_heap = []

heapq.heappush(max_heap, -10)
heapq.heappush(max_heap, -30)
heapq.heappush(max_heap, -20)

largest = -heapq.heappop(max_heap)  # 30
```

우선순위와 실제 데이터를 함께 넣을 때는 튜플을 사용한다.

```python
heap = []
heapq.heappush(heap, (2, "task B"))
heapq.heappush(heap, (1, "task A"))

priority, task = heapq.heappop(heap)
```

튜플은 앞 원소부터 비교하므로 우선순위가 같으면 두 번째 원소를 비교한다. 두 번째 원소끼리 비교할 수 없는 객체라면 고유 번호를 중간에 넣어 충돌을 피할 수 있다.

## 9. 조합과 누적 계산에 쓰는 표준 라이브러리

### `itertools`

순열은 순서가 중요하고, 조합은 순서가 중요하지 않다.

```python
from itertools import combinations, permutations, product

items = [1, 2, 3]

list(permutations(items, 2))
# [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]

list(combinations(items, 2))
# [(1, 2), (1, 3), (2, 3)]

list(product([0, 1], repeat=2))
# [(0, 0), (0, 1), (1, 0), (1, 1)]
```

중복 선택이 가능한 조합은 `combinations_with_replacement()`를 사용한다.

```python
from itertools import combinations_with_replacement

list(combinations_with_replacement([1, 2, 3], 2))
# [(1, 1), (1, 2), (1, 3), (2, 2), (2, 3), (3, 3)]
```

경우의 수가 매우 빠르게 증가하므로 편리하다는 이유만으로 큰 입력에 사용하면 안 된다. 순열 개수는 `n!`, 길이 `r`의 순열은 `nPr`이다.

여러 반복 객체를 하나로 이어 순회할 때는 `chain()`을 사용할 수 있다.

```python
from itertools import chain

list(chain([1, 2], [3, 4]))  # [1, 2, 3, 4]
```

정렬된 값의 연속된 그룹을 묶을 때는 `groupby()`가 유용하다.

```python
from itertools import groupby

values = [1, 1, 2, 2, 2, 3]
groups = [(key, len(list(group))) for key, group in groupby(values)]
# [(1, 2), (2, 3), (3, 1)]
```

`groupby()`는 같은 값이 연속한 구간만 묶으므로, 전체에서 같은 값을 모으려면 먼저 정렬하거나 `Counter`를 사용해야 한다.

### `accumulate`

```python
from itertools import accumulate

numbers = [1, 2, 3, 4]
prefix = list(accumulate(numbers))
# [1, 3, 6, 10]
```

구간 합 공식을 편하게 쓰려면 맨 앞에 0을 붙인다.

```python
prefix = [0] + list(accumulate(numbers))

# numbers[left:right + 1]의 합
range_sum = prefix[right + 1] - prefix[left]
```

### `math`

```python
import math

math.gcd(12, 18)     # 6
math.lcm(12, 18)     # 36
math.isqrt(20)       # 4
math.sqrt(20)        # 4.472...
math.ceil(3.2)       # 4
math.floor(3.8)      # 3
math.factorial(5)    # 120
```

정수 제곱근이 필요하면 부동소수점 오차가 없는 `isqrt()`가 알맞다.

### `functools.cache`

같은 상태의 재귀 결과를 다시 계산하지 않도록 메모이제이션할 수 있다.

```python
from functools import cache


@cache
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
```

인자는 딕셔너리 키처럼 해시 가능해야 한다. 리스트 상태를 캐시에 넣어야 한다면 튜플로 변환하는 방법을 고려한다.

## 10. 반복해서 쓰는 알고리즘 템플릿

함수를 외우는 것만큼 중요한 것은 어떤 문제에서 어떤 자료구조와 함께 사용하는지 연결하는 것이다.

### Prefix Sum

여러 구간의 합을 반복해서 구할 때 사용한다.

```python
numbers = [2, 4, 1, 3]
prefix = [0]

for number in numbers:
    prefix.append(prefix[-1] + number)


def range_sum(left, right):
    return prefix[right + 1] - prefix[left]
```

전처리는 `O(n)`, 각 구간 합은 `O(1)`이다.

### Two Pointers

양 끝이나 서로 다른 두 위치를 한 방향으로 이동시키며 탐색한다.

```python
left = 0
right = len(numbers) - 1

while left < right:
    current = numbers[left] + numbers[right]

    if current == target:
        break
    if current < target:
        left += 1
    else:
        right -= 1
```

각 포인터가 한 방향으로만 움직이면 전체 시간은 보통 `O(n)`이다. 두 수의 합 템플릿은 배열이 정렬되어 있다는 조건이 필요하다.

### Sliding Window

연속된 구간을 유지하면서 오른쪽 값을 추가하고 왼쪽 값을 제거한다.

```python
window_sum = sum(numbers[:k])
best = window_sum

for right in range(k, len(numbers)):
    window_sum += numbers[right]
    window_sum -= numbers[right - k]
    best = max(best, window_sum)
```

길이 `k`인 모든 구간의 합을 매번 `sum()`으로 다시 구하면 `O(nk)`지만, 이전 합을 갱신하면 `O(n)`이다.

### Binary Search

정답 후보가 단조롭게 참과 거짓으로 나뉘면 값 자체를 이진 탐색할 수 있다.

```python
left = minimum_answer
right = maximum_answer

while left <= right:
    middle = (left + right) // 2

    if feasible(middle):
        answer = middle
        right = middle - 1
    else:
        left = middle + 1
```

이 형태는 조건을 만족하는 가장 작은 값을 찾는다. 가장 큰 값을 찾을 때는 조건이 참인 경우 `left = middle + 1`로 방향이 바뀐다. 핵심은 `feasible()`의 결과가 한 번만 바뀌는 단조성을 확인하는 것이다.

### BFS

가중치가 없는 그래프의 최단 거리나 격자 탐색에는 큐를 사용한다.

```python
from collections import deque

queue = deque([start])
visited = {start}

while queue:
    node = queue.popleft()

    for next_node in graph[node]:
        if next_node in visited:
            continue

        visited.add(next_node)
        queue.append(next_node)
```

방문 표시는 큐에 넣을 때 해야 같은 노드가 여러 번 들어가는 일을 막을 수 있다. 인접 리스트를 사용하면 시간 복잡도는 `O(V + E)`다.

격자에서는 방향 배열을 함께 사용한다.

```python
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for dr, dc in directions:
    next_row = row + dr
    next_column = column + dc

    if 0 <= next_row < rows and 0 <= next_column < columns:
        pass
```

### DFS

재귀 또는 스택으로 깊이 우선 탐색을 구현한다.

```python
def dfs(node):
    visited.add(node)

    for next_node in graph[node]:
        if next_node not in visited:
            dfs(next_node)
```

입력이 깊은 연결 리스트 형태에 가까우면 Python의 재귀 깊이 제한에 걸릴 수 있다. 반복문으로 바꾸거나, 플랫폼이 허용하는 범위에서 제한을 조절한다.

```python
import sys

sys.setrecursionlimit(200_000)
```

재귀 제한을 크게 설정한다고 호출 스택 메모리 문제가 사라지는 것은 아니다. 단순 탐색이라면 명시적인 스택이 더 안전할 수 있다.

```python
stack = [start]
visited = {start}

while stack:
    node = stack.pop()

    for next_node in graph[node]:
        if next_node not in visited:
            visited.add(next_node)
            stack.append(next_node)
```

### Dijkstra

음수가 없는 가중치 그래프의 최단 거리는 최소 힙을 사용한다.

```python
import heapq

distance = [float("inf")] * node_count
distance[start] = 0
heap = [(0, start)]

while heap:
    current_distance, node = heapq.heappop(heap)

    if current_distance != distance[node]:
        continue

    for next_node, weight in graph[node]:
        new_distance = current_distance + weight

        if new_distance < distance[next_node]:
            distance[next_node] = new_distance
            heapq.heappush(heap, (new_distance, next_node))
```

힙에는 같은 노드의 예전 거리도 남아 있을 수 있다. 꺼낸 거리가 현재 기록과 다르면 오래된 항목이므로 건너뛴다. 시간 복잡도는 인접 리스트와 힙을 사용할 때 보통 `O((V + E) log V)`로 나타낸다.

### Union-Find

두 원소가 같은 집합에 속하는지 확인하고 집합을 합칠 때 사용한다.

```python
parent = list(range(n))
size = [1] * n


def find(x):
    while x != parent[x]:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x


def union(a, b):
    root_a = find(a)
    root_b = find(b)

    if root_a == root_b:
        return False

    if size[root_a] < size[root_b]:
        root_a, root_b = root_b, root_a

    parent[root_b] = root_a
    size[root_a] += size[root_b]
    return True
```

경로 압축과 크기 기준 합치기를 함께 사용하면 각 연산은 사실상 상수 시간에 가깝다.

### Dynamic Programming

같은 부분 문제의 답을 다시 사용하는 방식이다. 먼저 상태가 무엇인지, 이전 상태에서 어떻게 현재 상태를 만드는지 정한다.

```python
def climb_stairs(n):
    if n <= 2:
        return n

    previous_two = 1
    previous_one = 2

    for _ in range(3, n + 1):
        current = previous_two + previous_one
        previous_two = previous_one
        previous_one = current

    return previous_one
```

모든 상태를 나중에도 사용해야 하면 리스트에 저장하고, 직전 상태 몇 개만 필요하면 변수만 남겨 공간을 줄일 수 있다.

### Backtracking

선택하고, 재귀 호출하고, 선택을 되돌리는 순서가 핵심이다.

```python
result = []
path = []


def backtrack(start):
    if len(path) == target_length:
        result.append(path.copy())
        return

    for index in range(start, len(numbers)):
        path.append(numbers[index])
        backtrack(index + 1)
        path.pop()
```

`result.append(path)`로 저장하면 모든 결과가 같은 리스트 객체를 가리키게 된다. 현재 상태의 복사본인 `path.copy()`를 넣어야 한다.

## 11. 복사, 가변성, 함수 동작

### 대입과 복사는 다르다

```python
original = [1, 2, 3]
alias = original
alias[0] = 9

print(original)  # [9, 2, 3]
```

`alias = original`은 새 리스트를 만들지 않고 같은 객체에 다른 이름을 붙인다.

```python
copied1 = original.copy()
copied2 = original[:]
copied3 = list(original)
```

위 세 방식은 얕은 복사다. 중첩 리스트의 내부 객체까지 독립적으로 복사해야 한다면 `deepcopy()`가 필요하다.

```python
from copy import deepcopy

copied = deepcopy(nested_list)
```

### 제자리 수정 메서드의 반환값

`list.sort()`, `list.reverse()`, `list.append()`, `set.add()`처럼 원본을 바꾸는 메서드는 보통 `None`을 반환한다.

```python
numbers = [3, 1, 2]
result = numbers.sort()

print(numbers)  # [1, 2, 3]
print(result)   # None
```

반대로 `sorted()`, `reversed()`, 문자열 메서드들은 새 결과를 반환한다.

### 함수 인자의 기본값

가변 객체를 기본 인자로 직접 넣으면 호출 사이에 상태가 공유된다.

```python
# 잘못된 방식
def add_value(value, values=[]):
    values.append(value)
    return values


# 안전한 방식
def add_value(value, values=None):
    if values is None:
        values = []
    values.append(value)
    return values
```

### `==`와 `is`

`==`는 값이 같은지 비교하고, `is`는 같은 객체인지 비교한다. `None`은 `is`로 비교한다.

```python
if value is None:
    pass
```

숫자나 문자열의 값 비교에 `is`를 사용하면 안 된다.

### 타입 힌트

```python
from typing import Optional


def find_value(numbers: list[int], target: int) -> Optional[int]:
    for index, number in enumerate(numbers):
        if number == target:
            return index
    return None
```

타입 힌트는 코드의 의도를 설명하지만 일반적으로 실행 중 타입을 강제하지 않는다. `Optional[int]`는 `int` 또는 `None`이 될 수 있다는 뜻이다.

## 12. 주요 연산의 시간 복잡도

자료구조를 고를 때는 코드 길이보다 어떤 연산을 몇 번 실행하는지 먼저 확인해야 한다.

| 자료구조와 연산 | 평균 시간 복잡도 |
|---|---:|
| 리스트 `values[index]` | `O(1)` |
| 리스트 `append()`, 마지막 `pop()` | 분할 상환 `O(1)` |
| 리스트 앞·중간 삽입/삭제 | `O(n)` |
| 리스트 `in`, `count()`, `index()` | `O(n)` |
| 리스트 슬라이싱 `values[a:b]` | `O(k)` |
| 리스트 `sort()`, `sorted()` | `O(n log n)` |
| 딕셔너리 키 조회·삽입·삭제 | 평균 `O(1)` |
| 집합 포함 검사·추가·삭제 | 평균 `O(1)` |
| `deque` 양 끝 추가·삭제 | `O(1)` |
| 힙 최솟값 확인 | `O(1)` |
| 힙 `heappush()`, `heappop()` | `O(log n)` |
| `heapify()` | `O(n)` |
| 정렬된 리스트의 `bisect` 탐색 | `O(log n)` |
| 문자열 또는 리스트 `join()` | 결과 길이에 비례 |

표의 한 연산이 빠르더라도 반복 구조 안에서 몇 번 호출되는지까지 봐야 한다. 예를 들어 리스트의 `in`은 한 번에 `O(n)`이고, 이를 길이 `n`인 반복문 안에서 사용하면 전체가 `O(n²)`이 될 수 있다.

## 13. 스스로 묻고 답한 질문들

### Q. 리스트 컴프리헨션과 제너레이터 표현식은 무엇이 다를까?

대괄호는 모든 결과를 즉시 저장한 리스트를 만들고, 소괄호 형태의 제너레이터 표현식은 값을 필요할 때 하나씩 만든다.

```python
squares_list = [number * number for number in range(10)]
squares_generator = (number * number for number in range(10))
```

`sum()`, `any()`, `all()`처럼 한 번만 순회할 함수에는 제너레이터 표현식을 바로 전달하면 별도 리스트를 만들지 않아도 된다.

```python
total = sum(number * number for number in range(10))
```

### Q. `in`은 언제 빠르고 언제 느릴까?

자료구조에 따라 다르다. 리스트와 튜플, 문자열은 앞에서부터 찾으므로 보통 `O(n)`이다. 집합과 딕셔너리 키는 해시를 사용해 평균 `O(1)`이다. 포함 검사를 반복한다면 어떤 자료구조를 대상으로 하는지 확인해야 한다.

### Q. `dictionary.get(key, 0)`을 호출하면 키가 생길까?

생기지 않는다. 키가 없을 때 0을 반환할 뿐이다.

```python
counts = {}
counts.get("a", 0)

print(counts)  # {}
```

`counts["a"] = counts.get("a", 0) + 1`처럼 결과를 대입하거나, `setdefault()`, `defaultdict`를 사용해야 실제 키가 추가된다.

### Q. `sort()` 결과가 `None`인 이유는 무엇일까?

`sort()`는 기존 리스트를 직접 바꾸는 메서드이기 때문이다. 정렬된 새 리스트가 필요하면 `sorted()`를 사용한다.

```python
numbers.sort()
new_numbers = sorted(numbers)
```

### Q. 문자열을 반복문에서 `+=`로 이어 붙여도 될까?

짧은 입력에서는 동작하지만 문자열은 불변이므로 새 문자열을 반복해서 만들 수 있다. 많은 조각을 합칠 때는 리스트에 `append()`한 뒤 마지막에 `"".join(parts)`를 사용하는 방식이 의도를 분명하게 하고 안정적인 성능을 낸다.

```python
parts = []

for character in characters:
    if condition(character):
        parts.append(character)

result = "".join(parts)
```

### Q. `deque`, 리스트, 힙 중 무엇을 선택해야 할까?

마지막에 넣은 값을 먼저 꺼내면 리스트 스택, 먼저 넣은 값을 먼저 꺼내면 `deque` 큐, 현재 값 중 우선순위가 가장 높은 값을 반복해서 꺼내면 힙을 선택한다. 필요한 삭제 위치가 자료구조 선택의 기준이 된다.

### Q. 반복문에서 리스트를 직접 삭제해도 될까?

순회 중 원소를 삭제하면 뒤 원소의 인덱스가 당겨져 일부 값을 건너뛸 수 있다. 조건에 맞는 새 리스트를 만들거나 역순으로 삭제하는 방식이 안전하다.

```python
numbers = [1, 2, 3, 4]
numbers = [number for number in numbers if number % 2 == 0]
```

### Q. 재귀 풀이와 반복문 풀이 중 어느 것이 더 좋을까?

문제 구조가 트리처럼 재귀적으로 정의되면 재귀가 읽기 쉬울 수 있다. 하지만 Python은 재귀 깊이 제한과 호출 스택 비용이 있으므로 깊이가 큰 그래프나 선형 구조에서는 명시적인 스택을 사용하는 반복문 풀이가 더 안전하다. 정답 논리뿐 아니라 입력 크기와 실행 환경을 함께 봐야 한다.

## 정리하며

Week 1에서는 `split()`과 `join()`으로 문자열을 나누고 합쳤고, 리스트 슬라이싱과 `sum()`을 사용해 구간을 계산했으며, `dict.get()`과 집합으로 중복과 빈도를 다뤘다. `deque`를 사용하면서는 같은 삭제 연산이라도 리스트의 앞에서 지우는 것과 큐의 앞에서 꺼내는 것의 시간 복잡도가 다르다는 점도 확인했다.

정리해보니 Python 함수를 많이 아는 것보다 중요한 것은 세 가지였다. 함수가 새 값을 반환하는지 원본을 수정하는지, 해당 연산의 시간 복잡도가 얼마인지, 그리고 반복문 안에서 총 몇 번 실행되는지를 함께 보는 것이다.

앞으로 새로운 문제를 만났을 때는 먼저 필요한 연산을 적어보면 자료구조를 고르기 쉬워진다. 빠른 포함 검사는 집합이나 딕셔너리, 양 끝 처리는 `deque`, 최솟값 반복 추출은 힙, 정렬된 값의 위치 탐색은 `bisect`처럼 연산과 도구를 연결해두면 구현 단계에서 문법보다 문제의 핵심에 더 집중할 수 있다.
