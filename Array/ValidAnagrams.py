class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = [0] * 52  

        for i in range(len(s)):
            count[ord(s[i]) - ord('A')] += 1
            count[ord(t[i]) - ord('A')] -= 1

        return all(x == 0 for x in count)
