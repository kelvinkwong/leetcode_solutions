#!/usr/bin/python3
import sys

class Solution:
    def intToRoman(self, num):
        conversion = {
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

        roman_str = ""
        res_p = num
        for conversion_digit, conversion_value in conversion.items():
            while res_p > 0:
                res_n = res_p - conversion_digit
                # print(f"res_n {res_n} = res_p {res_p} - conv {conversion_digit}")
                if res_n >= 0:
                    roman_str += conversion_value
                    res_p = res_n
                elif res_n < 0:
                    break
        return roman_str

if __name__ == "__main__":
    print(Solution.intToRoman(None, int(sys.argv[1])))
