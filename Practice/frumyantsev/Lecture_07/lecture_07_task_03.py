import pickle
import random


FN = ['Jack', 'John', 'Mary', 'Jane', 'James', 'Jill']
LN = ['Smith', 'Brooks', 'Tailor', 'Black', 'Jones']
ADRS = ['1 Main St, Apt 5', '330 First St.', '21250 Gagarin Ave']
CTZN = ['RU', 'US', 'FR', 'CA', 'UK', 'CN']
ID = ['passport', 'ID Card', 'birth certificate', 'driving license']


class Human:
    def __init__(self):
        self._first_name = random.choice(FN)
        self._last_name = random.choice(LN)
        self._address = random.choice(ADRS)
        self._age = random.randint(0, 100)
        self._citizenship = random.choice(CTZN)
        self._id = random.choice(ID)

    def __str__(self):
        return f"{self._first_name} {self._last_name} {self._age} yo, citizen of {self._citizenship} " \
               f"residing at {self._address}, {self._id}"


def serialize_humans(count, file='human.data'):
    with open(file, 'wb') as fl:
        for inst in range(count):
            inst = Human()
            pickle.dump(inst, fl, protocol=pickle.HIGHEST_PROTOCOL)


def deserialize_humans(file):
    with open(file, 'rb') as fl:
        lst = []
        while 1:
            try:
                lst.append(pickle.load(fl))
            except EOFError:
                break
    for i in lst:
        print(f"{i} - {type(i)=}")
    return lst


if __name__ == "__main__":
    serialize_humans(4)
    deserialize_humans('human.data')
