class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash_map = {}
        for num in nums:
            hash_map[num] = hash_map.get(num, 0) + 1
        n = len(nums) // 2
        for num, count in hash_map.items():
            if count>n:
                return num
        