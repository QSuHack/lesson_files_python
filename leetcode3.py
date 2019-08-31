# from typing import List


class Solution:
    @staticmethod
    def reverse(self, x: int) -> int:
        """
        Return reversed int32, if reversed int overflow int32 it return 0
        """
        if x > 0:
            return int(str(x)[::-1]) if int(str(x)[::-1]) < 2147483648 else 0
        else:
            return -int(str(abs(x))[::-1]) if -int(str(abs(x))[::-1]) > -2147483648 else 0

    def roman_to_int(self, s: str) -> int:
        """
        Roman system to decimal
        """
        decimal_value = 0
        index = 0
        index2 = 0
        dict_of_values_roman_number = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        minus_list = [("I", "V"), ("I", "X"), ("X", "L"), ("X", "C"), ("C", "D"), ("C", "M")]
        roman_char_list = list(dict_of_values_roman_number.keys())[::-1]
        while index2 < len(roman_char_list):
            while s[index] == roman_char_list[index2]:
                decimal_value += dict_of_values_roman_number[roman_char_list[index2]]
                if index + 1 < len(s) and (s[index], s[index + 1]) in minus_list:
                    decimal_value += dict_of_values_roman_number[s[index + 1]]
                    decimal_value -= (dict_of_values_roman_number[s[index]] * 2)
                    index += 1
                index += 1
                if index >= len(s):
                    return decimal_value

            index2 += 1
        return decimal_value


a = Solution()

print(a.romanToInt(input()))
