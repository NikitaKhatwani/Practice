class Solution:
    def romanToInt(self, s: str) -> int:
        d = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        res = 0
        p = "I"
        for c in s[::-1]:
            if d[c]<d[p]:
                res = res - d[c]
            else:
                res = d[c] + res
            p = c
        return res