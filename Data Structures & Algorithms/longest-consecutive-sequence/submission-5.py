class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        sequence = set(nums)

        for num in sequence:
            if num - 1 not in sequence:
                curr = num
                length = 1

                while curr + 1 in sequence:
                    length += 1
                    curr += 1

                longest = max(longest, length)
        return longest