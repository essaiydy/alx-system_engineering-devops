#!/usr/bin/python3
'''extend your Python script to export data in the CSV format'''

from json import dump
import requests
import sys

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/todos?userId=' + sys.argv[1]
    usinfo = 'https://jsonplaceholder.typicode.com/users/' + sys.argv[1]

    todo_respo = requests.get(url).json()
    name_respo = requests.get(usinfo).json()
    NAME = name_respo.get("username")
    dicct = {}
    lis = []

    for task in todo_respo:
        lis.append({"task": task["title"], "completed": task["completed"],
                  "username": NAME})

    with open("{}.json".format(sys.argv[1]), "w") as f:
        dump({sys.argv[1]: lis}, f)
