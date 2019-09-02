from typing import List


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

    def defang_IP_addr(self, address: str) -> str:
        """
        Given a valid (IPv4) IP address, return a defanged version of that IP address.
        """
        return address.replace(".", "[.]")

    def to_lower(self, string: str) -> str:
        """
        Change upper letter to lower
        :param string: ONLY ASCII letter
        :return:
        """
        new_string = ""
        for char in string:
            if char.isupper():
                new_string = new_string + chr(ord(char) + 32)
            else:
                new_string = new_string + char
        return new_string
        # return string.lower() <- It also has 36ms runtime

    def numJewelsInStones(self, J: str, S: str) -> int:
        """
        Return number of jewels in stones
        :param J: representing the types of stones that are jewels
        :param S: representing the stones you have
        :return:number of jewels in stones (J in S, case-sensitive)
        """
        list_of_stones = list(S)
        list_of_jewels = list(J)
        num_of_jewels = 0
        for jewel in list_of_jewels:
            num_of_jewels += list_of_stones.count(jewel)
        return num_of_jewels

    def reverseVowels(self, s: str) -> str:
        """
        Return word with reserved vowels
        :param s: str
        :return: str with reserved vowels e.g. hello -> holle
        """
        new_string = ""
        list_of_vowels = []
        vowels = ["a", "e", "i", "o", "u","A","E","I", "O","U"]
        for char in s:
            if char in vowels:
                list_of_vowels.append(char)
        list_of_vowels = list_of_vowels[::-1]
        index = 0
        for char in s:
            if char in vowels:
                new_string = new_string + list_of_vowels[index]
                index += 1
            else:
                new_string = new_string + char
        return new_string

    def find_words(self, words: List[str]) -> List[str]:
        """
        Return list of words (contains only alphabet letter) that can be typed using only one row of American keyboard
        :param words: list of words
        :return: List of words which  meet the condition.
        """
        first_row = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p"]
        second_row = ["a","s", "d", "f", "g", "h", "j", "k","l"]
        third_row = ["z", "x", "c","v","b","n","m"]
        keyboard = [first_row, second_row, third_row]
        result = []
        for word in words:
            for row in keyboard:
                is_one_row = True
                for char in word:
                    if char.lower() not in row:
                        is_one_row = False
                        break
                if is_one_row:
                    result.append(word)
                    break
        return result


if __name__ == "__main__":
    a = Solution()
    print(a.find_words(["Allaska"]))
    print(a.roman_to_int(input()))
