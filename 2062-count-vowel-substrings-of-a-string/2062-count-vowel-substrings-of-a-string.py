class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        v = 'aeiou'
        s1 = []
        s = ''
        for i in word:
            if i in v:
                s += i
            else:
                s += " "
        for seq in s.split():
            if len(seq) >= 5:
                s1.append(seq)
        l = []
        for seq in s1: 
            for i in range(0, len(seq)):
                for j in range(i + 5, len(seq) + 1):
                    substring = seq[i:j]
                    if sorted(set(substring)) == sorted(v):
                        l.append(substring)
        return len(l)