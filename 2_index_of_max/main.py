"""
เขียบนโปรแกรมหา index ของตัวเลขที่มีค่ามากที่สุดใน list

[Input]
numbers: list of numbers

[Output]
index: index of maximum number in list

[Example 1]
input = [1,2,1,3,5,6,4]
output = 5

[Example 2]
input = []
output = list can not blank
"""


import argparse


class Solution:

    def find_max_index(self, numberListStr: str) -> int | str:
        numberListStr = numberListStr.replace("[", "").replace("]", "")
        if len(numberListStr) == 0:
            return "list can not blank"
        
        numbers = numberListStr.split(",")
    
        max_value = max(numbers)
        max_index = numbers.index(max_value)
        return max_index
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('numberListStr', type=str)

    args = parser.parse_args()

    sol = Solution()
    
    result = sol.find_max_index(args.numberListStr)
    print(f"input = {args.numberListStr}")
    print(f"output = {result}")
