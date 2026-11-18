from abc import ABC, abstractmethod

from day_19.Library_Management.models import Book, Member


class BookRepository(ABC):

    @abstractmethod
    def load(self):
        pass

    @abstractmethod
    def save(self):
        pass

    @abstractmethod
    def add(self,book:Book):
        pass

class FileBasedBookRepository(BookRepository):




    def __init__(self, file_path):
        self.file_path = file_path
        self.books = {}

    #load books from the text file
    def load(self):

        try:
            with open(self.file_path,"r") as file :

                for line_number, line in enumerate(file, start=1):

                    line = line.strip()

                    if not line:
                        continue

                    data = line.split("|")

                    if len(data) != 5 :
                        raise ValueError(f"Invalid book record at line {line_number}")

                    book = Book(book_id=data[0],
                                title=data[1],
                                author=data[2],
                                year=data[3],
                                book_lend_member_id =
                                None if data[4] == "None" else data[4]
                                )

                    self.books[book.book_id] = book

        except FileNotFoundError:
            self.books = {}

    def save(self):

        with open(self.file_path, "w") as file :

            for book in self.books.values():

                line = (
                    f"{book.book_id}|"
                    f"{book.title}|"
                    f"{book.author}|"
                    f"{book.year}|"
                    f"{book.book_lend_member_id}\n"

                )

                file.write(line)

    #add a new book
    def add(self, book: Book):

        if book.book_id in self.books:
            raise ValueError("Book ID already exists.")

        self.books[book.book_id] = book

        self.save()

    #Find a book using its ID
    def get_by_id(self,book_id):
        return self.books.get(book_id)

    def get_all_books(self):
        return list(self.books.values())

    #Update an existing book
    def update(self,book):

        if book.book_id not in self.books:
            raise ValueError('Book not found')

        self.books[book.book_id] = book

        self.save()


class FileBasedMemberRepository :

    def __init__(self, file_path):

        self.file_path = file_path
        self.members = {}

    def load(self):
        self.members = {}

        try:
            with open(self.file_path, "r")  as file:

                for line_number, line in enumerate(file, start=1):
                    line = line.strip()

                    if not line:
                        continue

                    data = line.split("|")

                    if len(data) != 3:
                        raise ValueError(f"Invalid member record at line {line_number}")

                    member = Member(member_id=data[0], name=data[1],contact=data[2])

                    self.members[member.member_id] = member

        except FileNotFoundError :
            self.members = {}

    def save(self):

        with open(self.file_path, "w") as file :
            for


















