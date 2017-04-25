def resolve_dots_in_path(path_arg):
    cwd_parts = os.getcwd().split(os.sep)
    path_arg_parts = path_arg.split(os.sep)
    temp = list()
    for part_ in path_arg_parts:
        if '.py' not in part_:
            if part_ != os.curdir:
                temp.append(part_)
    path_arg_parts = temp.copy()
    temp = list()
    for part_ in path_arg_parts:
        if part_ == os.pardir:
            cwd_parts.pop()
        else:
            temp.append(part_)
    # path_arg = os.sep.join(temp)
    cwd_parts.extend(temp)
    path_ = os.sep.join(cwd_parts)
    print("resolve_dots_in_path().path_:", path_)
    return path_


def is_path_abs(path_arg):
    sep_char = {'/', '\\'}
    a = path_arg == os.sep  # if os.sep, then at root of *nix system
    b = path_arg[0] == os.sep  # if first character is os.sep, then abs path of *nix os.
    c = path_arg[1] == ':'  # for when coding on windows- root is C:\, for example.
    path_is_abs = a or b or c
    return path_is_abs


def path_win2nix(path_win):
    """
    Accepts a windows path as arg and returns its unix-style path.
    :param (str) path_win:
    :return: (str)
    """
    temp = path_win.split(os.sep)
    temp.reverse()
    nix_add = ['', 'mnt', temp[-1][0].lower()]
    nix_add.reverse()
    temp.pop()
    temp.extend(nix_add)
    temp.reverse()
    file_nix = os.path.sep.join(temp)
    # print('>'*100, 'file_nix:', file_nix)
    return file_nix


def path_nix2win(path_nix):
    """
    Converts a unix style path into a windows-style path.
    :param (str) path_nix:
    :return: (str)
    """
    path_is_abs = is_path_abs(path_nix)
    temp = path_nix.split(os.sep)
    if path_is_abs is False:
        if './' in path_nix:
            print("WARNING: PATH uses . and .. Verify converted PATH. Accomodations might be necessary.")
    elif path_is_abs is True:
        if path_nix[1] == 'mnt':
            drive_ = ''.join([path_nix[2], ':'])
            temp[0] = drive_
    else:
        print("ERROR in unix to windows path conversion in path_nix2win()")
    path_win = '\\'.join(temp)
    return path_win
    # drive_letters = tuple(chr(num) for num in list(range(67, 91)))
    # temp = path_nix.split(os.sep)
    # for path_part_ in temp[0:5]:
    #     for drive_letter_ in drive_letters:
    #         if path_part_ == drive_letter_
    
    # print('>'*100, 'file_nix:', file_nix)
    return file_nix


if __name__ == '__main__':
    import os
    paths = ['D:/libraries/kc/Dropbox/workspace/tic/kc/tic_modules',
            'workspace/tic/kc/tic_modules',
            '../workspace/tic/kc/tic_modules',
            './workspace/tic/kc/tic_modules',
            '/workspace/tic/kc/tic_modules',
             "D:\\libraries\\kc\\Dropbox\\workspace\\tic\\kc\\tic_modules\\test_paths_from_sh.txt"
            ]
    print(os.getcwd())
    for path_ in paths:
        print(os.path.abspath(path_), '\t', path_)
    for path_ in paths:
        print(os.path.isabs(path_))
    for path_ in paths:
        print(os.path.normpath(path_))
    