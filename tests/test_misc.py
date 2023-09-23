import unittest
from timeitpoj.utils.misc import reformat_units, time_to_str, format_percentage, random_task_name


class MiscTestCase(unittest.TestCase):
    def test_reformat_units(self):
        # Test reformatting units
        self.assertEqual((5.0, 'milliseconds'), reformat_units(0.005))
        self.assertEqual((20.0, 'microseconds'), reformat_units(0.00002))
        self.assertEqual((0.3, 'microseconds'), reformat_units(0.0000003))

        # Test start_unit parameter
        self.assertEqual((100.0, 'milliseconds'), reformat_units(100, start_unit='milliseconds'))

    def test_time_to_str(self):
        # Test time formatting
        self.assertEqual('3.142 seconds', time_to_str(3.14159))
        self.assertEqual('5.000 microseconds', time_to_str(0.005, unit='milliseconds'))
        self.assertEqual('0.020 nanoseconds', time_to_str(0.00002, unit='microseconds'))

        # Test minute formatting
        self.assertEqual('1 minutes 1.000 seconds', time_to_str(61))
        self.assertEqual('2 minutes', time_to_str(120))

    def test_format_percentage(self):
        # Test percentage formatting
        self.assertEqual('[25.00%]', format_percentage(0.25))
        self.assertEqual('75.00%', format_percentage(0.75, include_brackets=False))
        self.assertEqual('[100.00%]', format_percentage(1.0))

    def test_random_task_name(self):
        # Test generation of random task names
        for _ in range(10):
            task_name = random_task_name()
            self.assertTrue(task_name.startswith('task'))
            self.assertTrue(' ' in task_name)


if __name__ == '__main__':
    unittest.main()
