#!/usr/bin/python3
''' Python script that, using this REST API, for a given employee ID'''

import requests
import sys

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/todos/' + sys.argv[1]
    usinfo = 'https://jsonplaceholder.typicode.com/users/' + sys.argv[1]

    try:
	todo_respo = requests.get(url).json()
	name_respo = requests.get(usinfo).json()

	name = name_respo.get("name")
	
	nub_todo = len(todo_respo)

	j = 0

	for i in todo_respo:
	    if i["userId"] == sys.argv[1] && i["completed"]:
		j++

	print("Employee {} is done with tasks {}/{}".format(name, j, nub_todo))

	for title in todo_respo:
	    if title["completed"]:
		print("\t {}".format(todo_respo.get("title")))

    except requests.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.RequestException as req_err:
        print(f"Request error occurred: {req_err}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
