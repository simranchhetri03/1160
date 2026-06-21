class Solution(object):
    def countCharacters(self, words, chars):
        longest= ""

        for word in words:
            temp_chars = list(chars)
            can_make = True

            for letter in word:
                if letter in temp_chars:
                    temp_chars.remove(letter)
                else:
                    can_make = False
                    break

            if can_make:
                if len(word) > len(longest):
                    longest = word

        return longest


words = ["apple", "pen", "pale", "lap"]
chars = "aplepn"

obj = Solution()
answer = obj.countCharacters(words, chars)

print(answer)