class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        
   
        for i, num in enumerate(nums):
            sum = 0

            while num:
                sum += num % 10
                num //= 10

            if sum == i:
                return i

        return -1    

        