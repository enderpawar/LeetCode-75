"""
LeetCode 605번 **"꽃 심기 (Can Place Flowers)"** 문제 번역입니다.

---

## 문제 설명

일부 구역에는 꽃이 심어져 있고 일부 구역은 비어 있는 긴 화단이 있습니다. 하지만 꽃은 인접한 구역에 연속해서 

심을 수 없습니다.
`0`은 비어 있는 구역, `1`은 꽃이 심어진 구역을 나타내는 정수 배열 `flowerbed`와 정수 `n`이 주어집니다. 

인접한 곳에 꽃을 심지 않는 규칙을 위반하지 않으면서 `n`개의 새로운 꽃을 심을 수 있다면 `true`, 
그렇지 않다면 `false`를 반환하세요.

---

## 예시

### 예시 1

* **입력:** `flowerbed = [1,0,0,0,1]`, `n = 1`
* **출력:** `true`
* **설명:** 가운데 인덱스 `2` 위치(0번째 기준)에 꽃을 1개 심을 수 있습니다.

### 예시 2

* **입력:** `flowerbed = [1,0,0,0,1]`, `n = 2`
* **출력:** `false`
* **설명:** 인접 규칙을 지키면서는 꽃을 최대 1개까지만 심을 수 있으므로 2개를 심는 것은 불가능합니다.

---

## 제약 조건

* $1 \le \text{flowerbed.length} \le 2 \times 10^4$
* `flowerbed[i]`는 `0` 또는 `1`입니다.
* 입력으로 주어지는 `flowerbed`에는 이미 인접해서 심어진 꽃이 없습니다.

---
pseudo code
# 1차원 지뢰찾기 문제네. 간단함.
1. 인덱스 1부터 n-1까지 순회
2. greedy 식으로, n일때 n-1, n+1 인덱스가 0라면 거기에 1을 박아놓고, cnt += 1
3. 그렇게 순회하고 나서 true if cnt == n else false 하면 될듯? 
"""
class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:

        planted = 0
        flowerbed = [0] + flowerbed + [0]

        for i in range(1, len(flowerbed) - 1):
            if flowerbed[i] == 1:
                continue
            if(flowerbed[i-1] == 0 and flowerbed[i+1] == 0): ## 아 &&이 아니라 and 다..
                flowerbed[i] = 1
                planted += 1
        result = True if planted >= n else False

        return result

            
if __name__ == "__main__":
    sol = Solution()

    # 테스트 케이스 입력
    print(sol.canPlaceFlowers([1, 0, 0, 0, 1], 1))  # Expected: True
    print(sol.canPlaceFlowers([1, 0, 0, 0, 1], 2))  # Expected: False
    print(sol.canPlaceFlowers([0, 0, 1, 0, 0], 1))  # Expected: True
