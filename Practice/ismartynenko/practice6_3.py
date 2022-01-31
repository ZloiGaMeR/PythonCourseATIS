from time import time, sleep


class TestManager:
    def __enter__(self):
        self.__start_time = time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__end_time = time()
        print(f"Time execute is {self.__end_time - self.__start_time} sec.")


with TestManager():
    sleep(1)
