"""
문제

인코딩된 문자열 s가 주어졌을 때, 이를 디코딩한 문자열을 반환하라.

인코딩 규칙은 다음과 같다.

k[encoded_string]

대괄호 [] 안에 있는 encoded_string을 정확히 k번 반복한다.

여기서 k는 항상 양의 정수이다.

입력 문자열은 항상 올바른 형식이라고 가정할 수 있다.

불필요한 공백은 없다.
대괄호 []는 항상 올바르게 짝지어져 있다.
원래 문자열에는 숫자가 포함되지 않는다.
숫자는 오직 **반복 횟수 k**를 나타내기 위해서만 등장한다.

따라서 다음과 같은 입력은 주어지지 않는다.

3a
2[4]

또한 테스트 케이스는 디코딩된 결과 문자열의 길이가 10^5를 넘지 않도록 만들어져 있다.

예제 1
Input: s = "3[a]2[bc]"
Output: "aaabcbc"

설명:

3[a]  → "aaa"
2[bc] → "bcbc"

예제 2
Input: s = "3[a2[c]]"
Output: "accaccacc"

여기는 중첩된 인코딩이 있다는 게 핵심이야.

먼저 안쪽부터 보면:

2[c] → "cc"

그러면:

a2[c] → "acc"

그리고 이것을 3번 반복해서:

3[acc] → "accaccacc"

# 의사코드 
- 커스텀 함수 하나 짜서, [] 한쌍이 나올때마다 호출해야할것 같아. 
- 아님 어떡하지 음 아 자료구조에서 본 중후선위 연산자 구조처럼 [] 를 트리거로 삼아서 해볼까 

# 그럼 현재 구조가 3은 for문을 돌릴 횟수고 []는 반복할 문자열임. 그럼 LIFO니까 
# 맨앞에 있는 if c is '[' 라면 for 문 시작하고 ']' 만날때까지의 문자열을 재귀로 보내주면될 것 같은데? 아니라면 그냥 print(s) 하고.

---> 이 재귀 버전은 improvement 버전으로 다시 구현해보자. 지금은 스택 연습을 해봐야하니까.



"""

# class Solution:
#     def decodeString(self, s):
#         stack = []

#         for c in s:
#             stack.append(c) # 이렇게 하면 문자 하나씩 들어간다 ex) '3', '[', 'a', '2', '[', 'c', ']', ']'

#         rcd_num = 0 # 반복할 문자열을 기록 중인지를 나타내는 상태를 기록
#         rpt_state = False 
#         tmp_stack = []

#         for i in range(len(stack)):
#             c = stack.pop()
            

#             if rpt_state == True:
#                 for i in range(int(c)): # 반복 횟수가 나오니까 int(c)로 감싸서 그만큼 반복하게 해줌
#                     print(tmp_stack.pop())
#                 rpt_state = False
#                 continue

#             if c == ']': # rcd_state 를 만들어서 rcd_state이면 임시 s에 현재 값들을 append 하게끔 할까?  그리고 '['를 만나면 다시 켜보는거지.
#                 rcd_num += 1
#                 continue # ] 두번 만나면 ]까지 기록하는걸 방지하기 위해 continue

#             if c == '[': # rcd_state 를 만들어서 rcd_state이면 임시 s에 현재 값들을 append 하게끔 할까?  그리고 '['를 만나면 다시 켜보는거지.
#                 rcd_num -= 1
#                 rpt_state = True
#                 continue # ] 두번 만나면 ]까지 기록하는걸 방지하기 위해 continue
            
#             if rcd_num != 0 and c != ']': 
#                 tmp_stack.append(c)    
            
#         # 스택은 LIFO 구조이므로 POP은 우->좌로 간다.
#         # for 
#         # if c is ']' 이면 
# s = "3[a2[c]]"
# Solution().decodeString(s)

class Solution:
    def decodeString(self, s):
        stack = []

        for c in s:
            if c != ']':
                stack.append(c)
            else:
                # 1. '[' 전까지 문자열 꺼내기
                tmp = ""

                while stack[-1] != '[':
                    tmp = stack.pop() + tmp

                # 2. '[' 제거
                stack.pop()

                # 3. 반복 횟수 꺼내기
                num = ""

                while stack and stack[-1].isdigit():
                    num = stack.pop() + num

                # 4. 문자열 반복
                decoded = tmp * int(num)

                # 5. 다시 stack에 넣기
                stack.append(decoded)

        return "".join(stack)


s = "3[a2[c]]"
print(Solution().decodeString(s))