from abc import ABC, abstractmethod
from datetime import datetime

from day_19.Library_Management.models import Book, Member, Loan


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
            for member in self.members.values():

                line = f"{member.member_id}|{member.name}|{member.contact}"

                file.write(line)

    def add(self,member):

        if member.member_id in self.members:
            raise ValueError("Member ID already exists.")

        self.members[member.member_id] = member

        self.save()

    def get_by_id(self,member_id):
        return self.members.get(member_id)


    def get_all(self):
        return list(self.members.values())


    def update_member(self,member):

        if member.member_id not in self.members:
            raise ValueError("Member not found.")

        self.members[member.member_id] = member

        self.save()


class LoanRepository:

    def __init__(self, file_path):
        self.file_path = file_path
        self.loans = {}

    def load(self):

        self.loans = {}

        try:

            with open(self.file_path, "r") as file :

                for line_number, line in enumerate(file,start=1):
                    line = line.strip()

                    if not line:
                        continue

                    data = line.split("|")

                    if len(data) != 5:
                        raise ValueError(f"Invalid loan record at line {line_number}")

                    loan = Loan(loan_id=data[0],
                                member_id=data[1],
                                book_id=data[2],
                                borrowed_at=datetime.strptime(data[3],"%Y-%m-%d %H:%M:%S"),
                                returned_at=
                                None if data[4] == "None" else
                                datetime.strptime(data[4],"%Y-%m-%d %H:%M:%S"))

                    self.loans[loan.loan_id] = loan

        except FileNotFoundError:
            self.loans = {}


    def save(self):

        with open(self.file_path, "w") as file :

            for loan in self.loans.values():

                line = (f"{loan.loan_id}|{loan.member_id}|{loan.book_id}|"
                        f"{loan.borrowed_at.isoformat()}|"
                        f"{loan.returned_at.isoformat() if loan.returned_at is not None 
                        else "None"}\n")

                file.write(line)

    def add(self,loan):

        if loan.loan_id in self.loans:
            raise ValueError("Loan ID already exists")

        self.loans[loan.loan_id] = loan

        self.save()

    def get_by_id(self,loan_id):
        return self.loans.get(loan_id)

    def get_all(self):
        return list(self.loans.values())

    def update(self,loan):

        if loan.loan_id not in self.loans:
            raise ValueError("Loan not found")

        self.loans[loan.loan_id] = loan

        self.save()

    def get_only_active_loans(self):
        return [loan for loan in self.loans.values if loan.is_active()]




















