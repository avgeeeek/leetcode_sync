class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        arr=[[]]
        for j in nums:
            arr+=[i+[j] for i in arr]
        return arr