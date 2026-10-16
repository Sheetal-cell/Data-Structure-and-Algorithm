class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l=len(nums)
        k=0
        for i in range(l):
            if nums[i]!=0:
                nums[k]=nums[i]
                k+=1

        for i in range(k,l):
            nums[i]=0
        