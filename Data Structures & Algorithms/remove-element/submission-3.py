class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        while nums:
            try:
                if nums[i] == val:
                    nums.pop(i)
                else:
                    i += 1
            except IndexError:
                return len(nums)
        return len(nums)

        