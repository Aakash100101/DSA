class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        last_s = {}
        last_t = {}
        for i in range(len(s)):
            if last_s.get(s[i], -1) != last_t.get(t[i], -1):
                return False
            last_s[s[i]] = i
            last_t[t[i]] = i
        return True
  
                

        