class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res=""
        count=0
        for br in s:
            if br=="(":
                count+=1
                if count>1:
                    res+=br
            if br==")":
                count-=1
                if count>0:
                    res+=br
        return res       
