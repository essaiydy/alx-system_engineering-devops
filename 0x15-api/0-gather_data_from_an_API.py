#!/usr/bin/python3
''' Python script that, using this REST API, for a given employee ID'''

import requests
import sys

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/todos/' + sys.argv[1]
    usinfo = 'https://jsonplaceholder.typicode.com/users/' + sys.argv[1]

    todo_respo = requests.get(url).json()
    name_respo = requests.get(usinfo).json()

    name = name_respo.get("name")

    num_todo = len(todo_respo)

    j = 0

    for task in todo_respo:
        if task["completed"]:
            j += 1
    print("Employee {} is done with tasks {}/{}".format(name, j, num_todo))

    for task in todo_respo:
        if task["completed"]:
            print("\t {}".format(task["title"]))
