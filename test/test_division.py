import unittest
import pytest
from operations.division import division

class TestPreProcessDataframe(unittest.TestCase):
    
    
    
    
    
    
    
    # Tests that division returns the correct result for happy paths.
    def test_happy_path_division(self):
        assert division(10, 2) == 5
        assert division(100, 25) == 4






    # Tests that division raises ZeroDivisionError when dividing by zero.
    def test_edge_case_division_by_zero(self):
        with pytest.raises(ZeroDivisionError):
            division(10, 0)
            
            
            
            
            
            
            
            
            
            

    # Tests that division returns the correct result when x is infinity.
    def test_edge_case_division_inf(self):
        assert division(float("inf"), 2) == float("inf")
        assert division(float("-inf"), 2) == float("-inf")












    # Tests that division handles negative numbers correctly.
    def test_general_behavior_division_negative_numbers(self):
        assert division(-10, 2) == -5
        assert division(10, -2) == -5














    # Tests that division returns NaN when x is NaN.
    def test_edge_case_division_nan(self):
        assert division(float("nan"), 2) != division(float("nan"), 3)
















    # Tests that division handles rounding errors correctly.
    def test_general_behavior_division_rounding_errors(self):
        assert division(1, 3) == pytest.approx(0.3333333333, 0.0001)
        assert division(1, 7) == pytest.approx(0.1428571428, 0.0001)


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPreProcessDataframe)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
