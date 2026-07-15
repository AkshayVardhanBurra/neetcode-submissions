class Solution:
    def isPalindrome(self, s: str) -> bool:


        last_letter = s[len(s) - 1]
        print(last_letter)
        if not last_letter.isalnum():
            s = s[0:len(s) - 1]

        
        
        i = 0
        b = len(s) - 1

        while i <= b:

            if not s[i].isalnum():
                i += 1
                continue
            
            if not s[b].isalnum():
                b -= 1
                continue

            if s[i].lower() != s[b].lower():
                return False
            i += 1
            b -= 1

            

            
        
        return True
        

#returns a string with all the spaces removed
    def removeSpaces(self, word):

        new_word = ""
        for letter in word:
            if letter.isalnum():
                new_word += letter

        return new_word