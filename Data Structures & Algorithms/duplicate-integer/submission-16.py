class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # for i in range(len(n)):
        #     for j in range(i+1, len(n)):
        #         if nums[i] == nums[j]:
        #             return True
        # return False

        # nums.sort()
        # if len(nums) == 1:
        #     return False
        # for i in range(len(nums)):
        #     if nums[i] == nums[i - 1]:
        #         return True
        # return False

        # hashset = set()
        # for n in nums:
        #     if n in hashset:
        #         return True
        #     hashset.add(n)
        # return False

        return len(set(nums)) != len(nums)






