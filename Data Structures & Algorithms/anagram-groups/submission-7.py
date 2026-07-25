class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for s in strs:
            sorted_anagram = "".join(sorted(s))
            if sorted_anagram in anagrams:
                anagrams[sorted_anagram].append(s)
            else:
                anagrams[sorted_anagram] = []
                anagrams[sorted_anagram].append(s)
        return list(anagrams.values())