class Solution:
    # @param A a list of integers
    # @return nothing, sort in place
    def sortColors(self, A):
        if not A:
            return []
        else:
            self.sort2(0,len(A)-1,A)
    def sort2(self,start,end,A):
        if start <= end:
            middle = self.QuickSort(start,end,A)
            print (middle)
            self.sort2(start,middle - 1,A)
            self.sort2(middle + 1,end,A)
    def QuickSort(delf,start,last,A):
        i = start
        k = start
        while (k < last):
            if A[k] < A[last]:
                var = A[k]
                A[k] = A[i]
                A[i] = var
                i = i + 1
            k = k +1
                
        var = A[i]
        A[i] = A[last]
        A[last] = var
        return i
                
A = [5,2,4,1,0,4,9,5]
s = Solution()
s.sortColors(A)
print (A)

