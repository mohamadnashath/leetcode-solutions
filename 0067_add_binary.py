class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a,b=a[::-1],b[::-1]
        res=""
        carry=0
        for i in range(max(len(a),len(b))):
            if i<len(a):
                digita=int(a[i])
            else:
                digita=0

            if i<len(b):
                digitb=int(b[i])
            else:
                digitb=0

            total=digita+digitb+carry
            char=str(total%2)
            res=res+char
            carry=total//2

        if carry!=0:
            res+="1"
    
        return res[::-1]