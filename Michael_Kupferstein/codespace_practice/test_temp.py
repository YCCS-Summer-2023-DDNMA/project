from temp import add,sub

class TestTemp:
    def test_add(self):
        assert add(2,2) == 4
        assert add(3,7) == 10
    def test_sub(self):
        assert sub(10,5) == 5
        assert sub(7,3) == 4
    def test_both(self):
        assert sub(add(3,7),sub(6,1)) == 5
        assert add(sub(10,4),add(2,2)) == 10
