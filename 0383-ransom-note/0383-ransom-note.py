class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        note = [i for i in ransomNote]
        for i in magazine:
            if i in note:
                note[note.index(i)]=True
        for i in range(len(note)):
            if note[i] is not True:
                note[i]=False
        print(note)
        if all(note):
            return True
        else:
            return False