"""
649. Dota2 Senate

Radiant와 Dire 의원의 현재 인덱스를 각각 큐에 저장한다.
더 앞선 인덱스의 의원이 상대 의원을 제거하고, 다음 라운드 인덱스로 이동한다.
"""

from collections import deque


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        radiant = deque()
        dire = deque()
        senate_count = len(senate)

        for index, party in enumerate(senate):
            if party == 'R':
                radiant.append(index)
            else:
                dire.append(index)

        while radiant and dire:
            radiant_index = radiant.popleft()
            dire_index = dire.popleft()

            if radiant_index < dire_index:
                radiant.append(radiant_index + senate_count)
            else:
                dire.append(dire_index + senate_count)

        return 'Radiant' if radiant else 'Dire'


print(Solution().predictPartyVictory("RRDDD"))
