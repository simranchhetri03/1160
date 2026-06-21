class Solution(object):
    def countCharacters(self, words, chars):
        total = 0

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
                total += len(word)

        return total


words = ["cat", "bt", "hat", "tree"]
chars = "atach"

obj = Solution()
answer = obj.countCharacters(words, chars)

print(answer)