# Создать класс Human с 5-10 атрибутами (имя, фамилия, возраст, меcто жительства и т.д.).
# Написать функцию, которая создавала бы указанное количество экземпляров, сериализовывала их и сохраняла в файл human.data,
# и другую функцию, которая бы читала файл human.data, десериализовывала его содержимое и выводила результат на печать.
# Примечание: чтоб у экземпляров Human были разные значения атрибутов, можно воспользоваться функциями random.randint()
# и random.choice().
import pickle as _pickle
import random as _random


class Setup:
    FILE_NAME = "human.data"


class Human:
    def __init__(self, name, family_name, patronymic, age, nationality, leaving_place, working_phone="", occupation=""):
        self._name = name
        self._family_name = family_name
        self._patronymic = patronymic
        self._age = age
        self._nationality = nationality
        self._leaving_place = leaving_place
        self._working_phone = working_phone
        self._occupation = occupation

    def __str__(self):
        out_str = f"Name: {self._name}, family name: {self._family_name}, patronymic: {self._patronymic}, " \
                  f"age: {self._age}, nationality: {self._nationality}, leaving_place: {self._leaving_place}, " \
                  f"working_phone: {self._working_phone}, occupation: {self._occupation}"
        return out_str


def word_generator(num):
    s1 = "аеиоуэюя"
    s2 = "бвгджзклмнпрстфхчшщ"
    res = ""
    s = s2
    while len(res) < num:
        res += _random.choice(s)
        s = s1 if s == s2 else s2
    return res


def phone_generator(num):
    res = "+7"
    while len(res) < num + 1:
        res += str(_random.randint(0, 9))
    return res


def human_generator(count):
    city = ["Москва", "Нижний Новгород", "Санкт Петербург"]
    work = ["Повар", "Слесарь", "Механик", "Программист"]
    national = ["Грек", "Индиец", "Румын", "Русский"]
    with open(Setup.FILE_NAME, "wb") as f:
        while count != 0:
            name = word_generator(_random.randint(4, 6))
            family_name = word_generator(_random.randint(4, 8))
            patronymic = word_generator(_random.randint(4, 7))
            age = _random.randint(18, 60)
            nationality = national[_random.randint(0, 3)]
            leaving_place = city[_random.randint(0, 2)]
            working_phone = phone_generator(9)
            occupation = work[_random.randint(0, 3)]
            human = Human(name, family_name, patronymic, age, nationality, leaving_place, working_phone, occupation)
            count -= 1
            _pickle.dump(human, f, protocol=_pickle.HIGHEST_PROTOCOL)


def human_extractor(count):
    out_list = []
    with open(Setup.FILE_NAME, "rb") as f:
        while count != 0:
            out_list.append(_pickle.load(f))
            count -= 1
        return out_list


human_generator(7)
for h in human_extractor(7):
    print(h)
