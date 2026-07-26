"""

### 문제 설명

정수 배열 `nums`가 주어졌을 때, 이 배열의 피벗 인덱스(pivot index)를 계산하세요.

피벗 인덱스란 **해당 인덱스의 엄격히 왼쪽에 있는 모든 숫자의 합이 엄격히 오른쪽에 있는 모든 숫자의 합과 같아지는 인덱스**를 의미합니다.

인덱스가 배열의 맨 왼쪽 끝에 있는 경우, 왼쪽에 요소가 없으므로 **왼쪽 합은 0**입니다. 이는 배열의 맨 오른쪽 끝에 있는 경우(오른쪽 합이 0)에도 동일하게 적용됩니다.

**가장 왼쪽에 위치한 피벗 인덱스**를 반환하세요. 만약 그러한 인덱스가 존재하지 않는다면 **-1**을 반환하세요.

한마디로 인덱스 슬라이싱해서
[0:n], [n+1:end] 더한게 같냐를 비교하면 되겠네.

"""
from typing import List

nums = [0,0]

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        output = -1

        for i in range(len(nums)):
            left_sum = sum(nums[0:i]) 
            print(left_sum)
            right_sum = sum(nums[i+1:])
            print(right_sum)
            if(left_sum == right_sum):
                output = i
                break;

        return output

print(Solution().pivotIndex(nums))

