"""
เขียบนโปรแกรมแปลงตัวเลขเป็นคำอ่านภาษาไทย

[Input]
number: positive number rang from 0 to 10_000_000

[Output]
num_text: string of thai number call

[Example 1]
input = 101
output = หนึ่งร้อยเอ็ด

[Example 2]
input = -1
output = number can not less than 0
"""


import argparse
from num2words import num2words

class Solution:

    def number_to_thai(self, number: int) -> str:
        try:
            if number < 0:
                return f"number can not less than 0"
            else:
                return num2words(number, lang='th')
        except Exception as e:
            return f"เกิดข้อผิดพลาด: {str(e)}"

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('number', type=int)

    args = parser.parse_args()

    sol = Solution()
    
    result = sol.number_to_thai(args.number)
    print(f"input = {args.number}")
    print(f"output = {result}")