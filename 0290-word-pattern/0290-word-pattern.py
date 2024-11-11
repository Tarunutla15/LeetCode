class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False
        
        pat_to_word = {}
        word_to_pat = {}
        
        for pat, word in zip(pattern, words):
            if pat not in pat_to_word:
                pat_to_word[pat] = word
            elif pat_to_word[pat] != word:
                return False
            
            if word not in word_to_pat:
                word_to_pat[word] = pat
            elif word_to_pat[word] != pat:
                return False
        
        return True
