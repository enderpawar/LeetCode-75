"""


---

### 문제 설명

길이가 $n$인 정수 배열 `height`가 주어집니다. $i$번째 선의 양 끝점이 $(i, 0)$과 $(i, \text{height}[i])$가 되도록 
$n$개의 수직선이 그려져 있습니다.

$x$축과 함께 용기를 형성하여 **가장 많은 물을 담을 수 있는 두 선**을 찾으세요.

용기가 담을 수 있는 **물의 최대 양**을 반환해야 합니다.

*(주의: 용기를 기울일 수는 없습니다.)*

---

### 예시

**예시 1:**

* **입력:** `height = [1,8,6,2,5,4,8,3,7]`
* **출력:** `49`
* **설명:** 수직선은 각각 `[1,8,6,2,5,4,8,3,7]` 위치에 있습니다. 인덱스 1(높이 8)과 
인덱스 8(높이 7)을 선택할 때 형성되는 면적이 $7 \times (8 - 1) = 49$로 최대가 됩니다.

**예시 2:**

* **입력:** `height = [1,1]`
* **출력:** `1`


제약조건 X

- 음..max 값 찾아서 계속 대소비교하면서 찾기? 
- 공식 자체는 그렇게 어렵지 않을것 같아. 걍 max로 해놓고 그렇게 할까?
- 근데 전체 대소비교하면 O(N X M) 이 형태가 될텐데 그건 비효율적임.
- 대신 내림차순으로 sort 해서 비교하는게 나을 것 같은데? dictionary로 못바꾸나  
- 일단 어떻게 되든 전체 탐색은 해야해. 근데 시간 제한이 안나와있어서 너무 애매하네. 
- 시간제한은 10^5까지니까 O(N^2)은 안돼. 그러면 전체 비교는 기각.

------
Try 2.  
- 투 포인터니까.. 최 좌 최 우측부터 탐색을 시작해서 점점 줄여가며 포인터가 만날떄까지 반복한다.
- 왜? 애초에 높이는 작은 쪽을 위주로 결정되고, 그럼 높이에 영향을 끼치는 쪽만 움직이면 브루트포스 식으로 전체 비교를하지 않아도 된다.
- 오케이. 정답 나왔다.
"""
height = [1,8,6,2,5,4,8,3,7]

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1

        max_width = -1 # 넓이의 최댓값

        while left < right:
            width = min(height[right], height[left]) * (right - left)

            if max_width < width:
                max_width = width

            if height[left] >= height[right]:
                right -= 1
            else:
                left += 1

        return max_width

print(Solution().maxArea(height))