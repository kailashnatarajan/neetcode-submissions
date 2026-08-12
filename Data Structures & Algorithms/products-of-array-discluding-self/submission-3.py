class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # i = 0
        # length = len(nums)
        # res = [0] * length
        # for i in range(length):
        #     pdt = 1
        #     for j in range(length):
        #         if i == j:
        #             continue
        #         pdt *= nums[j]
        #     res[i] = pdt
        # return res
        
        pdt = 1
        result = []
        for i in range(len(nums)):
            pdt = pdt * nums[i]
            result.append(pdt)
        pdt = 1
        for i in range(len(nums)-1, -1, -1):
            if i == 0:
                result[0] = pdt
                return result
            result[i] = result[i-1] * pdt
            pdt = pdt * nums[i]
