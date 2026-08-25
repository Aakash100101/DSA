class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        seen=set()
        for num in nums:
            seen.add(num)

        for i in range(1,len(nums)*100):
            if i*k not in seen:
                return i*k   



         
        