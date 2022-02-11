import os
import datetime as dt

pth = '.\\TempFolder1'


if __name__ == '__main__':
    while 1:
        for file_tup in os.walk(pth):
            for file in file_tup[2]:
                if dt.datetime.timestamp(dt.datetime.now()) - \
                        os.path.getctime(os.path.join(str(file_tup[0]), str(file))) > 60:
                    os.remove(os.path.join(str(file_tup[0]), str(file)))
        # for file_tup in os.walk(pth):
            for dire in file_tup[1]:
                # print(dire)
                if dt.datetime.timestamp(dt.datetime.now()) - \
                        os.path.getctime(os.path.join(str(file_tup[0]), str(dire))) > 120:
                    try:
                        os.rmdir(os.path.join(str(file_tup[0]), str(dire)))
                    except PermissionError as ex:
                        print(f"The folder \"{dire}\" contains file created earlier than 60 seconds ago. "
                              f"Waiting for file expiration...")
                        continue
                    except OSError:
                        print(f"The folder \"{dire}\" yet contains other folder. Waiting for inner folder removal...")
                        continue
