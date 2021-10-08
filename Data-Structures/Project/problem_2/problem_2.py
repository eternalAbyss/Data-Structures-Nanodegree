import os


def file_explorer(path, file_list=[]):
    for each in os.listdir(path):
        inner_path = os.path.join(path, each)
        if os.path.isdir(inner_path):
            return file_explorer(inner_path)
        else:
            if each[-2:] == ".c":
                file_list.append(inner_path)
            return
    return file_list


print(file_explorer('./testdir'))
