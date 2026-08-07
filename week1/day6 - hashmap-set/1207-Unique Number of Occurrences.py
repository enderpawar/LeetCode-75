"""
# 문제 
정수 배열 arr가 주어질 때, 배열에 존재하는 각 값의 등장 횟수(빈도수)가 
모두 서로 다르면 true, 중복된 횟수가 있으면 false를 반환하세요.

# 예시

1 -> 3번
2 -> 2번
3 -> 1번
-> 등장횟수가 모두 다르면 true.

# 의사코드 
딱히 무슨수가 몇번 나오는걸 구분해야되진 않음. 
걍 인덱스 0...1.. 으로 첫번째 나온수부터 중복횟수 기록하고, 
마지막에 len(set(cnt))와 len(arr)이 다르면 False, 같으면 True 반환. 

#시도1 cnt = [0,]으로 전부 초기화? 
- 근데 cnt 를 그대로 idx로 쓰기엔 희소 배열방식이라 비효율적이야. -1000부터니까 1000+ 보정을 때려서 한다고해도
  나머지 900 +n 개는 버려지는 공간이 됨.
# 시도2 dictionary (key,value)형태로 해보자.
- for num in arr : cnt.get(num,0) +1 . 파이썬에선 get하고 +1 하면 value에 +=1 됨. 놀 랍 다!
"""
from typing import List


arr = [1,2,2,1,1,3]

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:

       # result = True 걍 == 으로 직접 비교하자

        cnt = {} # []이 아니라 dictionary 형태로 선언
        for num in arr:
            cnt[num] = cnt.get(num,0) + 1

        occur = list(cnt.values())
        
        return len(occur) == len(set(occur))


print(Solution().uniqueOccurrences(arr))