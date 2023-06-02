from time import sleep

from timeit import TimeIt

if __name__ == '__main__':

    BASE_TIME = 0.1
    # random example script to test the timeit functionallity

    with TimeIt("my timer") as timer:
        print("executing my timer....")
        sleep(BASE_TIME)
        with timer("my subtimer"):
            print("executing my subtimer....")
            sleep(BASE_TIME)

            with timer("my nested subtimer"):
                print("executing my nested subtimer....")
                sleep(BASE_TIME)

                for _ in range(2):
                    with timer("my super nested subtimer 2"):
                        sleep(BASE_TIME)

            for _ in range(5):
                with timer("my nested subtimer 2"):
                    sleep(BASE_TIME)
        with timer("my subtimer 992"):
            print("executing my subtimer 2....")
            sleep(BASE_TIME)
            #
            #     with timer("my subtimer 3"):
            #         sleep(BASE_TIME)
            #
            # for _ in range(50):
            #     sleep(BASE_TIME)
            #     # uncovered time

        with timer("my subtimer 4"):
            print("executing my subtimer 4....")
            sleep(BASE_TIME)
        # something that is not covered by the timer
        sleep(BASE_TIME*2)
