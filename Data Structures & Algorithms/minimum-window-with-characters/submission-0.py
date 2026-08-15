class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = ""
        countT = {}
        countS = {}
        l = 0

        if len(s) < len(t):
            return res

        for ch in t:
            countT[ch] = countT.get(ch, 0) + 1
        
        have = 0
        need = len(countT)
        
        for r in range(len(s)):
            countS[s[r]] = countS.get(s[r], 0) + 1

            if s[r] in countT and countS[s[r]] == countT[s[r]]:
                have += 1
            
            while have == need:
                if not res or (r - l + 1) < len(res):
                    res = s[l: r + 1]
                countS[s[l]] -= 1

                if s[l] in countT and countS[s[l]] < countT[s[l]]:
                    have -= 1

                l += 1
        return res
            