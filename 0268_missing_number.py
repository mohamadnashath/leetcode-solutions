class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        freq={}
        for i in range(0,len(nums)+1):
            freq[i]=0
        for num in nums:
            freq[num]=1
        for k,v in freq.items():
            if v==0:
                return k
        
        