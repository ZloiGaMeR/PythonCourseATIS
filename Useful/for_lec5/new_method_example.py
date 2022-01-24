class Employee:
    cnt = 0

    def __new__(cls, *args, **kwargs):
        cls.cnt += 1
        return super().__new__(cls, *args, **kwargs)



e1 = Employee()
e2 = Employee()
print(Employee.cnt)