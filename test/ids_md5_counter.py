#!/usr/bin/python3
# coding: utf-8
import time
import hashlib
from collections import Counter

def compute_time(f):
    def wrapper(*args):
        start_time = time.time()
        ret = f(*args)
        timedelta = time.time() - start_time
        print('耗时（秒）',timedelta)

        return ret
    return wrapper


def md5(id):
    return hashlib.md5(id.encode()).hexdigest()

def clear_data():
    lines = []
    with open('md5s.txt', 'r') as f:
        for line in f:
            md5_id, type_str = line.split('\t')
            if type_str != '\n':
                lines.append((md5_id, type_str[:-1]))

    return lines


is_finded = False
ret = []


def async_find(datas, id_md5, md5_id):
    pass


def find_id(id_, md5_ids):
    id_md5 = md5(id_)
    for _id, type_ in md5_ids:
        if id_ == id_md5:

            break


def find_all_id():
    id_md5s = clear_data()

    with open('ids.txt', 'r') as f_:
        for id_ in f_:
            find_id(id_, id_md5s)

    return Counter(ret)


if __name__ == '__main__':
    print(dict(find_all_id()))
