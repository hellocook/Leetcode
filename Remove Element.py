class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
           number = 0
           while elem in A:
                  A.remove(elem)
           return len(A)
A = [4,4,5]
s = Solution()
s.removeElement(A,4)
print (A)
