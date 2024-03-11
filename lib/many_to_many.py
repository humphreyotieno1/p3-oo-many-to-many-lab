class Author:
    all = []
    
    def __init__(self, name):
        self.name = name
        self.__class__.all.append(self)
        self.contracts_list = []
        
    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]

    def books(self):
        return [contract.book for contract in self.contracts()]
    
    @classmethod
    def all_contracts(cls):
        return cls.all
    
    def sign_contract(self, book, date, royalties):
        if not isinstance(book, Book):
            raise Exception("Invalid book object")
        contract = Contract(self, book, date, royalties)
        return contract
    
    def total_royalties(self):
        return sum(contract.royalties for contract in self.contracts())
    
class Book:
    all = []
    def __init__(self, title):
        self.title = title
        self.__class__.all.append(self)
        
    @classmethod
    def all_books(cls):
        return cls.all
    
    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]

    def authors(self):
        return [contract.author for contract in self.contracts()]

class Contract:
    all = []
    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("Author must be an instance of the Author class")
        if not isinstance(book, Book):
            raise Exception("Book must be an instance of the Book class")
        if not isinstance(date, str):
            raise TypeError("Date must be a string")
        if not isinstance(royalties, int):
            raise TypeError("Royalties must be an integer")
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        self.__class__.all.append(self)
        
        
    @classmethod
    def all_contracts(cls):
        return cls.all

        
    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all_contracts() if contract.date == date]
        