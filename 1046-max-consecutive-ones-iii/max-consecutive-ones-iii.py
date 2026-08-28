class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left=0
        ones_count=0
        max_ones=0
        result=0
        for right in range(len(nums)):
            if nums[right]==1:
                ones_count+=1
            max_ones=max(max_ones,ones_count)    
            
           
            window_len=right-left+1
            if window_len-max_ones>k:
                if nums[left]==1:
                    ones_count-=1
                left+=1
            result=max(result,right-left+1)
        return result    

        