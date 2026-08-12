class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hash_table_s = {}
        hash_table_t = {}
        for i in range(len(s)):
            hash_table_s[s[i]] = 1 + hash_table_s.get(s[i], 0)
            hash_table_t[t[i]] = 1 + hash_table_t.get(t[i], 0)
        return hash_table_s == hash_table_t
