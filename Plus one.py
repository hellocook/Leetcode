class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        a = 0
        i = len(digits) - 1
        while i>=0:
               if i == len(digits) - 1:
                      if digits[i] + 1 >= 10:
                             digits[i] = digits[i]  - 9
                             a = 1
                      else:
                             digits[i] = digits[i] + 1
                             a = 0
               else:
                      digits[i] = digits[i] + a
                      if digits[i] >= 10:
                             digits[i] -=10
                             a = 1
                      else:
                             a = 0
               i -=1
        if a == 1:
               b = []
               b.append(1)
               #for k in range(len(digits)):
               #       b.append(digits[k])
               b.extend(digits)
               return b
        else:
               return digits

A = [9]
s=Solution()
print (s.plusOne(A))
