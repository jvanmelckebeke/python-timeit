import unittest
import time

from timeitpoj.timer.internal_timer import InternalTimer


class InternalTimerTests(unittest.TestCase):
    def test_internal_time_starts_at_zero(self):
        timer = InternalTimer()
        self.assertEqual(0, timer.internal_time)

    def test_context_manager_tracks_elapsed_time(self):
        with InternalTimer() as timer:
            time.sleep(0.1)

        self.assertAlmostEqual(timer.internal_time, 0.1, places=1)

    def test_multiple_context_managers_accumulate_elapsed_time(self):
        with InternalTimer() as timer1:
            time.sleep(0.1)

        with InternalTimer() as timer2:
            time.sleep(0.2)

        self.assertAlmostEqual(0.1, timer1.internal_time, places=1)
        self.assertAlmostEqual(0.2, timer2.internal_time, places=1)

    def test_nested_context_managers_accumulate_elapsed_time(self):
        with InternalTimer() as timer1:
            time.sleep(0.1)

            with InternalTimer() as timer2:
                time.sleep(0.2)

        self.assertAlmostEqual(0.3, timer1.internal_time, places=1)
        self.assertAlmostEqual(0.2, timer2.internal_time, places=1)


if __name__ == '__main__':
    unittest.main()
