"""
문제 지문(Description)과 제한사항(Constraints)의 한국어 번역입니다.

---

## 문제 설명

정수 배열 `nums`가 주어졌을 때, 0이 아닌 요소들의 상대적인 순서를 유지하면서 
모든 0을 배열의 끝으로 이동시키세요.

**주의:** 배열의 사본을 만들지 않고 in-place(제자리)에서 직접 수정해야 합니다.

---

## 예시

* **예시 1**
* **입력:** `nums = [0,1,0,3,12]`
* **출력:** `[1,3,12,0,0]`


* **예시 2**
* **입력:** `nums = [0]`
* **출력:** `[0]`

## 의사코드

- 모든 0을 배열의 끝으로 이동? push and pop을 포인터로 구현해야되는 것 같음.
- if nums[i] == 0 이면 tmp = nums[i] 저장하고, i+1 ~ n-1까지를 앞으로 당겨오기. -> O(n) 소모.
- 그럼 시간복잡도가 O(n^2)이 되는데 괜찮으려나. 안 될 것 같은데..
- 0가 있으면 빼고 cnt+=1, 다시 sort 한다음에 cnt 된 0의 개수만큼 뒤에 붙이는 형식으로 해야겠다.
"""
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:

        cnt = 0 

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[cnt] = nums[i]
                if cnt != i: 
                    nums[i] = 0
                cnt += 1   

                
        """
        Do not return anything, modify nums in-place instead.
        """

        