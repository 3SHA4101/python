class Car:
    def display_info(self):
        print(f"Car:brand= {self.brand},model= {self.model}")
my_car=Car()

b=input("enter brand=")
m=input("enter model=")
my_car.brand = b
my_car.model = m
my_car.display_info()
