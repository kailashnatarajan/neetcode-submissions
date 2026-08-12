class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for word in strs:
            encoded_string += str(len(word)) + "#" + word
        return encoded_string
    # def decode(self, s: str) -> List[str]:
    #     decoded_strs = []
    #     i = 0
    #     while i < len(s):
    #         digit = ""
    #         while s[i].isdigit():
    #             digit += s[i]
    #             i += 1
    #         if s[i] == '#':
    #             word = ""
    #             i += 1
    #             for _ in range(int(digit)):
    #                  word += s[i]
    #                  i += 1
    #             decoded_strs.append(word)
    #             continue
    #         i += 1
    #     return decoded_strs

    def decode(self, s: str) -> List[str]:
        res, i = [], 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            res.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        return res





