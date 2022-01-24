class Parent1:
    def __init__(self, *args, **kwargs):
        print(f"Parent1")
        super().__init__(*args, **kwargs)


class Child1(Parent1):
    def __init__(self, *args, **kwargs):
        print(f"Child1")
        super().__init__(*args, **kwargs)


class Parent2:
    def __init__(self, *args, **kwargs):
        print(f"Parent2")
        super().__init__(*args, **kwargs)


class Child2(Parent2):
    def __init__(self, *args, **kwargs):
        print(f"Child2")
        super().__init__(*args, **kwargs)


class MyClass(Child1, Child2):
    def __init__(self, *args, **kwargs):
        print(f"MyClass")
        super().__init__(*args, **kwargs)
        super(Parent1, self).__init__(*args, **kwargs)


m = MyClass()
