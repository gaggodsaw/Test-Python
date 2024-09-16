"""
เขียนโปรแกรมหาจำนวนเลข 0 ที่อยู่ติดกันหลังสุดของค่า factorial โดยห้ามใช้ function from math

[Input]
number: as an integer

[Output]
count: count of tailing zero as an integer

[Example 1]
input = 7
output = 1

[Example 2]
input = -10
output = number can not be negative
"""


import argparse


class Solution:

    def find_tailing_zeroes(self, number: int) -> int | str:
        count = 0
        i = 5
        while number // i > 0:
            count += number // i
            i *= 5
        return count
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('number', type=int)

    args = parser.parse_args()

    sol = Solution()
    
    result = sol.find_tailing_zeroes(args.number)
    print(f"input = {args.number}")
    print(f"output = {result}")