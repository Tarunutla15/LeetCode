class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortWord = min(strs,key=len)
        for i in range(len(shortWord)):
            for word in strs:
                if word[i]!=shortWord[i]:
                    return shortWord[:i]
        return shortWord
        
        