class Property:
    def __init__(self, area, rooms, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

    def __str__(self):
        return f"Property:\nArea: {self.area} sq. meters\nRooms: {self.rooms}\nPrice: {self.price} dollars\nAddress: {self.address}"

class House(Property):
    def __init__(self, area, rooms, price, address, plot):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return f"{super().__str__()}\nHouse Specifics:\nPlot Size: {self.plot} sq. meters"

class Flat(Property):
    def __init__(self, area, rooms, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return f"{super().__str__()}\nFlat Specifics:\nFloor: {self.floor}"

if __name__ == '__main__':

    house = House(area=150, rooms=4, price=300000, address="123 Main St", plot=500)

    flat = Flat(area=80, rooms=2, price=150000, address="456 Second St", floor=3)

    print("House Information:")
    print(house)

    print("\nFlat Information:")
    print(flat)