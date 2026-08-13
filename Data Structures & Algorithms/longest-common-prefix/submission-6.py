class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs == []:
            return ""
        min_len, min_word = len(strs[0]), strs[0]
        for word in strs:
            if len(word) < min_len:
                min_len = len(word)
                min_word = word
        longest_prefix = ''
        for i in range(min_len):
            for word in strs:
                if word[i] != min_word[i]:
                    break
            else:
                longest_prefix += min_word[i]
                continue
            break
        return longest_prefix