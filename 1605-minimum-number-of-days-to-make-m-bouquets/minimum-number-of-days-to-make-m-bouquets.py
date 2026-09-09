class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n=len(bloomDay)
        if m*k>n:
            return -1
        def canMakeMbou(bloomDay,k,mid):
            bouqcount=0
            count=0
            for i in range(n):
                if bloomDay[i]<=mid:
                    count+=1
                else:
                    count=0
                
                if count==k:
                    bouqcount+=1
                    count=0    
            return bouqcount          

            
        l=0
        r=max(bloomDay)
        ans=-1
        while l<=r:
            mid=l+(r-l)//2
            if canMakeMbou(bloomDay,k,mid)>=m:
                ans=mid
                r=mid-1
            else:
                l=mid+1
        return ans             
                


        