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

    def twoSum(self, nums:List[int], target: int) -> List[int]:
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

    def binary_search(self, nums:List[int], target: int) -> List[int]:
        """
        Sort first, then search?
        """
        #indexed = sorted({x:i for i,x in enumerate(nums)})
        #print(sorted)

        #logic is:
        # if target > last 2 in the left half, just do the right half
        # elif target < first 2 in the right half, just do the left half

        #total = 0
        if len(nums) < 5:
            self.my_comb(nums, target)
        else:
            mid = len(nums) // 2

            if target > nums[mid - 1] + nums[mid - 2]:
                right = nums[mid:]
                self.my_comb(right, target)
                #return self.binary_search(right, target)
            elif target < nums[mid + 1] + nums[mid + 2]:
                left = nums[0:mid]
                self.my_comb(left, target)
            #return self.binary_search(left, target)

    def my_comb(self, nums:List[int], target:int) -> List[int]:
        """
        Create combinations and indices at the same time
        :return: result structure is [index, index]
        """
        total = 0

        for i,x in enumerate(nums):
            # print(f"total:{total}")
            # print(f"i:x {i,x}")
            total += x
            for j,y in enumerate(nums[i+1:]):
                # print(f"total:{total}")
                # print(f"j,y: {j,y}")
                if (total + y) == target:
                    # print(f"total:{total+y}")
                    # print(f" result: {i,j+i+1}")
                    return [i,j+i+1]
            else:
                total = 0
                continue
        return [i,j+i+1]


"""Runtime: 5124 ms, faster than 22.34% of Python3 online submissions for Two Sum.
Memory Usage: 13.6 MB, less than 48.21% of Python3 online submissions for Two Sum."""