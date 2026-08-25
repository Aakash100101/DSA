class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n,m=len(s),len(p)
        if m>n:
            return []
        need=[0]*26
        window=[0]*26

        for ch in p:
            need[ord(ch)-ord('a')]+=1

        result=[]
        for i in range(n):
            window[ord(s[i])-ord('a')]+=1

            left=i-m
            if left>=0:
                 window[ord(s[left]) - ord('a')] -= 1
            if i >= m - 1 and window == need:
                result.append(i-m+1)         

        return result






        