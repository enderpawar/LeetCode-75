"""
LeetCode 1431번 **"가장 많은 사탕을 가진 아이들 (Kids With the Greatest Number of Candies)"** 문제의 한국어 번역입니다.

---

## 문제 설명

$n$명의 아이들이 사탕을 가지고 있습니다. 각 아이가 가진 사탕의 개수를 나타내는 정수 배열 `candies`와 추가로 가지고 있는 사탕의 개수를 나타내는 정수 `extraCandies`가 주어집니다.

길이가 $n$인 불리언(Boolean) 배열 `result`를 반환하세요. $i$번째 아이에게 `extraCandies`를 모두 주었을 때, 그 아이가 모든 아이들 중 **가장 많은 사탕**을 가지게 된다면 `result[i]`는 `true`, 그렇지 않다면 `false`가 됩니다.

*참고: 가장 많은 사탕을 가진 아이는 여러 명일 수 있습니다.*

---

## 예시

### 예시 1

* **입력:** `candies = [2, 3, 5, 1, 3]`, `extraCandies = 3`
* **출력:** `[true, true, true, false, true]`
* **설명:**
* **1번째 아이:** $2 + 3 = 5$개 (최대 개수인 5 이상이므로 `true`)
* **2번째 아이:** $3 + 3 = 6$개 (최대 개수인 5 이상이므로 `true`)
* **3번째 아이:** $5 + 3 = 8$개 (최대 개수인 5 이상이므로 `true`)
* **4번째 아이:** $1 + 3 = 4$개 (최대 개수인 5보다 작으므로 `false`)
* **5번째 아이:** $3 + 3 = 6$개 (최대 개수인 5 이상이므로 `true`)



### 예시 2

* **입력:** `candies = [4, 2, 1, 1, 2]`, `extraCandies = 1`
* **출력:** `[true, false, false, false, false]`
* **설명:** 추가 사탕이 1개뿐이므로, 기존에 가장 많이 가지고 있던 1번째 아이만 최댓값을 유지할 수 있습니다.

### 예시 3

* **입력:** `candies = [12, 1, 12]`, `extraCandies = 10`
* **출력:** `[true, false, true]`

result = 그 아이가 모든 아이들 중 **가장 많은 사탕**을 가지게 된다면 `result[i]`는 `true`, 그렇지 않다면 `false`가 됩니다.

----------
pseudo code
1. 걍 1~ n까지 순회하면서 대소비교 후, max 값에 가장 큰 친구 넣음. if (max < candies[i])
2. result = [0 for in range] (0으로 candies 개수만큼 채워넣기 해서 boolean 값으로 저장하게 함. )
3. 그렇게 max 값 구한 후 , 다시 candies[i] + extraCandies 해서 max와 대소비교 , result 값에 true false 넣기.

"""
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:

            max_num = 0
            result = [True] * len(candies) # 맞다 이렇게 썼었지.. result를 len(candies) 만큼의 크기로 초기화 해주자.

            for i in range(len(candies)):
                  if(max_num < candies[i]):
                        max_num = candies[i]

            #max 값 다 정했으면

            for i in range(len(candies)):
                result[i] = True if candies[i] + extraCandies >= max_num else False

            return result

            

