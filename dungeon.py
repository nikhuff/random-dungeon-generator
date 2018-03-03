import random
import numpy as np

class Room:
    def __init__(self, doors):
        self.doors = doors
        self.num_doors = doors.count(1)
        self.image = np.zeros((100, 100))
    
    def display(self):
        print(self.doors)
        print(self.num_doors)

class Dungeon:
    def __init__(self):
        self.map = np.zeros((9, 9), dtype=Room)
        self.map[4][4] = Room([1] * 4)

    def build_dungeon(self, coordinates):
        pass

    def place_room(self, coordinates):
        pass

    def create_room(self, room):
        pass

    def rotate(self, room):
        pass

    def display_dungeon(self):
        pass
       

if __name__ == '__main__':
    dungeon = Dungeon()
    dungeon.map[4][4].display()