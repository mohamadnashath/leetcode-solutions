class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        m,n=len(g),len(s)
        s.sort()
        g.sort()
        left,right,count=0,0,0
        while left<m and right<n:
            if g[left]<=s[right]:
                count+=1 
                left+=1
            right+=1
        return count
        
        