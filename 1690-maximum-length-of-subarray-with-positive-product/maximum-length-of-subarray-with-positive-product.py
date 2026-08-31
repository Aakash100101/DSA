class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        poslen,neglen=0,0
        maxlen=0
        for i in range(len(nums)):
            if nums[i]>0:
                poslen+=1
                neglen+=1 if neglen>0 else 0
                
            elif nums[i]<0:
                poslen,neglen=neglen,poslen

                poslen+=1 if poslen>0 else 0
                neglen+=1
            else:
                poslen=0
                neglen=0    
            maxlen=max(maxlen,poslen)
        return maxlen


        