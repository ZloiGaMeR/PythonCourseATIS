import os.path
import time


def monitoring(source):
    # Save original state
    orig_dirs = []
    orig_files = []
    for i in os.walk(source):
        for j in i[1]:
            orig_dirs.append(os.path.join(i[0], j))
        for j in i[2]:
            orig_files.append(os.path.join(i[0], j))

    # Monitoring
    LIFE_TIME_DIR = 120
    LIFE_TIME_FILE = 60
    rm_dirs = {}
    rm_files = {}
    while True:
        print("=========================================================================")
        for i in os.walk(source):
            for j in i[1]:
                # Path for new folders
                rmdir_path = os.path.join(i[0], j)
                if rmdir_path not in orig_dirs:
                    # Removal time for new folders
                    rm_time_d = os.path.getctime(rmdir_path) + LIFE_TIME_DIR
                    # dictionary {rm_dirs[rm_time_d]: path}
                    rm_dirs[rm_time_d] = rmdir_path
                    print(f"Directory {rmdir_path} will be remove at:   {time.ctime(rm_time_d)}")
            for j in i[2]:
                # Path for new files
                rmfile_path = os.path.join(i[0], j)
                if rmfile_path not in orig_files:
                    # removal time for new files
                    rm_time_f = os.path.getctime(rmfile_path) + LIFE_TIME_FILE
                    # dictionary {rm_files[rm_time_f]: path}
                    rm_files[rm_time_f] = rmfile_path
                    print(f"File {rmfile_path} will be removed at:  {time.ctime(rm_time_f)}")
        print("=========================================================================")

        time.sleep(refresh_time)

        # Delete files
        rm_files_cp = rm_files.copy()
        for i in rm_files_cp.keys():
            if i <= time.time():
                os.remove(rm_files.get(i))
                print(f"File {os.path.basename(rm_files.pop(i))} was removed")

        # Delete folders
        rm_dirs_cp = rm_dirs.copy()
        for i in rm_dirs_cp.keys():
            if i <= time.time():
                try:
                    os.rmdir(rm_dirs.get(i))
                except OSError:
                    print(f"Folder {rm_dirs.get(i)} is not empty.")
                    print(f"Increase life time for folder on {LIFE_TIME_DIR}sec.")
                    rm_dirs[i+LIFE_TIME_DIR] = rm_dirs.pop(i)
                else:
                    print(F"Directory {os.path.basename(rm_dirs.pop(i))} was removed")


# Scan frequency
refresh_time = 15
monitoring(r"C:\Users\dfyz\Desktop\ismartynenko")
