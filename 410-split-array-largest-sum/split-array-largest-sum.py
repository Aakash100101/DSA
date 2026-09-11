class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l=max(nums)
        h=sum(nums)
        ans=0
        while l<=h:
            mid=l+(h-l)//2
            if self.cansplit(nums,mid,k):
                ans=mid
                h=mid-1
            else:
                l=mid+1
        return ans
    def cansplit(self,nums,mid,k):
        count=1
        currsum=0
        for num in nums:
            if currsum+num<=mid:
                currsum+=num
            else:
                count+=1
                currsum=num
        return count<=k                          

        