from random import randint, choice
import pickle


name_list = ["Peter", "John", "Travis", "Bob", "Alex", "Rachel", "Michael", "Sindy", "Jerald", "Sheldon"]
surname_list = ["Cooper", "Butler", "McAlester", "Rostenkowsky", "Kutrapaly", "Dexter", "Richi", "Tores"]
fname_list = ["Sergeevich", "Popovich", "Alekseevich", "Vyacheslavovich", "Aleksandrovich", "Vladimirovich"]
car_list = ["Tesla", "Volvo", "VW", "Audi", "Kia", "Nissan", "Renault", "Lada", "Chevrolet", "Suzuki", "Honda"]
people_lst = []


class Human:
    def __init__(self, name, surname, fname, age, postal, car):
        self.name = name
        self.surname = surname
        self.fname = fname
        self.age = age
        self.postal = postal
        self.car = car


def create(num):
    with open("human.data", "wb") as f:
        for i in range(num):

            name = choice(name_list)
            surname = choice(surname_list)
            fname = choice(fname_list)
            age = randint(18, 65)
            postal = '603' + str(randint(100, 200))
            car = choice(car_list)

            people_lst.append(Human(name, surname, fname, age, postal, car))
            pickle.dump(people_lst[i].__dict__, f)


def read():
    # тут не смог реализовать следующее решение
    # res = pickle.load(f)
    # return res
    # считывало только первую строку
    unsrl = []
    with open("human.data", "rb") as f:
        for _ in people_lst:
            unsrl.append(pickle.load(f))
    return unsrl


create(5)
print(read())
