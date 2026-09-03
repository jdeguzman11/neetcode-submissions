class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        if word == abbr:
            return True

        l, r = 0, 0

        while r < len(abbr):
            if abbr[r].isalpha():
                if l >= len(word) or abbr[r] != word[l]:
                    return False

                l += 1
                r += 1

            else:
                if abbr[r] == "0":
                    return False

                else:
                    num = 0

                    while r < len(abbr) and abbr[r].isdigit():
                        num = num * 10 + int(abbr[r])
                        r += 1
                    
                    l += num
                    if l > len(word):
                        return False
        return l == len(word)

