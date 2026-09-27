class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        ans=[]
        ans=nums.copy()
        ans=ans+nums
        return ans

