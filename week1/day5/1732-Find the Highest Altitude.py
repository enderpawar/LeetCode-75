"""
한 라이더가 도로 여행을 떠납니다. 
이 도로 여행은 서로 다른 고도를 가진 $n + 1$개의 지점으로 구성되어 있습니다.
라이더는 고도가 0인 0번 지점에서 출발합니다.
길이가 $n$인 정수 배열 gain이 주어집니다. 
여기서 gain[i]는 지점 $i$와 $i + 1$ 사이의 net gain(고도 변화량)을 나타냅니다 
방문한 지점들 중 가장 높은 고도를 반환하세요.
"""
class Solution:

    def largestAltitude(self, gain: list[int]) -> int:
        current_altitude = 0
        max_altitude = 0  

        for g in gain:
            current_altitude += g
            if current_altitude > max_altitude:
                max_altitude = current_altitude

        return max_altitude

# 이건 너무 쉽다. velog 작성 x
