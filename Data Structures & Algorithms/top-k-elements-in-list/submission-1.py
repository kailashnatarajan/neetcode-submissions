class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        hash_count = [None] * (len(nums) + 1)
        result = []
        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1
        for num,count in hashmap.items():
            if hash_count[count] != None:
                hash_count[count].append(num)
            else:
                hash_count[count] = [num]
        for i in range(len(nums), 0, -1):
            if hash_count[i] == None:
                continue
            for num in hash_count[i]:
                result.append(num)
                if len(result) == k:
                    return result