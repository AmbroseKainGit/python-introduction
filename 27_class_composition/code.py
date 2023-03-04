class BookShelf:
    def __init__(self, *books) -> None:
        self.books = books

    def __str__(self) -> str:
        return f"BookShelf with {len(self.books)} books."


class Book:
    def __init__(self, name) -> None:
        self.name = name

    def __str__(self) -> str:
        return f"Book {self.name}"


book = Book("Harry Potter")
book2 = Book("Harry Potter 2")
shelf = BookShelf(book, book2)
print(shelf)
