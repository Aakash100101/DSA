class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_sum=0
        count=0
        prefix_map={0:1}
        for num in nums:
            prefix_sum+=num
            reminder=prefix_sum%k

            if reminder in prefix_map:
                count+=prefix_map[reminder]

            prefix_map[reminder]=prefix_map.get(reminder,0)+1

        return count    