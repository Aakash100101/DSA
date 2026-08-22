class Solution:
    def checkDivisibility(self, n: int) -> bool:
        digit_sum=0
        product=1
        temp=n
        while n>0:
            digit=n%10
            digit_sum+=digit
            product*=digit
            n//=10

        

        return temp % (digit_sum+product)==0
            
               
        