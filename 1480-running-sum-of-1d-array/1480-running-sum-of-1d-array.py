class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        sum=0
        ans=[]

        for i in nums:
            sum+=i
            ans.append(sum)
    
        return ans
        