from functions import Function

class TestFunction:
    def test_largest(self):
        assert Function.find_largest([1,3,4,3,1,3,6,12,56,63]) == 63
        assert Function.find_largest([-1,-2,-4,10,-590,100]) == 100

    def test_smallest_test(self):
        assert Function.find_smallest([1,3,4,3,1,3,6,12,56,63]) == 1
        assert Function.find_smallest([-1,-2,-4,10,-590,100]) == -590

    def test_is_integer(self):
        assert Function.is_integer_in_list(3, [1,2,3,4,5,6,7,8])
        assert Function.is_integer_in_list(-1, [0,1,2,3,4,5,6,-1])

