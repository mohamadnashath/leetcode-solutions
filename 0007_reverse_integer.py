class Solution:
    def reverse(self, x: int) -> int:
        sign=-1 if x<0 else 1
        x=abs(x)
        res=0
        while x:
            digit = int(x%10)
            x=int(x//10)   
            res=(res*10)+digit
        res=res*sign
        return res if -2**31<=res and (2**31)-1>=res else 0