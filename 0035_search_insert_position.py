class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        f = 0
        b = len(nums)-1
        while f <= b:
            m = (f+b)//2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                f = m+1
            else:
                b = m-1
        return f
