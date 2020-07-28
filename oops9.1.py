# Multilevel Inheritance

class Electronic_Device ():
    __device2 = 4
    device_level = 1
    def listen_at_home (self) :
        return f"you can listen music at home {self.device_level} level"

class Pocket_Gadgets (Electronic_Device):
    device_level = 2
    def while_walking (self) :
        return f"you can listen music while walking {self.device_level} level"

class Mobile_Phone (Pocket_Gadgets):
    device_level = 3
    def can_do_Anything(self):
        return  f"You can do whatever you want anywhere {self.device_level} level"

tape_recorde = Electronic_Device()
walk_men = Pocket_Gadgets()
android = Mobile_Phone()

# print(Electronic_Device.device_level)
print(walk_men.listen_at_home())
print (android._Electronic_Device__device2)

