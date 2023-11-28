#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    school = {'1a': 26, '1b': 27, '2b': 30, '6a': 30, '7v': 28}
    school['1a'] = 30
    school['3g'] = 27
    del school['7v']

    sum_of_students = sum(school.values())

    print(school)
    print(f'Общее количество обучающихся в школе: {sum_of_students}')
