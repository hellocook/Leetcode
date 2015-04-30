class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
        maxhere = maxsum = A[0]
        for i in range(1,len(A)):
            if maxhere < 0:
                maxhere=A[i]
            else:
                maxhere += A[i]
            if maxhere>maxsum:
                maxsum=maxhere
        return maxsum
            
        
