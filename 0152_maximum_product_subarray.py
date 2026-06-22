class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result=max(nums)
        maxi,mini=1,1
        for i in nums:
            if i==0:
                maxi,mini=1,1
                continue
            t=maxi*i  # iam assining coz maxi change next
            maxi=max(i*maxi,i*mini,i)
            mini=min(t,i*mini,i)
            result=max(result,maxi)
        return result