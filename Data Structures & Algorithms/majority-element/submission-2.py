class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash_table = {}
        for n in nums:
            hash_table[n] = hash_table.get(n, 0) + 1
        length = len(nums)
        for n, count in hash_table.items():
            if count >= length//2:
                return n
     