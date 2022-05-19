#хэш-таблица o(n)

def twoSum(self, nums, target):
    a = {}
    for i, value in enumerate(nums):         #используем enumerate для получения индекса элемента и его значения
        ost = target - nums[i]
        if ost in a:
            return [i, a[ost]]
        a[value] = i 
