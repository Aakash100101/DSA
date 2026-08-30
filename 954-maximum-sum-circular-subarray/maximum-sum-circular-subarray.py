class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total=0
        maxsum,curr_max=nums[0],0
        minsum,curr_min=nums[0],0
        for num  in nums:
            curr_max=max(curr_max+num,num)
            maxsum=max(maxsum,curr_max)

            curr_min=min(curr_min+num,num)
            minsum=min(minsum,curr_min)
            total+=num

        if maxsum<0:
            return maxsum 

        return max(maxsum,total-minsum)       
        