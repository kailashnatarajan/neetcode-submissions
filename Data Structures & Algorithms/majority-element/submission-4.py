class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Brute Force Approach
        # max_ctr, num = 0, nums[0]
        # for i in range(len(nums)):
        #     ctr = 1
        #     for j in range(i+1, len(nums)):
        #         if nums[i] == nums[j]:
        #             ctr += 1
        #     if ctr > max_ctr:
        #         max_ctr = ctr
        #         num = nums[i]
        # return num

        # Using Hash_Table
        hash_table = {}
        for n in nums:
            hash_table[n] = hash_table.get(n, 0) + 1
        length = len(nums)
        for n, count in hash_table.items():
            if count >= length//2:
                return n