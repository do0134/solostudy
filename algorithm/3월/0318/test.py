import os
import time

def dfs_search_directory(path, file_count, max_files=1000):
    if file_count[0] >= max_files:
        return
    try:
        for entry in os.listdir(path):
            full_path = os.path.join(path, entry)
            if os.path.isfile(full_path):
                file_count[0] += 1
                if file_count[0] >= max_files:
                    return

            elif os.path.isdir(full_path):
                dfs_search_directory(full_path, file_count, max_files)
    except PermissionError:
        pass

if __name__ == "__main__":
    directory = "/"
    max_files_to_find = 1000
    count = [0]
    start_time = time.time()
    dfs_search_directory(directory, count, max_files_to_find)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(count)
    print(f"Elapsed time: {elapsed_time} seconds")