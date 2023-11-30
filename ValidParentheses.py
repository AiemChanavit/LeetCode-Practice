class Solution(object):
    def isValid(self, s):
        stack = []
        for i in range(len(s)):
            if s[i] in '({[':
                   stack.append(s[i])
            else :
                   if not stack:
                        return False

                   pop_element = stack.pop()

                   if s[i] == ')' and pop_element != '(':
                        return False

                   elif s[i] == '}' and pop_element != '{':
                        return False

                   elif s[i] == ']' and pop_element != '[':
                        return False
        return not stack
                   

solution_instance = Solution()
input_string = "()[]{}"
result = solution_instance.isValid(input_string)
print(result)

        