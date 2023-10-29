class Car:
    def __init__(self,make,model,year,speed):
        self.make=make
        self.model=model
        self.year=year
        self.speed=speed

    def accelerate(self,paraspeed):
        self.speed+=paraspeed
        print("the car is now going ",self.speed," km/h")

    def brake(self,paraspeed):
        self.speed-=paraspeed
        print("the car is now going ", self.speed, " km/h")

var=Car("eurokid4","CarLite XR", 2069, 0)
var.accelerate(50)
