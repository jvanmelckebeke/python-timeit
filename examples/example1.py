from timeitpoj.timeit import TimeIt
from time import sleep

if __name__ == '__main__':
    BASE_TIME = 0.1

    with TimeIt("my timer") as timer:
        print("Executing my timer....")
        sleep(BASE_TIME)

        with timer("my subtimer"):
            print("Executing my subtimer....")
            sleep(BASE_TIME)

            with timer("my nested subtimer"):
                print("Executing my nested subtimer....")
                sleep(BASE_TIME)

                for _ in range(2):
                    with timer("my super nested subtimer 2"):
                        sleep(BASE_TIME)

            for _ in range(5):
                with timer("my nested subtimer 2"):
                    sleep(BASE_TIME)

        with timer("my subtimer 992"):
            print("Executing my subtimer 2....")
            sleep(BASE_TIME)

        with timer("my subtimer 4"):
            print("Executing my subtimer 4....")
            sleep(BASE_TIME)

        # Something that is not covered by the timer
        sleep(BASE_TIME * 2)
