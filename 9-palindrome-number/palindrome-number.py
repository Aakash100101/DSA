class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return  False
        original=x
        t=0    
        while x>0:
            r=x%10
            t=(t*10)+r
            x//=10
        return  original==t    






        