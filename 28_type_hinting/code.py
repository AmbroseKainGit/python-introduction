from typing import List


def list_avg(seq: List) -> float:
    return sum(seq) / len(seq)


list_avg(123)


class Book:
    TYPES = ("hardcover", "paperback")

    def __init__(self, name: str, book_type: str, weight: int) -> None:
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self) -> str:
        return f"<Book {self.name}, {self.book_type}, weighing {self.weight}g>"

    @classmethod
    def hardcover(cls, name, page_weight) -> "Book":
        return cls(name, cls.TYPES[0], page_weight + 100)

    @classmethod
    def paperback(cls, name, page_weight) -> "Book":
        return cls(name, cls.TYPES[1], page_weight + 100)
