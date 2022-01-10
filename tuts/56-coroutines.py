def searcing():
    import time
    # A 5-sec time consuming task
    book = "This is a book on python programming."
    time.sleep(5)

    while True:
        text = (yield)
        if text in book:
            print("your text is in the book")
        else:
            print("text is not in the book")

search = searcing()
next(search)
search.send("python")
input("press any key :")
search.send("python prog")

search.close()