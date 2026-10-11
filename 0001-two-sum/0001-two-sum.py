class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        dict={}
        for i, x in enumerate(nums):
            need = target-x
            if need in dict:
                return [dict[need],i]
            dict[x]=i
        