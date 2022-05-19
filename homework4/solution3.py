#хэш-таблица o(n)

def twoSum(self, nums, target):
    a = {}
    for i, value in enumerate(nums):         #используем enumerate для получения индекса элемента и его значения
        remaining = target - nums[i]
        if remaining in a:
            return [i, a[remaining]]
        a[value] = i 
