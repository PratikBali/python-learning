class BookStore():
    totalBooks = 0

    def __init__(self, bookName, authorName):
        self.book = bookName
        self.author = authorName
        BookStore.totalBooks += 1

    def Display(self):
        print('{} by {} and Total books {}'.format(self.book, self.author, BookStore.totalBooks))

obj1 = BookStore('Linux System Programming', 'Robert Love')
obj1.Display()
obj2 = BookStore('C Programming', 'Dennis Ritchie')
obj2.Display()
obj3 = BookStore('Chhavaa', 'Shivaji Savant')
obj3.Display()

