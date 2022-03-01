# Написать клиентское и серверное приложения. Клиент отправляет на сервер список зашифрованных слов,
# сервер дешифрует слова по словарю и возвращает клиенту список расшифрованных слов.
# Клиент должен вывести полученный список.
# Client
import socket
import pickle
from Lec10_1_1 import coding, gen_dict


def encoding_dictionary(offset=1):
    abc = "abcdefghijklmnopqrstuvwxyz"
    encoding_dict = {}
    for letter in abc:
        encoding_dict[letter] = abc[offset % 26]
        offset += 1
    return encoding_dict


# def coding(in_dict, in_str):
#     out_str = []
#     tmp = ""
#     for word in in_str:
#         for letter in word:
#             tmp += in_dict.get(letter)
#         out_str.append(tmp)
#         tmp = ""
#     return out_str


secret_list = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 49160
s.connect((host, port))
cripto_key = pickle.loads(s.recv(1024))
encoding_dict = gen_dict(cripto_key, False)
print("Sending data")
data = coding(encoding_dict, secret_list)
print(data)
s.send(pickle.dumps(data))
print("Response from server")
print(pickle.loads(s.recv(1024)))
s.close()

