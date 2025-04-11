from pycalc.operations.sum import sum

class TestOperations:

    def test_must_sum_correctly(self):
        assert sum(1, 10) == 11
        assert sum('1', '10') == 11
        assert sum(0, 0) == 0

