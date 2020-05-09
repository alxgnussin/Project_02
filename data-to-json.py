# -*- coding: utf-8 -*-
# Python 3.7.7 required

import json

from data import goals, teachers

with open('goals.json', 'w', encoding='utf8') as f:
    f.write(json.dumps(goals))

with open('teachers.json', 'w', encoding='utf8') as f:
    f.write(json.dumps(teachers))