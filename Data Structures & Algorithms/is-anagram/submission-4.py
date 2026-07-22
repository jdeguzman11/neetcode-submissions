class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts = {}
        
        if len(s) != len(t):
            return False

        for ch in s:
            counts[ch] = counts.get(ch, 0) + 1
        for ch in t:
            counts[ch] = counts.get(ch, 0) - 1
            if counts[ch] < 0:
                return False

        return True