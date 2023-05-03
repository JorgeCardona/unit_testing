import sys
import unittest
import pytest
from operations.addition import addition

class TestPreProcessDataframe(unittest.TestCase):
    # Tests that addition(2, 3) returns 5.
    def test_happy_path_addition(self):
        assert addition(2, 3) == 5




    # Tests that addition(0, 0) returns 0.
    @unittest.skip("No Ejecutar esta Prueba")
    def test_happy_path_addition_zero(self):
        assert addition(0, 0) == 0
        
        
        
        
        
        
        

    # Tests that addition(2.5, 3.5) returns 6.0.
    @unittest.skipUnless(sys.platform.startswith("win"), "requires Windows operative system")
    def test_edge_case_addition_float(self):
        assert addition(2.5, 3.5) == 6.0









    # Tests that addition('2', '3') raises TypeError.
    def test_edge_case_addition_type_error(self):
        with pytest.raises(TypeError):
            addition("2", "3")






    # Tests that addition(-2, 2) returns 0.
    def test_happy_path_addition_negative(self):
        assert addition(-2, 2) == 0






    # Tests that addition([], []) raises TypeError.
    @unittest.expectedFailure
    def test_edge_case_addition_type_error_list(self):
        with pytest.raises(TypeError):
            addition([], [])








if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPreProcessDataframe)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
