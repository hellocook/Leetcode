class Solution:
    # @param num, a list of integers
    # @return a string
    def largestNumber(self, num):
        #num = map(str,num)
        num = [str(i) for i in num]
        num.sort(cmp=self.myCmp,reverse=True)
        return str(int("".join(num)))
    def myCmp(self, a, b):
        if a+b > b+a:
            return 1
        elif a+b < b+a:
            return -1
        else:
            return 0
       
s = Solution()
l = [3,30,34,5,9]
print (s.largestNumber(l))
