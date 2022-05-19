class Solution(object):
    def twoSum(self, numbers, target):
        a = []                                              #массив для сортировки
        for i in range(len(numbers)):
            a.append(numbers[i])
        a.sort()                                            #отсортированный массив
        for i in range(len(a)):                             #binary search
            minn = 0
            maxx = len(numbers) - 1
            diff = target - a[i]
            res = []
            while minn <= maxx:
                j = (minn + maxx) // 2
                if diff < a[j]:
                    maxx = j - 1
                elif diff > a[j]:
                    minn = j + 1
                elif diff == a[j] and j != i:
                    res = [numbers.index(a[i]), len(numbers) - numbers[::-1].index(diff) - 1]
                    break
                else:
                    break
            if res != []:
                return min(res), max(res)
