from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        k = r

        while l <= r:
            spd = (l + r) // 2
            time = 0

            for p in piles:
                time += ceil(p / spd)
            
            if time > h:
                l = spd + 1

            else:
                k = min(k, spd)
                r = spd - 1
        
        return k