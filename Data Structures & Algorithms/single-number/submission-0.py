from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count=Counter(nums)
        ans=0
        for i,n in count.items():
            if n==1:
                ans=i
        return ans
        