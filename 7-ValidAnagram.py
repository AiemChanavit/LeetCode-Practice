class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        HashS = {}
        HashT = {}

        for i in range(len(s)):
            if s[i] in HashS:
                count = HashS.get(s[i])
                HashS[s[i]] = count + 1
            else:
                HashS[s[i]] = 0
        
        for i in range(len(t)):
            if t[i] in HashT:
                count = HashT.get(t[i])
                HashT[t[i]] = count + 1
            else:
                HashT[t[i]] = 0
        
        return HashS == HashT
    

solution_instance = Solution()
s = "rat"
t = "car"
result = solution_instance.isAnagram(s,t)
print(result)