import unittest
from math_quiz import rand_int, rand_operator, problem_answer
class TestMathGame(unittest.TestCase):
    def test_rand_int(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = rand_int(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)
    def test_rand_operator(self):# Test if random operators generated are within the selected operators
        for _ in range(1000):# Test a large number of random values
            rand_op= rand_operator()
            self.assertTrue(rand_op in ['+', '-', '*'])
    def test_problem_answer(self):
            test_cases = [(5, 2, '+', '5 + 2', 7),(7,2,'-','7 - 2',5),
                (3, 4, '*', '3 * 4', 12),(10, 5, '+', '10 + 5', 15),
                (8, 2, '*', '8 * 2', 16),(15, 3, '-', '15 - 3', 12)]
            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                actual_problem,actual_answer=problem_answer(num1, num2, operator)
                self.assertTrue(actual_problem == expected_problem and actual_answer == expected_answer)
if __name__ == "__main__":
    unittest.main()
