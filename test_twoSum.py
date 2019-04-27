import unittest2
from twoSum import Solution

class TestTwoSum(unittest2.TestCase):

    def test_five_unique(self):
        nums = [2,7,11,15]
        target = 9
        solve = Solution()
        x = solve.twoSum(nums, target)
        assert x == [0,1]

    def test_two_identical(self):
        nums = [3,3]
        target = 6
        solve = Solution()
        x = solve.twoSum(nums, target)
        assert x == [0,1]

class TestTestCases(unittest2.TestCase):

    def test_read_testfile(self):
        solve = Solution()
        nums, target = solve.read_testcase()
        assert isinstance(nums, list)
        assert all([isinstance(x, int) for x in nums])
        assert isinstance(target, int)

    def test_long_example(self):
        "current solution takes 28s"
        solve = Solution()
        nums, target = solve.read_testcase()
        result = solve.twoSum(nums, target)
        assert isinstance(result, list)
        assert len(result) == 2

if __name__ == '__main__':
    unittest2.main()