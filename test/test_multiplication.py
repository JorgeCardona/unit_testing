from __future__ import annotations

import unittest

from operations.multiplication import multiplication


class TestPreProcessDataframe(unittest.TestCase):
    
    # Tests that multiplication of two positive integers returns correct result.
    def test_happy_path_multiplication_integers(self):
        assert multiplication(2, 3) == 6




    # Tests that multiplication of zero with any integer returns zero.
    def test_edge_case_multiplication_zero(self):
        assert multiplication(0, 5) == 0
        
        
        
        

    # Tests that multiplication of two negative integers returns correct result.
    def test_edge_case_multiplication_negative(self):
        assert multiplication(-2, -3) == 6
        
        
        
        
        
        
        
        
        
        

    # Tests that multiplication of large numbers does not cause overflow.
    def test_important_multiplication_overflow(self):
        assert multiplication(999999999, 999999999) == 999999998000000001




    # Tests that multiplication of two positive floats returns correct result.
    def test_general_behavior_multiplication_floats(self):
        assert multiplication(2.5, 3.5) == 8.75










    # Tests that multiplication of a positive integer and a negative float returns correct result.
    def test_general_behavior_multiplication_mixed(self):
        assert multiplication(-2, 3.5) == -7.0





if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPreProcessDataframe)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
