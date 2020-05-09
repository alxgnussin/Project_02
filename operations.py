# -*- coding: utf-8 -*-
# Python 3.7.7 required

import json
import os.path
from random import randint


def is_exist(file):
    return os.path.exists(file)


def get_json_data(file):
    with open(file, 'r', encoding='utf8') as f:
        my_object = json.loads(f.read())
    return my_object


def append_json_data(file, record):
    if is_exist(file):
        exist_data = get_json_data(file)
        exist_data.append(record)
        content = json.dumps(exist_data)
        with open(file, 'w', encoding='utf8') as f:
            f.write(content)
    else:
        content = json.dumps([record])
        with open(file, 'w', encoding='utf8') as f:
            f.write(content)


def goals():
    return get_json_data('goals.json')


def teachers():
    return get_json_data('teachers.json')


def select_profile(key, id):
    return next(dic for dic in teachers() if dic[key] == id)


def select_goals(my_goals):
    teacher_goals = []
    for i in my_goals:
        teacher_goals.append(goals()[i])
    return teacher_goals


def schedule(data):
    timetable = {}
    for key, value in data.items():
        times = []
        for time, flag in value.items():
            if flag:
                times.append(time)
        dic = {key: {'name': week_days()[key], 'times': times}}
        timetable.update(dic)
    return timetable


def random_generator():
    keys = []
    while len(keys) < 6:
        key = randint(0, len(teachers()) - 1)
        if key in keys:
            continue
        else:
            keys.append(key)
    return keys


def week_days():
    dic = {'mon': 'Понедельник', 'tue': 'Вторник', 'wed': 'Среда', 'thu': 'Четверг', 'fri': 'Пятница',
           'sat': 'Суббота', 'sun': 'Воскресение'}
    return dic


def week_time():
    dic = {"time1": "1-2", "time2": "3-5", "time3": "5-7", "time4": "7-10"}
    return dic