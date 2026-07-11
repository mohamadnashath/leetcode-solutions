class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        res=[0]*len(nums)
        posind,negind=0,1
        for i in nums:
            if i>=0:
                res[posind]=i
                posind+=2
            else:
                res[negind]=i
                negind+=2
        return res

        