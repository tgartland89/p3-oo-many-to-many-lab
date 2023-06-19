class Author:

    all = []

    def __init__(self, name):
        self.name = name
        Author.all.append(self)
# module 2 Test Author class initializes with name . 

    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]
# module 8 Test Author class has method contracts() that returns a list of its contracts . 

    def books(self):
        return [contract.book for contract in self.contracts()]
# module 9 Test Author class has method books() that returns a list of its books .

    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)
# module 12 Test Author class has method sign_contract() that creates a contract for an author and book . 
    
    def total_royalties(self):
        return sum([contract.royalties for contract in self.contracts()])
# module 13 Test Author class has method total_royalties that gets the sum of all its related contracts' royalties . 

class Book:

    all = []

    def __init__(self, title):
        self.title = title
        Book.all.append(self)
# module 1 Test Book class initializes with title .  
    
    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]
# module 10 Test Book class has method contracts() that returns a list of its contracts . 
    def authors(self):
        return [contract.author for contract in self.contracts()]
# module 11 Test Book class has method authors() that returns a list of its authors . 

class Contract:

    all = []

    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)
# module 3 Test Contract class initializes with author, book, date, royalties .  

    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise Exception
        self._author = value

# module 4 Test Contract class validates author of type Author . 

    @property
    def book(self):
        return self._book
    
    @book.setter
    def book(self, value):
        if not isinstance(value, Book):
            raise Exception
        self._book = value
# module 5 Test Contract class validates book of type Book .  

    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self, value):
        if not isinstance(value, str):
            raise Exception
        self._date = value
# module 6 Test Contract class validates date of type str . 

    @property
    def royalties(self):
        return self._royalties
    
    @royalties.setter
    def royalties(self, value):
        if not isinstance(value, int):
            raise Exception
        self._royalties = value
# module 7 Test Contract class validates royalties of type int .

    @classmethod
    def contracts_by_date(cls):
        return sorted(cls.all, key=lambda c: c.date)
# module 14 Test Contract class has method contracts_by_date() that sorts all contracts by date .
