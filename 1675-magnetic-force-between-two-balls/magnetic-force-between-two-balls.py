class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        def possibletoplace(mid,position,m):
            prev=position[0]
            countballs=1
            for i in range(1,n):
                curr=position[i]
                if curr-prev>=mid:
                    countballs+=1
                    prev=curr
                if countballs==m:
                    break    
                
            return countballs==m           

        n=len(position)
        position.sort()

        minforce=1
        maxforce=position[n-1]-position[0]
        result=0
        while minforce<=maxforce:
            mid=minforce+(maxforce-minforce)//2

            if possibletoplace(mid,position,m):
                result=mid
                minforce=mid+1
            else:
                maxforce=mid-1
        return result            


        

        