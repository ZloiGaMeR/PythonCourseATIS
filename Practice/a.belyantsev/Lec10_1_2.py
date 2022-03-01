# Написать клиентское и серверное приложения. Клиент отправляет на сервер список зашифрованных слов,
# сервер дешифрует слова по словарю и возвращает клиенту список расшифрованных слов.
# Клиент должен вывести полученный список.
# Client
import socket
import pickle
from Lec10_1_1 import coding, gen_dict


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

