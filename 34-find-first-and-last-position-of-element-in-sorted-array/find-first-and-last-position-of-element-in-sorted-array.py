class Solution:

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lb = self.lowerbound(nums, target)

        if lb == -1  or nums[lb]!=target:
            return [-1, -1]

        ub = self.upperbound(nums, target)

        return [lb, ub - 1]

    def lowerbound(self, nums, target):
        n = len(nums)
        lb = -1
        left = 0
        right = n - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] >= target:
                lb = mid
                right = mid - 1
            else:
                left = mid + 1

        return lb

    def upperbound(self, nums, target):
        n = len(nums)
        ub =n
        left = 0
        right = n - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] > target:
                ub = mid
                right = mid - 1
            else:
                left = mid + 1

        return ub