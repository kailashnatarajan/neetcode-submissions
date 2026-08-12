class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_prefix = ""
        least_length = len(strs[0])
        least_word = strs[0]
        for word in strs:
            if len(word) < least_length:
                least_length = len(word)
                least_word = word
        
        for i in range(least_length):
            for word in strs:
                if word[i] != least_word[i]:
                    return common_prefix
            common_prefix += least_word[i]
        return common_prefix