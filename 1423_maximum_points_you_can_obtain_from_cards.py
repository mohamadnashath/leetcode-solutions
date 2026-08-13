class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n=len(cardPoints)
        if(n==k):
            return sum(cardPoints)
        leftsum,rightsum=0,0
        for i in range(0,k):
            leftsum+=cardPoints[i]
        maxi=leftsum
        right_ind=n-1
        for i in range(k-1,-1,-1):
            leftsum-=cardPoints[i]
            rightsum+=cardPoints[right_ind]
            maxi=max(maxi,leftsum+rightsum)
            right_ind-=1
        return maxi
           

        