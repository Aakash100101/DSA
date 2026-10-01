class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        stack=[]
        result={}
        for num in nums2:
            while stack and num>stack[-1]:
                result[stack[-1]]=num
                stack.pop()
            stack.append(num)    
        while stack:
            result[stack[-1]]=-1
            stack.pop()
        ans=[]
        for num in nums1:
            ans.append(result[num])
        return ans          
                
                

        