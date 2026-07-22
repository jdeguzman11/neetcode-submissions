class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for s in strs:
            sorted_text = "".join(sorted(s))
            if sorted_text in anagrams:
                anagrams[sorted_text].append(s)

            else:
                anagrams[sorted_text] = []
                anagrams[sorted_text].append(s)

        return list(anagrams.values())
            