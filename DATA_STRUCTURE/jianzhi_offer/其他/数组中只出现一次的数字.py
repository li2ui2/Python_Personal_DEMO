"""
一个整型数组里除了两个数字之外，其他的数字都出现了两次。
请写程序找出这两个只出现一次的数字。
"""


class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        d = {}
        for key in array:
            d[key] = d.get(key, 0) + 1
        ret = []
        for key in d:
            if d[key] == 1:
                ret.append(key)
        return ret