#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    dictt = {1: 'A', 2: 'B', 3: 'C', 4: 'D'}
    dict_items ={v: k for k, v in dictt.items()}

    print(dict_items)
