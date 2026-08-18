# 735. Asteroid Collision - 개선 버전
# 입력 리스트를 스택으로 재사용해서 추가 공간을 O(1)로 줄인 풀이


class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """

        top = 0  # 스택에 살아남은 원소 개수

        for asteroid in asteroids:

            while top > 0 and asteroids[top - 1] > 0 and asteroid < 0:
                if asteroids[top - 1] < -asteroid:
                    top -= 1
                    continue

                elif asteroids[top - 1] == -asteroid:
                    top -= 1

                break

            else:
                asteroids[top] = asteroid
                top += 1

        del asteroids[top:]

        return asteroids


if __name__ == "__main__":
    solution = Solution()

    print(solution.asteroidCollision([5, 10, -5]))      # [5, 10]
    print(solution.asteroidCollision([8, -8]))          # []
    print(solution.asteroidCollision([10, 2, -5]))      # [10]
    print(solution.asteroidCollision([-2, -1, 1, 2]))   # [-2, -1, 1, 2]
    print(solution.asteroidCollision([1, -1, -2, -2]))  # [-2, -2]
    print(solution.asteroidCollision([-2, 2, 1, -2]))   # [-2]
