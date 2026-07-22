class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        snums = sorted(nums)
        valid = []

        for i in range(len(snums) - 2):
            if i > 0 and snums[i] == snums[i - 1]:
                continue

            left = i + 1
            right = len(snums) - 1

            while left < right:
                total = snums[i] + snums[left] + snums[right]
                
                if total == 0:
                    valid.append([snums[i], snums[left], snums[right]])
                    left += 1
                    right -= 1

                    while left < right and snums[left] == snums[left - 1]:
                        left += 1

                    while left < right and snums[right] == snums[right + 1]:
                        right -= 1

                elif total < 0:
                    left += 1

                else:
                    right -= 1

        return valid
