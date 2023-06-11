import unittest
from timeitpoj.utils.misc import reformat_units, time_to_str, format_percentage, random_task_name


class MiscTestCase(unittest.TestCase):
    def test_reformat_units(self):
        # Test reformatting units
        self.assertEqual(reformat_units(0.005), (5.0, 'milliseconds'))
        self.assertEqual(reformat_units(0.00002), (20.0, 'microseconds'))
        self.assertEqual(reformat_units(0.0000003), (0.3, 'microseconds'))

        # Test start_unit parameter
        self.assertEqual(reformat_units(100, start_unit='milliseconds'), (100.0, 'milliseconds'))

    def test_time_to_str(self):
        # Test time formatting
        self.assertEqual(time_to_str(3.14159), '3.142 seconds')
        self.assertEqual(time_to_str(0.005, unit='milliseconds'), '5.000 microseconds')
        self.assertEqual(time_to_str(0.00002, unit='microseconds'), '0.020 nanoseconds')

    def test_format_percentage(self):
        # Test percentage formatting
        self.assertEqual(format_percentage(0.25), '[25.00%]')
        self.assertEqual(format_percentage(0.75, include_brackets=False), '75.00%')
        self.assertEqual(format_percentage(1.0), '[100.00%]')

    def test_random_task_name(self):
        # Test generation of random task names
        for _ in range(10):
            task_name = random_task_name()
            self.assertTrue(task_name.startswith('task'))
            self.assertTrue(' ' in task_name)


if __name__ == '__main__':
    unittest.main()
