# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):
"""


### 문제: 숫자 맞추기 게임 (Guess Number Higher or Lower)

숫자 맞추기 게임을 진행합니다. 게임 규칙은 다음과 같습니다.

내가 $1$부터 $n$까지의 숫자 중 하나를 선택합니다. 당신은 내가 선택한 숫자가 무엇인지 맞춰야 합니다 (내가 선택한 숫자는 게임이 진행되는 동안 바뀌지 않습니다).

당신이 틀린 숫자를 제시할 때마다, 내가 선택한 숫자가 당신이 추측한 숫자보다 높은지(higher) 낮은지(lower) 알려줍니다.

당신은 이미 정의된 API인 `int guess(int num)`을 호출할 수 있으며, 이 함수는 다음 3가지 결과를 반환합니다.

* **-1**: 당신이 추측한 숫자가 내가 선택한 숫자보다 큽니다 (`num > pick`).
* **1**: 당신이 추측한 숫자가 내가 선택한 숫자보다 작습니다 (`num < pick`).
* **0**: 당신이 추측한 숫자가 내가 선택한 숫자와 같습니다 (`num == pick`).

내가 선택한 숫자를 반환하는 프로그램을 작성하세요.

# 의사코드
- Binary search로 하면 될 것 같은데?
- 1~n 중 일단 2/n으로 한다음에, 1이 나오면 Array slice로 1~ n/2 - 1로 하고, -1일 시 n/2 +1 ~ n으로. 
- 이거 반복하다가 n == pick일 시 return.
"""
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

# 입력 : n = 10 / pick = 6 이런식으로.

    
class Solution(object):
    def guessNumber(self, n):

        left = 1
        right = n

        while left <= right:            

            answer = (left+right) // 2

            if guess(answer) == 1:
                left = answer + 1
            if guess(answer) == -1:
                right = answer - 1
            if guess(answer) == 0:
                return answer
            