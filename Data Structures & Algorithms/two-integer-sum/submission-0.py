class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indx = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in indx:
                return [indx[diff], i]
            indx[n] = i
        return