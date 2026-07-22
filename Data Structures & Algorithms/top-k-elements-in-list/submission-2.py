class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        top = []

        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        for i in range(k):
            max_key = max(counts, key=counts.get)
            top.append(max_key)
            del counts[max_key]
        
        return top