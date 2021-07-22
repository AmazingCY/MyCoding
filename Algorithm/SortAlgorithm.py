# -*- coding: utf-8 -*-
# @Time : 2021/7/21 22:52
# @Author : Cao yu
# @File : SortAlgorithm.py
# @Software: PyCharm

import random

class SortAlgorithm(object):
    __slots__ = ["__input_list"]

    def __init__(self, sort_list: list):
        self.__input_list = sort_list

    @property
    def input_list(self) -> list:
        return self.__input_list

    @input_list.setter
    def input_list(self, set_list):
        self.__input_list = set_list


    # 稳定排序
    def bubble_sort(self):
        BubbleSort = self.__input_list.copy()
        length = len(BubbleSort)
        for i in range(length):
            for j in range(1, length - i):
                if BubbleSort[j] <= BubbleSort[j - 1]:
                    BubbleSort[j], BubbleSort[j - 1] = BubbleSort[j - 1], BubbleSort[j]
        print("------------------Bubble Sort------------------")
        print(f"Before Sort: {self.__input_list}")
        print(f"After Bubble Sort: {BubbleSort}")
        print("Time complexity：O(n*n), Space complexity: O(1)")
        print("-----------------------------------------------")

    # 非稳定排序
    def quick_sort(self):
        QuickSort = self.__input_list.copy()

        def recursion(nums: list) -> list:
            if len(nums) < 2:
                return nums
            else:
                pivot = nums[0]
                front = [i for i in nums[1:] if i <= pivot]
                back = [j for j in nums[1:] if j > pivot]
                return recursion(front) + [pivot] + recursion(back)

        print("------------------Quick Sort------------------")
        print(f"Before Sort: {self.__input_list}")
        print(f"After Quick Sort: {recursion(QuickSort)}")
        print("Time complexity：O(nlog2n), Space complexity: O(nlog2n)")
        print("-----------------------------------------------")

    # 稳定排序
    def insert_sort(self):
        InsertSort = self.__input_list.copy()
        for index in range(1, len(InsertSort)):
            insert_data = InsertSort[index]
            current_index = index
            while current_index > 0 and InsertSort[current_index - 1] > insert_data:
                InsertSort[current_index] = InsertSort[current_index - 1]
                current_index -= 1
            InsertSort[current_index] = insert_data

        print("------------------Insert Sort------------------")
        print(f"Before Sort: {self.__input_list}")
        print(f"After Quick Sort: {InsertSort}")
        print("Time complexity：O(n*n), Space complexity: O(1)")
        print("-----------------------------------------------")

    # 非稳定排序
    def select_sort(self):
        SelectSort = self.__input_list.copy()
        def find_min_index(nums):
            a = nums[0]
            b = 0
            for index in range(len(nums)):
                if nums[index] < a:
                    a = nums[index]
                    b = index
            return b
        select_sort_res = []
        while SelectSort:
            min_index = find_min_index(SelectSort)
            select_sort_res.append(SelectSort.pop(min_index))

        print("------------------Select Sort------------------")
        print(f"Before Sort: {self.__input_list}")
        print(f"After Quick Sort: {select_sort_res}")
        print("Time complexity：O(n*n), Space complexity: O(1)")
        print("-----------------------------------------------")


if __name__ == "__main__":

    test = SortAlgorithm([random.randint(1, 10) for index in range(10)])
    test.bubble_sort()
    test.quick_sort()
    test.insert_sort()
    test.select_sort()

