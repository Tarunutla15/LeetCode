class Solution:
    def getLucky(self, s: str, k: int) -> int:
        num = int("".join([str(ord(x)-96) for x in s]))
        
        for _ in range(k):
            val = 0
            while num!=0:
                a = num%10
                val +=a
                num//=10
            num=val
        return num
            
        