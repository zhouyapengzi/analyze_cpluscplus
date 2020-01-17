import os
valid_extensions = ['.cc', '.cpp', '.h', '.hpp']

# two ways to get all files under one directory
# the first method using recursive
# the second method using os.walk


def find_all_files(path, recursive=True):
    """
    Return a list of all the files in the folder.
    If recursive is True, the function will search recursively.
    """
    files = []
    for entry in os.scandir(path):
        if entry.is_dir() and recursive:
            files += find_all_files(entry.path)
        elif get_extension(entry.path) in valid_extensions:
            files.append(entry.path)
    return files


def find_all_proto_files(path):
    proto_files = []
    for root, directories, files in os.walk(path):
        for file in files:
            if file.endswith('.proto'):
                file_path = os.path.join(root, file)
                proto_files.append(file_path)
    print("Total proto files: %s" % len(proto_files))
    return proto_files
