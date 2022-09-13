#!/usr/bin/python3
""" Queries REST API for all employee info, exports to JSON
"""
if __name__ == "__main__":
    import json
    import requests as r

    user_q = r.get("https://jsonplaceholder.typicode.com/users")
    user_data = user_q.json()
    json_data = {}

    for user in user_data:
        username = user.get("username")
        user_id = str(user.get("id"))
        url = "https://jsonplaceholder.typicode.com/todos?userId=" + user_id
        task_q = r.get(url)
        task_data = task_q.json()


        json_dict = {}
        json_list = []

        for elem in task_data:
            json_dict["task"] = elem.get("title")
            json_dict["completed"] = elem.get("completed")
            json_dict["username"] = username
            json_list.append(json_dict)
            json_dict = {}

        json_data[user_id] = json_list

    with open("todo_all_employees.json", 'w') as jsonfile:
        json.dump(json_data, jsonfile)

