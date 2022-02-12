import datetime as dt


def business_days(date1, date2):
    d1 = dt.datetime.strptime(date1, '%Y-%m-%d')
    d2 = dt.datetime.strptime(date2, '%Y-%m-%d')
    bd = 0
    d = d1
    while d < d2:
        if d.weekday() < 5:
            # print(d.weekday())
            bd += 1
        d += dt.timedelta(days=1)
    print(f"{bd=}")


if __name__ == "__main__":
    print(f"Today is {dt.datetime.today()}")
    print(dt.datetime.weekday.__doc__)
    business_days('2021-02-09', '2022-02-10')
    business_days('2022-02-09', '2022-02-10')
    business_days('2022-01-09', '2022-02-10')
    business_days('2022-02-02', '2022-02-10')
    business_days('2022-02-09', '2021-02-10')
