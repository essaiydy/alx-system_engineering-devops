#!/usr/bin/python3
'''extend your Python script to export data in the CSV format'''

import csv
import requests
import sys

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/todos?userId=' + sys.argv[1]
    usinfo = 'https://jsonplaceholder.typicode.com/users/' + sys.argv[1]

    todo_respo = requests.get(url).json()
    name_respo = requests.get(usinfo).json()
    NAME = name_respo.get("username")
    data = []

    for respo in todo_respo:
        data.append([sys.argv[1], NAME, respo["completed"], respo["title"]])
    with open('{}.csv'.format(sys.argv[1]), 'w') as f:
        writer = csv.writer(f, quotechar='"', quoting=csv.QUOTE_ALL)
        writer.writerows(data)
