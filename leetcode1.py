from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for item in nums:
            for item2 in nums:
                if item + item2 == target:
                    if nums.index(item) == nums.index(item2):
                        if nums.count(item) == 1:
                            continue
                        else:
                            if item + item2 == target:
                                return [nums.index(item), nums.index(item2, nums.index(item) + 1)]

                    return [nums.index(item), nums.index(item2)]

    def twoSum_with_sorted_array(self, numbers: List[int], target: int) -> List[int]:
        for item in numbers:
            if target != 0 and item == 0:
                continue
            for item2 in numbers:
                if item + item2 == target:
                    if numbers.index(item) == numbers.index(item2):
                        if numbers.count(item) == 1:
                            continue
                        else:
                            if item + item2 == target:
                                return [numbers.index(item) + 1, numbers.index(item2, numbers.index(item) + 1) + 1]

                    return [numbers.index(item) + 1, numbers.index(item2) + 1]

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        n1 = self.addTwoNumbers_extract_from_list(l1)
        n2 = self.addTwoNumbers_extract_from_list(l2)
        result = n1 + n2
        if result == 0:
            return ListNode(0)
        lsi = []
        while result != 0:
            lsi.append(result % 10)
            result //= 10
        lsi = lsi[::-1]
        ls = ListNode(lsi[0])
        n = 1
        while n < len(lsi):
            tmp = ListNode(lsi[n])
            tmp.next = ls
            ls = tmp
            n += 1
        return ls

    def addTwoNumbers_extract_from_list(self, l1):
        n1 = l1.val
        licznik = 1
        l1 = l1.next
        while l1 is not None:
            n1 += l1.val * 10 ** licznik
            l1 = l1.next
            licznik += 1
        return n1

    def addBinary(self, a: str, b: str) -> str:
        return str(bin(int(a, 2) + int(b, 2)))[2::]

    def plusOne(self, digits: List[int]) -> List[int]:
        numb = 0
        licznik = 0
        if digits[0] == 0:
            return [1]
        for x in digits[::-1]:
            numb += x * (10 ** licznik)
            licznik += 1
        numb += 1
        digits = []
        while numb != 0:
            digits.append(numb % 10)
            numb //= 10
        return digits[::-1]

    def lengthOfLongestSubstring(self, s: str) -> int:
        # It's not optimal solution, 94% of solution on leetcode was faster than this
        if s == "":
            return 0
        elif len(s) ==1:
            return 1
        else:
            max_length = 0
            for y in range(0,len(s)-1):
                collection = []
                collection.append(s[y])
                for x in range(y+1,len(s)):
                    if not s[x] in collection:
                        collection.append(s[x])
                    else:
                        break
                max_length = max(max_length, len(collection))
            return max_length




class Run():
    @staticmethod
    def run_plus_one():
        apx = Solution()
        apx.plusOne([1, 2, 3])

    @staticmethod
    def run_add_two_number():
        apx = Solution()
        l1 = ListNode(2)
        l1.next = ListNode(4)
        l1.next.next = ListNode(3)
        l2 = ListNode(5)
        l2.next = ListNode(6)
        l2.next.next = ListNode(4)
        s = apx.addTwoNumbers(l1, l2)
        print(s)

    @staticmethod
    def run_two_sum():
        apx = Solution()
        print(apx.twoSum([3, 1, 2, 30, 8, 4], 6))
        print(apx.twoSum([3, 3], 6))
    @staticmethod
    def run_max_substring():
        apx = Solution()
        print(apx.lengthOfLongestSubstring(input()))


Run.run_max_substring()