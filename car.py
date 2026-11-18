class driver:
    def __init__(self, name):
             self. name = name

class brand(driver):
    def __init__(self, name, brand):
	    super(). __init__(name)
	    self. brand = brand
	    

class car(brand):
    def __init__(self, name, brand, car, series):
	    super(). __init__(name, brand)
	    self. car = car
	    self. series = series
	    

    def display(self):
	    print(self.name)
	    print(self.brand)
	    print(self.car)
	    print(self.series)
	   

p1 = car("max verstapin", "redbull", "RB", 28)
p1.display()

