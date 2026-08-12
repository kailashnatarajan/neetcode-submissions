class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # nums.sort()
        # for i in range(1, len(nums)):
        #     if nums[i] == ums[i - 1]:
        #         return True
        # return False

        # hash_map = set()
        # for num in nums:
        #     if num in hash_map:
        #         return True
        #     hash_map.add(num)
        # return False

        return len(set(nums)) < len(nums)