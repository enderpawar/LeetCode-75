"""
문제 설명

최근 특정 시간 동안 발생한 요청(Request)의 수를 세는 RecentCounter 클래스를 구현하는 문제입니다.

RecentCounter 클래스 사양:

RecentCounter() : 최근 요청 수를 0으로 초기화합니다.

int ping(int t) : 밀리초 단위 시간 t에 새로운 요청을 추가하고, 
최근 3000밀리초 내에 발생한 요청의 개수를 반환합니다. 
정확히는 [t - 3000, t] 범위(양 끝값 포함) 내에 발생한 요청 수입니다.

참고: ping 함수가 호출될 때 전달되는 t값은 항상 이전 호출의 t값보다 엄격하게 큽니다(엄격한 오름차순).

예시 분석
입력:
["RecentCounter", "ping", "ping", "ping", "ping"]
[[], [1], [100], [3001], [3002]]
출력:
[null, 1, 2, 3, 3]

"""
from collections import deque

class RecentCounter:

    def __init__(self):
        self.queue = deque() # t를 담아두기 위해서 다음과 같이 함수 queue 생성.

    def ping(self, t: int) -> int:

        self.queue.append(t)

        while self.queue and self.queue[0] < t - 3000:
            self.queue.popleft()

        return len(self.queue)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
# !! velog 글 작성시 python deque, stack 관련 함수 사용법 전부 적을 것.
