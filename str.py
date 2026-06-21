class Solution(object):
    def countCharacters(self, words, chars):
        result = []

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
                result.append(word)
                
        return result


words = ["dog", "cat", "dad", "good"]
chars = "odgcat"

obj = Solution()
answer = obj.countCharacters(words, chars)

print(answer)