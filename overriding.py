class vehicle:
    def start(self):
        print("Vehicle starting")
class car(vehicle):
    def start(self):
        print("Car starting")
v=vehicle()
v.start()
c=car()
c.start()