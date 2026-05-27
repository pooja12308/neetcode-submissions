class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.binarysearch(0,len(nums)-1,target,nums)
    
    def binarysearch(self,l:int,h:int,t:int,nums:List[int]):
        l=l
        h=h
        
        if l>h:
            return -1

        m=int((l+h)/2)
        if t==nums[m]:
            return m
        elif t<nums[m]:
            h=m-1
            return self.binarysearch(l,h,t,nums)
        else:
            l=m+1
            return self.binarysearch(l,h,t,nums)