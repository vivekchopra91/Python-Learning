class Electronicdevices:
    motherboard = 1
    circuit = 5
    def elect_details(self):
        return f"The electronic devices have {self.circuit} circuits & {self.motherboard} motherboard."

class Pocketgadget(Electronicdevices):
    GPS = 1
    circuit = 8
    time = "yes"
    def pocket_device(self):
        return f"The pocket-gadgets have {self.circuit} circuits, {self.motherboard} motherboard, {self.GPS} GPS-enabled and can also share time {self.time}"

class Smartphone(Pocketgadget):
    screentouch = 1
    circuit = 9
    GPU = 1
    CPU = 1
    def smart_device(self):
        return f"The smart-phone has {self.screentouch} screentouch ability\
            , {self.circuit} circuits with inbuild {self.GPU} GPU & {self.CPU} CPU "


TV = Electronicdevices()
ipod = Pocketgadget()
apple = Smartphone()

print(apple.circuit)
print(apple.motherboard)
print(apple.pocket_device())
print(ipod.elect_details())
# print(TV.smart_device())          # will be error, since multilevel follows chronological order.