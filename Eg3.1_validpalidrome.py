# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
# https://leetcode.com/problems/valid-palindrome/description/
# rat  # cannot do % // on string
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        cleaned = ""
        
        for char in s:
            if char.isalnum():
                cleaned +=char.lower()
        return cleaned == cleaned[::-1] 
            

        

