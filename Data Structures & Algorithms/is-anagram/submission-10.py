class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if len(s) != len(t):
        #     return False
        # return sorted(s) == sorted(t)


        # if len(s) != len(t):
        #     return False
        # count = {}
        # for ch in s:
        #     count[ch] = count.get(ch, 0) + 1
        # for ch in t:
        #     if ch not in count or count[ch] == 0:
        #         return False
        #     count[ch] -= 1
        # return True


        if len(s) != len(t):
            return False
        count = [0] * 26 #since we 26 alphabets(lower-case) in english
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1 # count[ord(s[i]) - 97] += 1
            count[ord(t[i]) - ord('a')] -= 1 # count[ord(t[i]) - 97] -= 1
        for val in count:
            if val != 0:
                return False
        return True