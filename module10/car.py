class Car:
    def __init__(self, brand, color, max_speed, price):
        self.brand = brand
        self.color = color
        self.max_speed = max_speed
        self.price = price


    def car_look(self):
        description = ("car " + self.brand + " " +self.color + " color " + "and max speed (km/h): " + str(self.max_speed) + "  cost USD: " + str(self.price))
        print(description)


    def car_moving(self):
        print(f"car {self.brand} is started moving forward")

    def set_speed(self, speed):
        self.speed = speed
        print(f"Car {self.brand} set speed at {self.speed} km/h")

class Owner:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
    
    def info(self):
        return {"name": self.name,"age": self.age,"address": self.address}




class Truck(Car):
    def __init__(self, brand, color, max_speed, price, weight, owner):
        super().__init__(brand, color, max_speed, price)
        self.weight = weight
        self.load = 0
        self.owner = owner

    def who_is_owner(self):
        return Owner.info(self.owner)


    def take_load(self):
        self.load += 100

    def car_look(self):
            description = ("car " + self.brand + " " +self.color + " color " + "and max speed (km/h): " + str(self.max_speed) + "  cost USD: " + str(self.price) +
             " truck weight, kilos = " + str(self.weight) + " load = " + str(self.load) + ". Owner info: " + str (Owner.info(self.owner)))
            print(description)



owner = Owner("Onufriy", 37, "Iordanska str.17")

car1 = Car("Lada", "red", 160, 5000)
car1.car_look()
car2 = Car("Lanos", "white", 145, 4500)
car2.car_look()
car1.car_moving()
car1.set_speed(60)

car3 = Truck("Kamaz", "brown", 100, 16000, 4000, owner)
car3.car_look()
car3.take_load()
car3.car_look()
car3.set_speed(45)


        


    



