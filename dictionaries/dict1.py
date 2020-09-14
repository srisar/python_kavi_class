# dictionary

book1 = {
    "title": "the lord of the ring: fellowship of the ring",
    "author": "j.r.r tolkin",
    "price": 29.9
}

# book2 = book1
book2 = book1.copy()

book2["title"] = "1984"
book2["author"] = "george orwell"
book2["price"] = 9.69

print(book2)
print(book1)

# print(book)
# print(book["title"])
# print(book["author"])
# print(book["price"])
#
# book_title = book["title"]
#
# print(book_title)
#
# book["price"] = 19.9
# print(book)
#
# book["pages"] = 785
#
# print(book)

# for item in book:
#     print(f"{item} => {book[item]}")

# print(book.values())
# print(book.keys())
# print(book.items())

# if "pages" in book:
#     print("pages is available")

# print(len(book))
#
# book.pop("price")
# print(book)
