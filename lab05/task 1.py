class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    def get_info(self):
        return 'Название книги {}, Автор: {}, Год издания: {}'.format(self.title, self.author, self.year)

death_soul = Book('Мертвые души','Н.В. Гоголь', '1835')
    
print(death_soul.get_info())