class Solution:
    def romanToInt(self, s: str) -> int:
        values = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
        }
        result=0
        r=len(s)
        for i in range (r-1):
            if values[s[i]]<values[s[i+1]]:
                result=result-values[s[i]]
            else:
                result=result+values[s[i]]
        result=result+values[s[-1]]
        return result