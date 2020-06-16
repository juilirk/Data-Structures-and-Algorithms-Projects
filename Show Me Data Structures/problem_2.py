import os


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """

    if suffix == None:
        return []
    if len(os.listdir(path)) == 0:
        return []

    paths = os.listdir(path)
    files = []
    for f in paths:
        if f.endswith("."+suffix):
            files.append(f)
        elif os.path.isdir(path+'/'+f):
            files.extend(find_files(suffix=suffix, path=path+'/'+f))

    return files

    # %% Testing official
# Testing preparation
path_base = os.getcwd() + '/testdir'

# Normal Cases:
print(find_files(suffix='c', path=path_base))
# [a.c', 'b.c', 'a.c', 't1.c']

print(find_files(suffix='h', path=path_base))
# ['a.h', 'b.h', 'a.h', 't1.h']

print(find_files(suffix='z', path=path_base))
# []

# Edge Cases:
print(find_files(suffix='', path=path_base))
# []
