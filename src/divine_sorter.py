import csv
import json


def book_sorter():
    with open("../base_data/users.json") as users:
        loader = users.read()
        users_data = json.loads(loader)

    users_list = []
    for i in users_data:
        users_list.append({"name": i["name"], "gender": i["gender"], "age": i["age"], "address": i["address"]})

    with open("../base_data/books.csv") as books:
        reader = csv.reader(books)
        books_data = next(reader)
        books_list = []
        for j in reader:
            books_list.append(dict(zip(books_data, j)))

    users_with_books_list = []
    for x in users_list:
        users_with_books_list.append(
            {
                "name": x["name"],
                "gender": x["gender"],
                "age": x["age"],
                "address": x["address"],
                "books": []
            }
        )

    users_count = len(users_with_books_list)
    total_count = 0
    for y in books_list:
        users_with_books_list[total_count]["books"].append(
            {
                "title": y["Title"],
                "author": y["Author"],
                "pages": int(y["Pages"]),
                "genre": y["Genre"]
            }
        )
        total_count += 1
        if total_count >= users_count:
            total_count = 0

    with open("result.json", "w") as result_json:
        users_with_books_data = json.dumps(users_with_books_list, indent=4)
        result_json.write(users_with_books_data)


book_sorter()
