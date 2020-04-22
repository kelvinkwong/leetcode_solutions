#!/usr/bin/python3
import sys

class Solution:
    def intToRoman(self, num):
        roman_conversion_table = {
            1000: "M",
            900: "CM",
            500: "D",
            400: "CD",
            100: "C",
            90: "XC",
            50: "L",
            40: "XL",
            10: "X",
            9: "IX",
            5: "V",
            4: "IV",
            1: "I"
        }

        roman_ans = ""
        res_p = num
        for integer in roman_conversion_table.keys():
            while res_p:
                res_n = res_p - integer
                # print(f"res_n {res_n} = res_p {res_p} - conv {integer}")
                if res_n >= 0:
                    roman_ans += roman_conversion_table[integer]
                    res_p = res_n
                else:
                    break
        return roman_ans

if __name__ == "__main__":
    print(Solution.intToRoman(None, int(sys.argv[1])))
