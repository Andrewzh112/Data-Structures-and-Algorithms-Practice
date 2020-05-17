class Solution:
    """
    @param A: an integer array
    @return: nothing
    """

    def sortIntegers2(self, A):
        # Quick sort
        self.quick_sort(0, len(A) - 1, A)
        return A

    def quick_sort(self, left, right, A):
        if left >= right:
            return

        start, end = left, right
        pivot = A[start + (end - start) // 2]

        while start <= end:
            while start <= right and A[start] < pivot:
                start += 1
            while end >= left and A[end] > pivot:
                end -= 1

            if start <= end:
                A[start], A[end] = A[end], A[start]
                start += 1
                end -= 1

        self.quick_sort(left, end, A)
        self.quick_sort(start, right, A)