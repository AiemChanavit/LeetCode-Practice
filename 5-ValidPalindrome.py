class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = 0
        right = len(s)-1

        while left < right:
            if not s[left].isalnum():
                left +=1
            
            elif not s[right].isalnum():
                right -=1

            elif s[left].isalnum() and s[right].isalnum() and s[left].lower() == s[right].lower():
                left += 1
                right -= 1
            else:
                return False
        return True 


solution_instance = Solution()
s = "A man, a plan, a canal: Panama"
result = solution_instance.isPalindrome(s)
print(result)