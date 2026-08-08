class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        seen=set()
        n=len(nums)
        expected_sum=n*(n+1)//2
        actual_sum=sum(nums)
        for num in nums:
            if num in seen:
                duplicate=num
            seen.add(num)
        missing_number=expected_sum - actual_sum + duplicate  

        return [duplicate,missing_number]      
            



            
            

           


        