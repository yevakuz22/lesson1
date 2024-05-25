class Vehicle:
    def __init__(self, make, model, mileage):
        self.make = make
        self.model = model
        self.mileage = mileage

    def display_info(self):
        print("Make: {self.make}, Model: {self.model}, Mileage: {self.mileage} miles");

    def drive(self, miles):
        self.mileage += miles

    def maintenance_needed(self):
        return self.mileage > 100000

    def reset_mileage(self):
        self.mileage = 0
        print(0)




class Chess:

    def __init__(color, position):

class Pawn(Chess):
    def move(new_position):
        print("{color} Pawn moves to {new_position}")

class Rook(Chess):
    def move(new_position):
        print("{color} Rook moves to {new_position}")

class Knight(Chess):
    def move(new_position):
        print("{color} Knight moves to {new_position}")

class Bishop(Chess):
    def move(new_position):
        print("{color} Bishop moves to {new_position}")

class Queen(Chess):
    def move(new_position):
        print("{color} Queen moves to {new_position}")

class King(Chess):
    def move(new_position):
        print("{color} King moves to {new_position}")
























