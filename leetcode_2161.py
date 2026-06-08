# class Solution:
#     def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
#         n=len(nums)
#         if n==1: return nums
#         R=[]
#         l, m=0, 0
#         for x in nums:
#             if x<pivot:
#                 nums[l]=x
#                 l+=1
#             elif x>pivot:
#                 R.append(x)

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        n=len(nums)
        if n==1: return nums
        k=[]
        l=[]
        piv=[]
        
        for i in range(len(nums)):
            if nums[i]>pivot:
                k.append(nums[i])
            elif nums[i]< pivot:
                l.append(nums[i])
            elif nums[i]==pivot:
                piv.append(nums[i])
             
        
        result=[]
        result=l+piv+k
        return result




