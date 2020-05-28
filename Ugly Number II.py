class Solution:
    """
    @param n: An integer
    @return: return a  integer as description.
    """
    def nthUglyNumber(self, n):
        # write your code here
        import heapq
        heap = [1]
        seen = set([1])
        
        val = None
        for i in range(n):
            val = heapq.heappop(heap)
            for factor in [2, 3, 5]:
                if val*factor not in seen:
                    seen.add(val*factor)
                    heapq.heappush(heap, val*factor)
        return val
            