class Solution:
    """
    @param reader: An instance of ArrayReader.
    @param target: An integer
    @return: An integer which is the first index of target.
    """
    def searchBigSortedArray(self, reader, target):
        # write your code here
        end=1
        while reader.get(end)<target:
            end*=2
        start=0
        
        while start+1<end:
            mid=start+(end-start)//2
            if reader.get(mid)<target:
                start=mid
            else:
                end=mid
        if reader.get(start)==target:
            return start
        if reader.get(end)==target:
            return end
        return -1