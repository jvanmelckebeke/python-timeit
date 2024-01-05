import logging
import unittest
from time import sleep

from timeitpoj import TimeIt
from timeitpoj.timer.internal_timer import InternalTimer

BASE_TIME = 0.1


class IntegrationTests(unittest.TestCase):
    def setup_logger(self, name="timeitpoj", level=logging.INFO):
        logger = logging.getLogger(name)
        logger.setLevel(level)

        format = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(level)
        stream_handler.setFormatter(format)

        logger.addHandler(stream_handler)

        return logger

    def test_simple_timer(self):
        logger = self.setup_logger("simple timer")
        ti = TimeIt("simple timer", log_func=logger.info)
        with ti as timer:
            sleep(BASE_TIME)
        self.assertAlmostEqual(BASE_TIME, ti.elapsed_time, places=1)

    def test_single_nested_timer(self):
        logger = self.setup_logger("nested timer")
        ti = TimeIt("nested timer", log_func=logger.info)
        with ti as timer:
            sleep(BASE_TIME)
            with timer("task"):
                sleep(BASE_TIME)

        self.assertAlmostEqual(2 * BASE_TIME, ti.elapsed_time, places=1)

    def test_complex_nested_timer(self):
        logger = self.setup_logger("complex nested timer")
        ti = TimeIt("complex nested timer", log_func=logger.info)
        with ti as timer:
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

        self.assertAlmostEqual(8 * BASE_TIME, ti.elapsed_time, places=1)
