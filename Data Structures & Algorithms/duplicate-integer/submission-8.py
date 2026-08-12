class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # nums.sort()
        # if nums == []:
        #     return False
        # temp = nums[0]
        # for i in range(1, len(nums)):
        #     if nums[i] == temp:
        #         return True
        #     temp = nums[i]
        # return False

        hash_map = set()
        for num in nums:
            if num in hash_map:
                return True
            hash_map.add(num)
        return False