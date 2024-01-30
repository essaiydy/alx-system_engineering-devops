#!/usr/bin/python3
''' Python script that, using this REST API, for a given employee ID'''

import requests
import sys
import csv

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/todos?userId=' + sys.argv[1]
    usinfo = 'https://jsonplaceholder.typicode.com/users/' + sys.argv[1]

    todo_respo = requests.get(url).json()
    name_respo = requests.get(usinfo).json()
    NAME = name_respo.get("name")

    data = []
    for respo in todo_respo:
        data.append([sys.argv[1], NAME, respo["completed"], respo["title"]])

    with open('{}.csv'.format(sys.argv[1]), mode='w', newline='') as f:
        writer = csv.writer(f, quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
        writer.writerows(data[1:])
