class Solution(object):
    def romanToInt(self, s):
        a = {'I' : 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000}
        s = s.replace('\"', '').replace('s = ', '')
        res = 0
        prev = 0
        for val in s[::-1]:
            current = a[val]
            if current >= prev: res += current
            else: res -= current
            prev = current
        return res
