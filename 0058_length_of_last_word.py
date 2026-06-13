class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n=len(s)-1
        result=0
        for i in range(n,-1,-1):
            if s[i]!=" ":
                result+=1
            elif s[i]==" " and result>0:
                return result
        return result
        
