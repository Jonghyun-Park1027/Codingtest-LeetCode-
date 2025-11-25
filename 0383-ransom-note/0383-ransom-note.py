from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        magazine = Counter(magazine)
        for i in ransomNote:
            magazine[i] -= 1
            if magazine[i] < 0 :
                return False
        
        return True