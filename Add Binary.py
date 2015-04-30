import string
class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        length_a = len(a)
        length_b = len(b)
        c = []
        var = 0
        while length_a > 0 or length_b > 0:
                    if length_a == 0 and length_b != 0:
                        value1 = int(b[length_b - 1]) + var
                        if value1 >= 2:
                            var = 1
                            value1 -= 2
                        else:
                            var = 0
                        c.append(str(value1))
                        length_b -= 1
                    elif length_b == 0 and length_a != 0:
                        value2 = int(a[length_a - 1])  + var
                        if value2 >= 2:
                            var = 1
                            value2 -= 2
                        else:
                            var = 0
                        c.append(str(value2))
                        length_a -= 1
                    else:
                        value = int(a[length_a - 1]) + int(b[length_b - 1] ) + var
                        if value >= 2:
                            var = 1
                            value -= 2
                        else:
                            var = 0
                        c.append(str(value))
                        length_b -= 1
                        length_a -= 1
        if var == 1:
            c.append('1')
        c.reverse()
        return ''.join(c)

if __name__ == '__main__':
    s = Solution()
    c = s.addBinary("1010","1011")
    print (c)

    
        
