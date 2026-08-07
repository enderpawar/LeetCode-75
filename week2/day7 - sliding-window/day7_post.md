# [LeetCode 75 Day 14] 1004. Max Consecutive Ones III & 1456. Maximum Number of Vowels in a Substring of Given Length

Day 14에서는 슬라이딩 윈도우로 묶이는 두 문제를 풀었다. 하나는 윈도우 크기가 조건에 따라 늘어나거나 줄어드는 가변 윈도우이고, 다른 하나는 크기가 항상 k로 고정된 윈도우다. 둘 다 매번 윈도우 안을 처음부터 다시 세지 않고, 빠지는 값과 들어오는 값만 반영해서 상태를 갱신하는 방식으로 풀었다.

## 1. Max Consecutive Ones III - 0을 최대 k개 뒤집어서 만들 수 있는 최장 연속 1

이진 배열 `nums`에서 0을 최대 `k`개까지 1로 뒤집을 수 있을 때, 만들 수 있는 가장 긴 연속된 1의 길이를 구하는 문제다.

```python
class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        zero_idx = []

        for i in range(len(nums)):
            if nums[i] == 0:
                zero_idx.append(i)

        if len(zero_idx) <= k:
            return len(nums)

        start_pnt = 0
        end_pnt = k
        max_len = 0

        while end_pnt <= len(zero_idx):
            if start_pnt == 0:
                left_zero = -1
            else:
                left_zero = zero_idx[start_pnt - 1]

            if end_pnt == len(zero_idx):
                right_zero = len(nums)
            else:
                right_zero = zero_idx[end_pnt]

            crt_len = right_zero - left_zero - 1
            max_len = max(max_len, crt_len)

            start_pnt += 1
            end_pnt += 1

        return max_len
```

`nums`를 직접 슬라이딩하는 대신, 0이 있는 인덱스만 `zero_idx`에 모아두고 그 배열 위에서 길이 `k`짜리 구간을 슬라이딩한다. `zero_idx[start_pnt]`부터 `zero_idx[end_pnt - 1]`까지가 이번에 뒤집는 `k`개의 0이고, 그 구간의 바로 바깥에 있는 0인 `left_zero`와 `right_zero`는 뒤집지 않고 그대로 둔다. 이 두 경계 0 사이의 길이에서 경계 자신을 빼면(`right_zero - left_zero - 1`) 그 구간에서 만들 수 있는 연속 1의 길이가 된다.

이 계산이 성립하는 이유는 `zero_idx`의 연속한 두 값 사이에는 항상 1만 있다는 점이다. `zero_idx`는 0의 위치만 순서대로 모은 배열이므로, 그 사이 구간에 또 다른 0이 섞여 있을 수 없다. 처음에는 구간 양 끝에 원래 있던 1까지 따로 더해줘야 하는 것으로 생각했는데, 이 성질을 알고 나니 경계 0의 인덱스 차이만 구하면 그 안의 1은 자동으로 포함된다는 것을 알 수 있었다.

`zero_idx`의 개수가 `k`보다 적거나 같을 때는 배열 전체를 1로 만들 수 있으므로 `len(nums)`를 바로 반환한다. 이 예외 처리가 없으면 `end_pnt`가 `zero_idx`의 길이를 넘어서 `while` 문이 한 번도 실행되지 않고 `max_len`이 0으로 남는다.

`zero_idx`를 만드는 데 `O(n)`, 그 위에서 슬라이딩하는 데 최악의 경우(0이 배열의 대부분을 차지할 때) `O(n)`이 걸리므로 시간 복잡도는 `O(n)`이다. `zero_idx`에 0의 위치를 모두 저장하므로 공간 복잡도도 최악의 경우 `O(n)`이다.

### 더 개선한다면

`zero_idx`라는 별도 배열을 만들지 않고도 같은 결과를 얻을 수 있다. `nums` 위에서 두 포인터로 직접 윈도우를 유지하면서, 윈도우 안의 0 개수가 `k`를 넘으면 왼쪽을 줄이면 된다.

```python
class Solution(object):
    def longestOnes(self, nums, k):
        left = 0
        zeros = 0
        max_len = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1

            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len
```

`right`가 한 칸씩 늘어날 때마다 0 개수가 `k`를 넘지 않는 한 윈도우를 그대로 넓히고, 넘으면 `left`를 옮겨 0 개수를 다시 `k` 이하로 맞춘다. 시간 복잡도는 여전히 `O(n)`이지만, 0의 위치를 따로 저장하는 배열이 없어 추가 공간이 `O(1)`로 줄어든다.

## 2. Maximum Number of Vowels in a Substring of Given Length - 길이 k인 부분 문자열의 최대 모음 개수

문자열 `s`에서 길이가 정확히 `k`인 부분 문자열 중 모음(`a`, `e`, `i`, `o`, `u`) 개수가 가장 많은 경우를 구하는 문제다.

```python
from collections import deque


class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        window = deque(s[0:k])
        vowel_num = 0

        for i in range(k):
            if window[i] in "aeiou":
                vowel_num += 1

        max_vowel = vowel_num
        end_point = k - 1

        while end_point < len(s) - 1:
            if window[0] in "aeiou":
                vowel_num -= 1

            window.popleft()
            window.append(s[end_point + 1])

            if s[end_point + 1] in "aeiou":
                vowel_num += 1

            max_vowel = max(vowel_num, max_vowel)
            end_point += 1

        return max_vowel
```

처음에는 길이 `k`짜리 부분 문자열을 매번 처음부터 끝까지 훑어서 모음 개수를 세는 방식을 생각했지만, `s`의 길이가 최대 `10^5`라 이 방식은 `O(n * k)`, 즉 최악의 경우 `n^2`에 가까워져 시간 초과가 날 수 있다. 그래서 윈도우를 매번 새로 세지 않고, 오른쪽으로 한 칸 이동할 때 빠지는 글자와 들어오는 글자만 확인해서 `vowel_num`을 갱신하는 방식으로 바꿨다.

`window`는 현재 윈도우에 들어있는 글자를 담은 `deque`다. 오른쪽으로 이동할 때 `window[0]`(빠질 글자)이 모음이면 개수를 하나 빼고, 새로 들어오는 `s[end_point + 1]`이 모음이면 개수를 하나 더한다. `popleft()`와 `append()`는 각각 `O(1)`이라 윈도우를 이동하는 비용이 일정하다.

시간 복잡도는 `s`를 한 번만 훑으므로 `O(n)`이다. 공간 복잡도는 길이 `k`짜리 윈도우를 `deque`에 그대로 들고 있으므로 `O(k)`다.

### 더 개선한다면

이 문제에서 실제로 필요한 것은 윈도우 안의 모음 개수뿐이고, 어떤 글자들이 들어있는지는 `s`를 인덱스로 바로 확인할 수 있다. 그러므로 윈도우의 글자를 `deque`에 복사해서 들고 있을 필요가 없다.

```python
class Solution(object):
    def maxVowels(self, s, k):
        vowels = set("aeiou")

        vowel_num = sum(1 for ch in s[:k] if ch in vowels)
        max_vowel = vowel_num

        for right in range(k, len(s)):
            if s[right] in vowels:
                vowel_num += 1
            if s[right - k] in vowels:
                vowel_num -= 1

            max_vowel = max(max_vowel, vowel_num)

        return max_vowel
```

윈도우의 오른쪽 끝 인덱스 `right`만 옮기면 왼쪽 끝은 항상 `right - k`이므로, `s[right]`와 `s[right - k]`를 직접 확인하는 것만으로 충분하다. 시간 복잡도는 `O(n)`으로 같지만, 윈도우를 별도로 복사해두지 않으므로 추가 공간이 `O(k)`에서 `O(1)`로 줄어든다.

## 3. 스스로 묻고 답한 질문들

### Q. `zero_idx`의 연속한 두 값 사이에는 왜 항상 1만 있다고 확신할 수 있을까?

`zero_idx`는 `nums`를 처음부터 끝까지 훑으면서 값이 0인 인덱스만 순서대로 모은 배열이다. 만약 `zero_idx`의 연속한 두 값 사이에 또 다른 0이 있었다면, 그 위치도 `zero_idx`에 포함되어 있어야 한다. 따라서 `zero_idx`에 담긴 값들 사이 구간에는 정의상 0이 존재할 수 없고, 남은 값은 모두 1이다.

### Q. `zero_idx`의 길이가 `k` 이하일 때 왜 별도로 예외 처리가 필요할까?

메인 반복문은 `end_pnt`가 `k`에서 시작해서 `zero_idx`의 길이를 넘지 않는 동안만 실행된다. `zero_idx`의 길이가 `k`보다 작으면 시작부터 `end_pnt`가 `zero_idx`의 길이를 넘어서므로 반복문이 한 번도 돌지 않고 `max_len`이 초깃값 0으로 반환된다. 하지만 이 경우는 0이 `k`개 이하라는 뜻이므로 전부 뒤집어서 배열 전체를 1로 만들 수 있다. 그래서 반복문에 들어가기 전에 `len(nums)`를 바로 반환하는 처리가 필요하다.

### Q. `deque`에서 `window[i]`처럼 인덱스로 접근하는 것도 빨랐던 걸까?

`deque`는 양쪽 끝에서의 추가·제거(`append`, `appendleft`, `pop`, `popleft`)는 `O(1)`이지만, 중간 인덱스로 접근하는 것은 내부적으로 이중 연결 리스트 구조라 최악의 경우 `O(n)`이 걸린다. 이번 코드에서는 초기 윈도우를 세팅할 때만 `range(k)`만큼 인덱스로 접근했으므로 그 부분의 비용은 `O(k)`이고, 이후 반복문에서는 `window[0]`만 확인하므로 매번 맨 앞 원소를 보는 `O(1)` 접근이다. 만약 반복문 안에서 중간 인덱스에 계속 접근했다면 전체 시간 복잡도가 나빠졌을 것이다.

## 정리하며

Day 14에서는 슬라이딩 윈도우를 유지하는 두 가지 방식을 다뤘다. Max Consecutive Ones III는 조건(0의 개수 ≤ k)에 따라 윈도우 크기가 늘어나거나 줄어드는 가변 윈도우였고, Maximum Number of Vowels in a Substring of Given Length는 크기가 항상 `k`로 고정된 윈도우였다. 두 문제 모두 매번 윈도우 안을 처음부터 다시 세지 않고, 빠지는 값과 들어오는 값만 반영해서 상태를 갱신하는 것이 핵심이었다.

또한 두 풀이 모두 처음에는 값을 담는 별도의 자료구조(`zero_idx` 배열, `deque` 윈도우)를 만들었지만, 원본 배열이나 문자열을 인덱스로 직접 참조하는 것만으로도 같은 정보를 얻을 수 있다는 점을 개선하면서 확인했다. 다음에는 윈도우 크기가 고정되어 있을 때 자료구조를 새로 복사하지 않고 인덱스만으로 처리하는 방식을 먼저 시도해볼 생각이다.
