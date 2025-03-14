class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print(f"Car: {self.brand} {self.model}")

b=input("enter brand")
m=input("enter model")
my_car = Car(f"{b}, {a}")
my_car.display_info()
