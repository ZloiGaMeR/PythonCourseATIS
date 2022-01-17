# 1.
# Написать функцию-фабрику танков.
# Принимает {тип: количество танков}: {T34: 5, Tiger: 10}
# Возвращает отсортированный по мощи (power) список танков.

# 2.
# + принимает значения скорости (speed), мощи (power) и начальной координаты (x).
# + Устанавливает переданные значения для всех танков.
import sys
sys.path.append(r'C:\Users\Stmadm\Documents\PythonCourseForATIS\PythonCourseATIS\Useful\for_lec5')
import tanks


def fabric(d):
    t_common = []
    for k, v in d.items():
        t_common += [k() for _ in range(v)]
        # t_local = []
        # i = 0
        # while i < v:
        #     t_local.append(k())
        #     i += 1
        # t_common += t_local
    #t_common.sort()
    return sorted(t_common)


lst = fabric({tanks.Tiger: 10, tanks.T34: 5})
print(lst)