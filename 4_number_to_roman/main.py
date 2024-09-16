"""
เขียนโปรแกรมแปลงตัวเลขเป็นตัวเลข roman

[Input]
number: list of numbers

[Output]
roman_text: roman number

[Example 1]
input = 101
output = CI

[Example 2]
input = -1
output = number can not less than 0
"""


import argparse
import roman

class Solution:

    def number_to_roman(self, number: int) -> str:
        try:
            if number < 0:
                return f"number can not less than 0"
            else:
                return roman.toRoman(number)
        except Exception as e:
            return f"เกิดข้อผิดพลาด: {str(e)}"

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('number', type=int)

    args = parser.parse_args()

    sol = Solution()
    
    result = sol.number_to_roman(args.number)
    print(f"input = {args.number}")
    print(f"output = {result}")