class Car:
    color = ""
    cartype = ""
    price = 0.0
    brand = ""

    def acc(self):
        print("Incresing Car Speed.")
    def brake(self):
        print("Stoping the car")
    def display(self):
        print("Brand Name :" , self.brand)
        print("Color      :" , self.color)
        print("Type       :" , self.cartype)
        print("Price      :" , self.price)


obj = Car()

obj.color = "Red"
obj.price = 2345678
obj.cartype = "Sedan"
obj.brand = "Audi"

obj1 = Car()

obj1.color = "White"
obj1.price = 123000
obj1.cartype = "Sedan"
obj1.brand = "Range Rower"


obj.display()


obj1.display()
