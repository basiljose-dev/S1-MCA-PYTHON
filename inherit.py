class publisher:
    def __init__(self, name):
             self. name = name

class book(publisher):
    def __init__(self, name, title, author):
	    super(). __init__(name)
	    self. title = title
	    self. author = author

class python(book):
    def __init__(self, name, title, author, price, no_of_page):
	    super(). __init__(name, title, author)
	    self. price = price
	    self. no_of_page = no_of_page

    def display(self):
	    print(self.name)
	    print(self.title)
	    print(self.author)
	    print(self.price)
	    print(self.no_of_page)

p1 = python("anu", "GOD", "john", 2000, 600)
p1.display()

