class Parent1:
    def __init__(self, *args, **kwargs):
        print(f"Parent1")


class Parent2:
    def __init__(self, *args, **kwargs):
        print(f"Parent2")


class Parent3:
    def __init__(self, *args, **kwargs):
        print(f"Parent3")


class MyClass(Parent1, Parent2, Parent3):
    def __init__(self, *args, **kwargs):
        print(f"MyClass")
        super().__init__(*args, **kwargs)
        super(Parent1, self).__init__(*args, **kwargs)
        super(Parent2, self).__init__(*args, **kwargs)


m = MyClass()
