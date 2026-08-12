class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        dic={}
        left,right=0,0
        max_length=0
        while right<len(fruits):
            dic[fruits[right]]=dic.get(fruits[right],0)+1
            if len(dic)>2:
                dic[fruits[left]]-=1
                if dic[fruits[left]]==0:
                    del dic[fruits[left]]
                left+=1
            if len(dic)<=2:
                max_length=max(max_length,right-left+1)
            right+=1
        return max_length