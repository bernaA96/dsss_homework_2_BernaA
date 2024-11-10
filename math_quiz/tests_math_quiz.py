import unittest
from math_quiz import random_int, random_operator, calculate


class TestMathGame(unittest.TestCase):
    """
    The TestMathGame class contains a set of tests to verify that the functions in the math_quiz module work correctly.
    These tests test random number and operator generation, and computational functions.
    """

    def test_random_int(self):
        """
        Tests whether the random_int() function generates random numbers within the given min_val and max_val limits.
        The number returned must be within the specified range.
        """
        min_value = 1
        max_value = 10

        for _ in range(1000):  # Testing a large number of random values

            random_number = random_int(min_value, max_value)  # Makes sure the number is between min_value and max_value
            self.assertTrue(min_value <= random_number <= max_value,
                            f"Generated number {random_number} is out of range [{min_value}, {max_value}]")

    def test_random_expression(self):
        """
        Checks that the random expression() function returns a valid operator ( +, -, * ).
        """
        valid_operators = ['+', '-', '*']
        re = random_operator()  # Picking a random operator and checking if it is in the valid operator list.

        self.assertIn(re, valid_operators, f"Generated operator {re} is not a valid operator in {valid_operators}")

    def test_calculate(self):
        """
        Tests the calculate() function with various inputs. Verifying that the expected problem and answering match
        the calculated result.
        """
        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (5, 2, '-', '5 - 2', 3),
            (5, 2, '*', '5 * 2', 10),
            (7, 3, '+', '7 + 3', 10),
            (7, 3, '-', '7 - 3', 4),
            (7, 3, '*', '7 * 3', 21),
            (-7, -3, '+', '-7 + -3', -10),  # Negative values tested here
            (-7, +3, '-', '-7 - 3', -10)  # Mixed negative and positive values

        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            generated_problem, calculated_answer = calculate(num1, num2,
                                                             operator)  # Calling the calculate() function and getting the return values.

            self.assertEqual(generated_problem, expected_problem,
                             f"Expression {generated_problem} does not match expected {expected_problem}")
            # Verifying the generated problem statement

            self.assertEqual(calculated_answer, expected_answer,
                             f"Result {calculated_answer} does not match expected {expected_answer}")
            # Verifying the calculated answer matches expected


if __name__ == "__main__":
    unittest.main()
