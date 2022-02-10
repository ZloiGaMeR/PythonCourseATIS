import datetime as dt


def work_days(a, b):
    date1 = dt.datetime.strptime(a, "%d%m%Y")
    date2 = dt.datetime.strptime(b, "%d%m%Y")
    w_days = 0

    if a > b:
        date1, date2 = date2, date1

    for i in range((date2 - date1).days + 1):
        delta = date1 + dt.timedelta(days=i)
        if 1 <= delta.isoweekday() <= 5:
            w_days += 1

    return w_days


print("Working day's -", work_days('11032022', '17032022'))
