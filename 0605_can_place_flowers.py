class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n==0:
            return True
        m=len(flowerbed)
        for i in range(m):
            left=(i==0)or (flowerbed[i-1]==0)
            right=(i==m-1)or(flowerbed[i+1]==0)
            if left and right and flowerbed[i]==0:
                flowerbed[i]=1
                n-=1
                if n==0:
                    return True
        return False