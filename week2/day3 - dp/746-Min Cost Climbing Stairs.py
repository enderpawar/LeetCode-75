"""
746. 계단 오르기 최소 비용 (Min Cost Climbing Stairs)
정수 배열 cost가 주어집니다. 여기서 cost[i]는 계단의 $i$번째 계단을 밟을 때 지불해야 하는 비용입니다. 
비용을 지불하고 나면 1칸 또는 2칸을 오를 수 있습니다.
계단 오르기는 인덱스 0번째 계단 또는 인덱스 1번째 계단 중 어디서든 시작할 수 있습니다.
계단의 꼭대기(Top, 마지막 계단 너머)에 도달하기 위한 최소 비용을 반환하세요.

점화식 = prev1 ,prev2로 min 비교해서 하면 될거 ㅅ 같은데?
"""

class Solution(object):

    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        # prev1: 1단계 전 계단까지의 최소 비용
        # prev2: 2단계 전 계단까지의 최소 비용
        prev2, prev1 = 0, 0

        for c in cost:
            # 현재 계단을 밟고 다음으로 넘어가는 최소 비용 계산
            curr = c + min(prev1, prev2)
            prev2 = prev1
            prev1 = curr

        # 꼭대기는 마지막 계단(prev1) 또는 그 전 계단(prev2)에서 바로 도착할 수 있음
        return min(prev1, prev2)