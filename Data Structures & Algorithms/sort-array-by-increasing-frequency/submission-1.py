class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        count = {}
        res = []

        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        freq = [[] for _ in range(len(nums) + 1)]

        for num, frequency in count.items():
            freq[frequency].append(num)
        
        for frequency in range(1, len(freq)):
            freq[frequency].sort(reverse=True)

            for num in freq[frequency]:
                for _ in range(frequency):
                    res.append(num)
        return res
        
        
        
        

