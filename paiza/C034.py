eq = input()
left, right = [num.replace(" ", "") for num in eq.split("=")]

import re

def calc(left):
    nums = re.findall(r"[\+\-]?.?\d", left)
    nums = list(map(int, nums))
    ans = sum(nums)
    return ans * -1 if ans < 0 else ans

if ("x" in left):
    left += "-"+right
print(calc(left))

