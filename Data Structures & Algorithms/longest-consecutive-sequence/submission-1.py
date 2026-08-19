class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set=set(nums)
        longest=0
        for num in num_set:
            if num-1 not in num_set:
                currnum=num
                currsteak=1
                while currnum+1 in num_set:
                    currnum+=1
                    currsteak+=1
                longest=max(longest,currsteak)
        return longest
        