# Написать клиентское и серверное приложения. Клиент отправляет на сервер список зашифрованных слов,
# сервер дешифрует слова по словарю и возвращает клиенту список расшифрованных слов.
# Клиент должен вывести полученный список.
# Server
import socket
import pickle
import random
from Lec10_1 import gen_dict, coding


if __name__ == "__main__":
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '127.0.0.1'
    port = 49160
    s.bind((host, port))
    s.listen(2)
    cripto_key = 1
    while True:
        conn, addr = s.accept()
        print(f'Server got connection from {addr}')
        print(f'Send cripto key')
        cripto_key = random.randint(1, 10)
        conn.send(pickle.dumps(cripto_key))
        decoding_dict = gen_dict(cripto_key, True)
        print("Waiting data")
        data = coding(decoding_dict, pickle.loads(conn.recv(1024)))
        print("Send response to the client")
        conn.send(pickle.dumps(f"You send - {data}"))
        conn.close()
