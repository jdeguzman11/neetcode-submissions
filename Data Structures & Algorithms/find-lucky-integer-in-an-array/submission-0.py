class Solution:
    def findLucky(self, arr: List[int]) -> int:
        counts = {}

        for num in arr:
            counts[num] = counts.get(num, 0) + 1

        lucky = -1

        for num, freq in counts.items():
            if num == freq:
                lucky = max(lucky, num)

        return lucky