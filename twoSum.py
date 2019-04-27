from itertools import combinations
from typing import List


class Solution:

    def read_testcase(self):
        """
        Read and parse testcase example with a very long array
        :returns: nums, target
        """
        with open('twoSum_testcase1.txt', 'r') as f:
            nums = list(map(int, f.readline().lstrip('[').rstrip(']\n').split(',')))
            target = int(f.readline())

        return nums, target

    def twoSum(self, nums:
        List[int], target

        : int) -> List[int]:
        """
        Find the indices of the two numbers that sum to the target
        :returns: list of 2 indices
        """
        indices = list(range(len(nums)))

        # don't list it, takes up too much memory
        comb = combinations(indices, 2)
        #print(list(comb))

        # it says this is taking too long on long lists, so what if we say
        # do a binary search so we don't have to try all the combinations-?
        # that only makes sense if it's sorted

        for x in comb:
            first = x[0]
            second = x[1]
            total = sum([nums[first], nums[second]])
            # print(total)
            if total == target:
                #print(list(x))
                break

        return list(x)
