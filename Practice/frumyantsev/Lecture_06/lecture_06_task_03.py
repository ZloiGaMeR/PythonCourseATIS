import time


class CtxMgrTimeMeter:
    def __enter__(self):
        self._t = time.perf_counter()

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Time spent for inner code: {time.perf_counter() - self._t}")


if __name__ == "__main__":
    for i in range(8):
        dct = dict()
        with CtxMgrTimeMeter():
            dct[i] = []
            for j in range(10**i):
                dct[i].append(j * (1 / 2))
