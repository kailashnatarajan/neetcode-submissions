class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_table_s = {}
        hash_table_t = {}
        for ch in s:
            hash_table_s[ch] = hash_table_s.get(ch, 0) + 1
        for ch in t:
            hash_table_t[ch] = hash_table_t.get(ch, 0) + 1
        return hash_table_s == hash_table_t
