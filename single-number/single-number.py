class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = {}
        for i in nums:
            if i not in count:
                count[i] = 1
            else: 
                del count[i]
        return list(count)[0]