#!/usr/bin/python3
""" Queries REST API for employee info, exports to CSV
"""
if __name__ == "__main__":
    import csv
    import requests as r
    from sys import argv

    user_id = argv[1]
    name_q = r.get("https://jsonplaceholder.typicode.com/users/{}/"
                   .format(user_id))
    data = name_q.json()
    username = data.get("username")

    url = "https://jsonplaceholder.typicode.com/users/1/todos/"
    task_q = r.get(url, params={'userId': user_id})
    data = task_q.json()


    with open('{}.csv'.format(user_id), 'w', newline='') as csvfile:
        csv_data = csv.writer(csvfile, delimiter=',', quotechar='"',
                              quoting=csv.QUOTE_ALL)
        for elem in data:
            csv_data.writerow([elem["userId"], username,
                               elem["completed"], elem["title"]])

