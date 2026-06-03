class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n=len(heights)
        ar=0
        m=0
        for i in range(n):
            for j in range(i+1,n):
                ar=min(heights[i],heights[j])*(j-i)
                m=max(m,ar)
        return m

        