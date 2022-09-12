#!/usr/bin/python3
''' api fetch '''
import requests
import sys


if __name__ == "__main__":
    userNameRequest = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(
            sys.argv[1]
        )
    )
    userName = userNameRequest.json()["name"]
    response = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}/todos".format(
            sys.argv[1]
        )
    )
    json = response.json()

    i = 0
    todoList = []
    did = 0
    total = 0

    for idx in json:
        if idx["completed"]:
            todoList.append(idx["title"])
            did += 1
        total += 1

    print(f"Employee {userName} is done with tasks({did}/{total}):")

    for idx in todoList:
        print("\t " + idx)
