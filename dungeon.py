import random
import numpy as np
from PIL import Image


class Room:
    """
    Contains the notion of a room. Doors is an array representing the
    door on that room as follows: [left, top, right, bottom]. 1 denotes
    a door while 0 denotes no door. Image is a numpy array holding the
    image of the room.
    """
    def __init__(self, doors):
        self.doors = doors
        self.num_doors = doors.count(1)
        self.image = np.zeros((100, 100))

    def rotate(self):
        # rotate the doors and image 90 degrees
        self.doors = self.doors[-1] + self.doors[:-1]
        np.rot90(self.image, -1)
    
    # used for debugging
    def display(self):
        print(self.doors)
        print(self.num_doors)

class Dungeon:
    """
    Contains the notion of a dungeon. Map is a 9x9 array that holds
    instances of rooms. Build dungeon starts at the center room
    in the array and recursively brances out.
    """
    def __init__(self):
        self.map = np.zeros((9, 9), dtype=Room)
        self.map[4][4] = Room([1] * 4)

    def build_dungeon(self, x, y):
        # if current room has only one door, we have reached a dead end
        if self.map[x][y].num_doors == 1:
            return
        else:
            doors = self.map[x][y].doors
            # loop through the doors of the current room
            for i in range(doors):
                # if there is a door
                if doors[i]:
                    # if the door is on the left and there is not
                    # already a door on that side
                    if i == 0 and self.map[x - 1][y] is int:  
                        self.place_room(x - 1, y)
                        self.build_dungeon(x - 1, y)
                    # if the door is on the right and there is not
                    # already a door on that side
                    elif i == 1 and self.map[x][y + 1] is int:
                        self.place_room(x, y + 1)
                        self.build_dungeon(x, y + 1)
                    # if the door is on the bottom and there is not
                    # already a door on that side
                    elif i == 2 and self.map[x + 1][y] is int:
                        self.place_room(x + 1, y)
                        self.build_dungeon(x + 1, y)
                    # if the door is on the bottom and there is not
                    # already a door on that side
                    elif i == 3 and self.map[x][y + 1] is int:
                        self.place_room(x, y + 1)
                        self.build_dungeon(x, y + 1)
            # once you've checked all your doors, return
            return

    def place_room(self, x, y):
        pass

    def create_room(self, room):
        pass

    def rotate(self, room):
        pass

    def display_dungeon(self):
        horizontal_imgs = list()
        imgs_comb = None
        for i in range(0, len(self.map[0])):
            imgs = self.map[i]
            imgs_comb = np.hstack(imgs)
            horizontal_imgs.append(imgs_comb)

        imgs_comb = np.vstack(horizontal_imgs)
        imgs_comb = Image.fromarray(imgs_comb)

        imgs_comb.save('./assets/dungeon.png')
       

if __name__ == '__main__':
    dungeon = Dungeon()
    dungeon.map[4][4].display()