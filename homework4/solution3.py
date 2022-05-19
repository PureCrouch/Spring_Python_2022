#хэш-таблица o(n)

def twoSum(self, nums, target):
    seen = {}
    for i, value in enumerate(nums):         #используем enumerate для получения индекса элемента и его значения
        remaining = target - nums[i]
        if remaining in seen:
            return [i, seen[remaining]]
        seen[value] = i 
