def fun(a, b):
    print(a + b)

#==================

expected = 10
actual = None

def mock_fun(x):
    global actual
    actual = x


class CtxManager:
    def __enter__(self):
        global print
        self.backup = print
        print = mock_fun
    def __exit__(self, exc_type, exc_val, exc_tb):
        global print
        print = self.backup
        print(f"{exc_type=}{exc_val=}{exc_tb=}")


with CtxManager():
    fun(5, 2)
    raise Exception("Some exception")

print(actual == expected)