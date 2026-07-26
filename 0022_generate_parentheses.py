class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result=[]
        brackets=[""]*(n*2)
        def solve(ind,total,brackets,result):
            if ind>=len(brackets):
                if total==0:
                    result.append("".join(brackets))
                return
            if total>len(brackets)//2:
                return
            elif total<0:
                return
            brackets[ind]="("
            solve(ind+1,total+1,brackets,result)
            brackets[ind]=")"
            solve(ind+1,total-1,brackets,result)
        solve(0,0,brackets,result)
        return result

        