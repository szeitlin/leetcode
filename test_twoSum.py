import unittest2
from twoSum import Solution

class TestTwoSum(unittest2.TestCase):

    def test_five_unique(self):
        nums = [2,7,11,15]
        target = 9
        solve = Solution()
        #x = solve.twoSum(nums, target)
        x = solve.binary_search(nums, target)
        assert x == [0,1]

    def test_five_unique_mycomb(self):
        nums = [2,7,11,15]
        target = 9
        solve = Solution()
        result = solve.my_comb(nums, target)
        assert result == [0, 1]

    def test_two_identical(self):
        nums = [3,3]
        target = 6
        solve = Solution()
        #x = solve.twoSum(nums, target)
        x = solve.binary_search(nums, target)
        assert x == [0,1]

    def test_two_identical_mycomb(self):
        nums = [3,3]
        target = 6
        solve = Solution()
        result = solve.my_comb(nums, target)
        assert result == [0, 1]

    def test_three(self):
        nums = [3,2,3]
        target = 6
        solve = Solution()
        result = solve.my_comb(nums, target)
        assert result == [0,2]

    def test_three_two(self):
        nums = [3,2,4]
        target = 6
        solve = Solution()
        result = solve.my_comb(nums, target)
        assert result == [1,2]

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

    def test_long_example_mycomb(self):
        solve = Solution()
        nums, target = solve.read_testcase()
        result = solve.my_comb(nums, target)
        assert isinstance(result, list)
        assert len(result) == 2

class TestMyComb(unittest2.TestCase):

    def test_simple_comb(self):
        nums = [10,20,30]
        target = 50
        solve = Solution()
        result = solve.my_comb(nums, target)
        assert result == [1,2]

if __name__ == '__main__':
    unittest2.main()