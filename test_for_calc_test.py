import calc_test

class TestCalculator:

    def test_addition(self):
        assert 4 == calc_test.add(2,2)

    
    def test_subtraction(self):
        assert 2 == calc_test.subtract(4,2)


