class Solution(object):
    def myAtoi(self, s):
        s = s.strip()
        if not s: return 0
        sign, i = 1, 0
        if s[0] in ['-', '+']:
            sign = -1 if s[0] == '-' else 1
            i = 1
        ret = 0
        while i < len(s) and s[i].isdigit():
            ret = ret * 10 + int(s[i])
            i += 1
        return max(-2**31, min(sign * ret, 2**31 - 1))
