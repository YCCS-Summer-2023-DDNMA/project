import functions
import unittest

class FunctionTests(unittest.TestCase):
    def largest_test(self):
        assert functions.find_largest([1,3,4,3,1,3,6,12,56,63]) == 63
        assert functions.find_largest([-1,-2,-4,10,-590,100]) == 100

    def smallest_test(self):
        assert functions.find_smallest([1,3,4,3,1,3,6,12,56,63]) == 1
        assert functions.find_smallest([-1,-2,-4,10,-590,100]) == -590

    def is_integer(self):
        assert functions.is_integer_in_list(3, [1,2,3,4,5,6,7,8])
        assert functions.is_integer_in_list(-1, [0,1,2,3,4,5,6,-1])