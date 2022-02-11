# Написать функцию для подсчета количества рабочих дней между двумя датами (даты передаются в качестве параметров).
import datetime as _datetime


first_date = _datetime.date(2022, 2, 7)
second_date = _datetime.date(2022, 2, 28)


def work_time(d_start, d_end):
    work_days = frozenset({0, 1, 2, 3, 4})
    out_work_days = 0
    while d_start <= d_end:
        if d_start.weekday() in work_days:
            out_work_days += 1
        d_start += _datetime.timedelta(days=1)
    return out_work_days


print(f"There are {work_time(first_date, second_date)} work days between {first_date} and {second_date}.")
