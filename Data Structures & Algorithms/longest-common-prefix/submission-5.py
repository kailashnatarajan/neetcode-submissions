class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_prefix = ""
        shortest = min(strs, key=len)
        
        for i in range(len(shortest)):
            for word in strs:
                if word[i] != shortest[i]:
                    return common_prefix
            common_prefix += shortest[i]
        return common_prefix