import unittest
from time import sleep

from timeitpoj import TimeIt

BASE_TIME = 0.1


class IntegrationTests(unittest.TestCase):
    def test_simple_timer(self):
        with TimeIt("simple timer") as timer:
            sleep(BASE_TIME)

        print(timer)

        self.assertAlmostEqual(BASE_TIME, timer.elapsed_time, places=1)

    def test_single_nested_timer(self):
        with TimeIt("nested timer") as timer:
            sleep(BASE_TIME)
            with timer("task"):
                sleep(BASE_TIME)

        print(timer)
        self.assertAlmostEqual(BASE_TIME, timer.elapsed_time, places=1)

    def test_complex_nested_timer(self):
        with TimeIt("complex nested timer") as timer:
            sleep(BASE_TIME)
            with timer("parent task"):
                sleep(BASE_TIME)
                with timer("1st child task"):
                    sleep(BASE_TIME)
                with timer("2nd child task"):
                    sleep(BASE_TIME)
                with timer("3th child task"):
                    sleep(BASE_TIME)
                    with timer("3.1 grandchild task"):
                        sleep(BASE_TIME)
                        with timer("3.1.1 grand-grandchild task"):
                            sleep(BASE_TIME)
                    with timer("3.2 grandchild task"):
                        sleep(BASE_TIME)
