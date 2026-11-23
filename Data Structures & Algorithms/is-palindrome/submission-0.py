class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_string = []
        for ch in s:
            if ch.isalnum():
                clean_string.append(ch.lower())
        return clean_string == clean_string[::-1]