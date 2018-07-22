#!/usr/bin/python
# -*- coding: utf-8 -*-

def get_suffix_file_dict_from_path(repo_root_path, suffix_dict, skip_hidden=True):
    file_list = []
    import os
    for fpathe,dirs,fs in os.walk(repo_root_path):
        for f in fs:
            if skip_hidden and "." in fpathe:
                continue
            child_abspath = os.path.join(fpathe,f)
            file_list.append(child_abspath)

    suffix_file_dict = dict()
    suffix_list = suffix_dict.keys()
    for fidx in xrange(len(file_list)):
        f = file_list[fidx]
        for sidx in xrange(len(suffix_list)):
            suffix = suffix_list[sidx]
            if f[-len(suffix):] == suffix:
                suffix_file_dict[f] = suffix_dict[suffix]
                break
    return suffix_file_dict

def get_license_content(license_path):
    import os
    if os.path.isfile(license_path):
        with open(license_path, "r") as license_handle:
            license_list = license_handle.readlines()
    else:
        print("[ERROR] license file not found: {}".format(license_path))
        exit(1)
    return license_list

def add_license_for_file(license_list, suffix_file_dict):
    print("[INFO] start add license ......")
    suffix_file_list = suffix_file_dict.keys()
    for fidx in xrange(len(suffix_file_list)):
        suffix_file = suffix_file_list[fidx]
        # different suffix, different license
        suffix_file_comment = suffix_file_dict[suffix_file]
        file_added_license_list = map(lambda line:\
                                             " ".join([suffix_file_comment, line]),\
                                      license_list)
        # read
        with open(suffix_file, "r") as handle:
            file_list = handle.readlines()
            file_added_license_list.extend(file_list)
        # write
        with open(suffix_file, "w") as handle:
            handle.writelines(file_added_license_list)
        print("[INFO] license added to {}".format(suffix_file))
    print("[INFO] license addition finished")
    print("[INFO] added file sum: {}".format(len(suffix_file_list)))

if __name__ == "__main__":
    # 0.init parameters
    repo_root_path = "/home/yuanshuai/code/inferx_model"
    license_path = "./LICENSE"
    # suffix name with it's comment string for one line
    suffix_dict = {".prototxt":"#", ".c":"//", ".h":"//", ".py":"#"}

    # 1.get all files needs to be added LICENSE
    suffix_file_path_dict = get_suffix_file_dict_from_path(repo_root_path,\
                                                           suffix_dict,\
                                                           skip_hidden=True)
    # 2.get LICENSE content
    license_list = get_license_content(license_path)

    # 3.add license
    add_license_for_file(license_list, suffix_file_path_dict)

