class Solution:
    def fib(self, n: int) -> int:
        if n<2:
            return n
        curr,prev=1,0
        for i in range(2,n+1):
            curr,prev=prev+curr,curr
        return curr