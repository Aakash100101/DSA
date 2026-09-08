import math
class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        n = len(dist)
        if hour <= n - 1:
            return -1

        def time_needed(speed: int) -> float:
            total = 0
            for i in range(n - 1):
                total += math.ceil(dist[i] / speed)
            total += dist[-1] / speed
            return total

        lo, hi = 1, 10**7
        ans = -1
        while lo <= hi:
            mid = (lo + hi) // 2
            if time_needed(mid) <= hour:
                ans = mid
                hi = mid - 1
            else:
                lo = mid + 1
        return ans        