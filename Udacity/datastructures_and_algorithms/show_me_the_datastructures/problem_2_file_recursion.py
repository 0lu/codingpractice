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
    if not suffix:
        return

    result = []
    find_files_helper(suffix, path, result)
    return result


def find_files_helper(suffix, path, result):
    if not os.path.isdir(path):
        if path.endswith(suffix):
            result.append(path)
            return

    current_path_files = os.listdir(path)
    folders = [os.path.join(path, file) for file in current_path_files if os.path.isdir(os.path.join(path, file))]
    files = [os.path.join(path, file) for file in current_path_files if os.path.isfile(os.path.join(path, file))]

    if folders:
        for folder in folders:
            find_files_helper(suffix, folder, result)

    if files:
        for file in files:
            if file.endswith(suffix):
                result.append(file)


print(find_files(".c", "testdir"))
#['testdir/subdir3/subsubdir1/b.c', 'testdir/subdir5/a.c', 'testdir/subdir1/a.c', 'testdir/t1.c']

print(find_files("", "testdir"))
#None

print(find_files(" ", "testdir"))
#[]

print(find_files("dslfjdsflsdjfwfipwjfwlkjfsdaklfjasfkdsjafiosdfjlsdkafjsdkfa ", "testdir"))
#[]

print(find_files(".h", "testdir"))
#['testdir/subdir3/subsubdir1/b.h', 'testdir/subdir5/a.h', 'testdir/subdir1/a.h', 'testdir/t1.h']

path = "./solution/problem2/problem2.py"
suffix = ".py"
print(find_files(suffix, path))