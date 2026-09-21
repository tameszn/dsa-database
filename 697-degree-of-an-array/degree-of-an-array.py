class Solution:
    def findShortestSubArray(self, nums):
        d       = defaultdict(list) # Dictionary with [indexes] where each label appears
        m, best = 1, 1              # m = record degree, best = shortest span (for m)
        for i,x in enumerate(nums):
            d[x].append(i) # Add index to respective sub-array
            L =len(d[x])   # Track length of sub-array at label = x
            if L>m:
                # Initialize new Record
                m = L
                best = i - d[x][0] + 1
            elif L == m:
                # Pick best at highest degree
                best = min( best , i - d[x][0] + 1 )
        return best