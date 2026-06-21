class Solution(object):
    def countCharacters(self, words, chars):
        x=0 

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
                x= x+1
                
        return x
    


words = ["hello", "hi", "hey", "world"]
chars = "hieyl"

obj = Solution()
answer = obj.countCharacters(words, chars)

print(answer)