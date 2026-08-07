"""
정수 배열 `nums`와 정수 `k`가 주어집니다.

한 번의 연산에서 배열에서 **합이 `k`가 되는 두 수를 선택해 제거**할 수 있습니다.

배열에 수행할 수 있는 **연산의 최대 횟수**를 반환하세요.

---

### 예시 1

**입력:**

```text
nums = [1,2,3,4], k = 5
```

**출력:**

```text
2
```

**설명:**

처음 배열은 다음과 같습니다.

```text
nums = [1,2,3,4]
```

* `1`과 `4`를 제거하면 `nums = [2,3]`
* `2`와 `3`을 제거하면 `nums = []`

더 이상 합이 `5`가 되는 두 수가 없으므로, 총 연산 횟수는 `2`입니다.

---

### 예시 2

**입력:**

```text
nums = [3,1,3,4,3], k = 6
```

**출력:**

```text
1
```

**설명:**

처음 배열은 다음과 같습니다.

```text
nums = [3,1,3,4,3] -> sort 시 1,3,3,3,4
```

* 첫 번째 `3`과 두 번째 `3`을 제거하면 `nums = [1,4,3]`

더 이상 합이 `6`이 되는 두 수가 없으므로, 총 연산 횟수는 `1`입니다.


# 의사코드
- 일단 예외 처리 해야할게.. nums[i]>= k인 경우. 이경우에는 그냥 건너 뛰어야해.
left = 0 → right = 4, 3, 2, 1
left = 1 → right = 4, 3, 2
left = 2 → right = 4, 3
left = 3 → right = 4

이렇게 할까? 안돼 이건 n-1 + n-2 ....결국 등차수열 합 O(N^2)이 나온다.

Try 2
1,3,3,3,4 -> 아까처럼 left right 나눠서 좌우측에서 이동시켜봐?

3,3,4,4 k =6 -> 이때 실행횟수 한번. 근데 좌우측에서 동시에 좁혀가는건 안돼. 특수 조건이 있어야함. 

특수조건?
1. k/2보다 작다? 아 그걸 모르겠네. 어쨌든 전체 탐색하는건 걸러야해. 일단 정렬하고, 특수 조건에 따라 포인터가 따로 움직이게 만들어야함.
2. 아..그러니까 현 상황에서 영향을 가장많이 주고 있는 수. 그걸 택해야함.  그게 **투포인터의 핵심**. 
 k < sum(nums[left],nums[right]) -> 너무 과해. right만 이동. 왜? 제일 작은 수랑 제일 큰수 더했는데도 k보다 큰거니까 가장 큰놈을 줄여야지.
 k > ~~ -> 너무 작아. left를 올려. 비슷한 이유.
 

#예외처리
1. if nums[i]>= k인 경우


"""
nums = [1,2,3,4]
k = 5

class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        pair_num = 0 # 두개 더해서 값이 k가 나오는 쌍의 개수

        nums.sort() # 그냥 sort(nums) 아니다. 주의.

        while left < right:
            if k < nums[left] + nums[right]: # 너무 과해. right를 옮겨
                right -= 1
            elif k > nums[left] + nums[right]:
                left += 1
            elif k == nums[left] + nums[right]:
                pair_num += 1
                right -= 1
                left += 1

        return pair_num

print(Solution().maxOperations(nums,k))