class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        
        cleaned=""
        for char in s:
            if char.isalnum():
                cleaned+=char
        
        rev=""
        for c in range(len(cleaned)-1,-1,-1):
            rev= rev+cleaned[c]
        
        if rev==cleaned:
            return True
        
        else:
            return False
