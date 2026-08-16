class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sequence = set(nums)
        longest = 0

        for num in nums:
            if num - 1 not in sequence:
                curr = num
                length = 1

                while curr + 1 in sequence:
                    curr += 1
                    length += 1

                longest = max(longest, length)
        return longest