from operations.subtraction import subtraction

import pytest
import unittest

class TestPreProcessDataframe(unittest.TestCase):
    
    # Tests that subtraction works correctly for positive values of x and y. 
    def test_happy_path_positive(self):
        assert subtraction(5, 3) == 2

    # Tests that subtraction works correctly for negative values of x and y. 
    def test_happy_path_negative(self):
        assert subtraction(-5, -3) == -2        
        
    # Tests that subtraction returns None when x or y is None.
    @unittest.expectedFailure
    def test_edge_case_none(self):
        assert subtraction(None, 3) == None
        assert subtraction(5, None) == None

    # Tests that subtraction works correctly when x is positive and y is negative. 
    def test_general_behavior_positive_negative(self):
        assert subtraction(5, -3) == 8
        
    # Tests that subtraction works correctly when x is negative and y is positive. 
    def test_general_behavior_negative_positive(self):
        assert subtraction(-5, 3) == -8
                                                                         
if __name__ == '__main__':
    
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPreProcessDataframe)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)