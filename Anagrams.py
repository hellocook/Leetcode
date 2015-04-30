import collections
class Solution:
    # @param strs, a list of strings
    # @return a list of strings
    def anagrams(self, strs):
        d = collections.defaultdict(list)
        result = []
        for i in strs:
            val = tuple(sorted(i))
            d[val].append(i)
        for i in d.keys():
            if len(d[i]) > 1:
                result.extend(d[i])
        return result

s = Solution()
voca = ["cab","tin","pew","duh","may","cba","buy","bar","max","abc"]
print (s.anagrams(voca))

