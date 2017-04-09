#!/usr/bin/env python
from __future__ import print_function
import codecs
from sys import argv

scr, list_a, list_b = argv


def get_str_keys(lines):
    filer_list = filter(lambda x: '=' in x, lines)
    res = map(lambda x: x.split('=')[0].strip(), filer_list)
    return res


def get_lines_from_file(file):
    with codecs.open(file, 'r', encoding='utf16') as f:
        txt = f.readlines()
        return txt


strs = map(get_lines_from_file, [list_a, list_b])
(k_a, k_b) = map(get_str_keys, strs)
gap = list(set(k_a) - set(k_b))

map(print, gap)
