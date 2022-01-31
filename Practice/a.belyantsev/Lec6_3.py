# Напишите свой менеджер контекста, замеряющий и показывающий время исполнения кода внутри него
import time


class TimeCounting:

    def __enter__(self):
        print("Start timing")
        self._enter_time = time.time_ns()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._exit_time = time.time_ns() - self._enter_time
        print("Stop timing")
        print(f"Time of work: {self._exit_time} ns or {self._exit_time/1000000000} s.")


with TimeCounting():
    print("do something")
    time.sleep(3)
