import unittest
from student_utils import calculate_average, is_passing, get_grade

class TestStudentUtils(unittest.TestCase):
    def test_ordinary_arithmetic(self):
        self.assertEqual(calculate_average([80, 90, 100]), 90.0)
        
    def test_single_element_no_crash(self):
        self.assertEqual(calculate_average([40]), 40.0)

    def test_clearly_above_mark(self):
        self.assertTrue(is_passing(41))

    def test_exactly_at_pass_mark(self):
        self.assertTrue(is_passing(40))

    def test_just_below_mark(self):
        self.assertFalse(is_passing(39))

    def test_top_band(self):
        self.assertEqual(get_grade(95), "Distinction")

    def test_first_band(self):
        self.assertEqual(get_grade(60), "First")

    def test_second_band(self):
        self.assertEqual(get_grade(45), "Second")

    def test_below_all_bands(self):
        self.assertEqual(get_grade(30), "Fail")
        
    def test_perfect_score_upper_bounds(self):
        self.assertEqual(get_grade(100), "Distinction")

if __name__ == '__main__':
    unittest.main(argv=[""], exit=False)