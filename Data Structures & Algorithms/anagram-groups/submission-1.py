class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}
        anagrams_grp = []
        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word in hash_map:
                hash_map[sorted_word].append(word)
            else:
                hash_map[sorted_word] =  [word]
        for anagram in hash_map.values():
            anagrams_grp.append(anagram)
        return anagrams_grp

        