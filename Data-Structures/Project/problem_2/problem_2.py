import os


def find_files(path, files=[]):
    for each in os.listdir(path):
        inner_path = os.path.join(path, each)
        if os.path.isdir(inner_path):
            find_files(inner_path, files)
        else:
            if each.endswith('.c'):
                files.append(inner_path)
    return files


basepath = './testdir'
output = find_files(basepath)
for each in output:
    print(each)
