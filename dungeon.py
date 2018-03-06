import numpy as np
import random
import time
import copy
from PIL import Image
from rooms import Room, roomLists

class Dungeon:
    """
    Contains the notion of a dungeon. Map is a 9x9 array that holds
    instances of rooms. Build dungeon starts at the center room
    in the array and recursively branches out.
    """
    def __init__(self):
        self.map = np.zeros((9, 9), dtype=Room)
        self.map[4][4] = roomLists[4][random.randint(0,3)]

    def build_dungeon(self, x, y):
        self.display_dungeon()
        time.sleep(.2)
        # if current room has only one door, we have reached a dead end
        if self.map[y][x].num_doors == 1:
            # print('base case')
            return
        else:
            doors = self.map[y][x].doors
            # loop through the doors of the current room
            for i in range(0, len(doors)):
                # if there is a door
                # print(doors[i])
                if doors[i]:
                    # print("there's a door")
                    # if the door is on the left and there is not
                    # already a door on that side
                    if i == 0 and self.map[y][x - 1] == 0:  
                        self.place_room(x - 1, y)
                        self.build_dungeon(x - 1, y)
                    # if the door is on the right and there is not
                    # already a door on that side
                    elif i == 1 and self.map[y - 1][x] == 0:
                        self.place_room(x, y - 1)
                        self.build_dungeon(x, y - 1)
                    # if the door is on the bottom and there is not
                    # already a door on that side
                    elif i == 2 and self.map[y][x + 1] == 0:
                        self.place_room(x + 1, y)
                        self.build_dungeon(x + 1, y)
                    # if the door is on the bottom and there is not
                    # already a door on that side
                    elif i == 3 and self.map[y + 1][x] == 0:
                        self.place_room(x, y + 1)
                        self.build_dungeon(x, y + 1)
                # else:
                    # print("no door")
            # once you've checked all your doors, return
            return

    def get_room(self, doors, num):
        if (num == 1):
            new_room = copy.deepcopy(roomLists[1][random.randint(0,4)])
            while new_room.doors != doors:
                new_room = new_room.rotate()
            # print(doors)
            # new_room.display()
            return new_room
        
        if (num == 2):
            if(doors[0] == doors[2] or doors[1] == doors[3]):
                new_room = copy.deepcopy(roomLists[2][random.randint(0,3)])
                while new_room.doors != doors:
                    new_room = new_room.rotate()
                # print(doors)
                # new_room.display()
                return new_room
            else:
                new_room = copy.deepcopy(roomLists[0][random.randint(0,3)])
                while new_room.doors != doors:
                    new_room = new_room.rotate()
                # print(doors)
                # new_room.display()
                return new_room

        if (num == 3):
            new_room = copy.deepcopy(roomLists[3][random.randint(0,5)])
            while new_room.doors != doors:
                new_room = new_room.rotate()
            # print(doors)
            # new_room.display()
            return new_room

        if (num == 4):
            new_room = copy.deepcopy(roomLists[4][random.randint(0,3)])
            while new_room.doors != doors:
                new_room = new_room.rotate()
            # print(doors)
            # new_room.display()
            return new_room

    def place_room(self, x, y):
        """
        Takes in new room coordinates and checks surrounding spaces in
        the array for rooms. if there is a room then it checks if it
        need to match the door of the room if not it randomly picks if
        it has a door.
        """
        new_doors = [0, 0, 0, 0]
        if x > 0:
            if self.map[y][x-1] != 0:
                if self.map[y][x-1].doors[2] == 1:
                    new_doors[0] = 1
                else:
                    new_doors[0] = random.randint(0, 1)
            else:
                new_doors[0] = random.randint(0, 1)

        if y < 8:
            if self.map[y+1][x] != 0:
                if self.map[y+1][x].doors[1] == 1:
                    new_doors[3] = 1
                else:
                    new_doors[3] = random.randint(0, 1)
            else:
                new_doors[3] = random.randint(0, 1)

        if x < 8:
            if self.map[y][x + 1] != 0:
                if self.map[y][x + 1].doors[0] == 1:
                    new_doors[2] = 1
                else:
                    new_doors[2] = random.randint(0, 1)
            else:
                new_doors[2] = random.randint(0, 1)

        if y > 0:
            if self.map[y - 1][x] != 0:
                if self.map[y - 1][x].doors[3] == 1:
                    new_doors[1] = 1
                else:
                    new_doors[1] = random.randint(0, 1)
            else:
                new_doors[1] = random.randint(0, 1)

        
        num_doors = sum(new_doors)
        new_room = self.get_room(new_doors, num_doors)
        self.map[y][x] = new_room

    def display_dungeon(self):
        horizontal_imgs = list()
        imgs_comb = None
        for i in range(0, len(self.map)):
            imgs = list()            
            for j in range(len(self.map[0])):
                if self.map[i][j] != 0:
                    imgs.append(self.map[i][j].image)
                else:
                    imgs.append(np.zeros((100,100)))
            imgs_comb = np.hstack(imgs)
            horizontal_imgs.append(imgs_comb)

        imgs_comb = np.vstack(horizontal_imgs)
        imgs_comb = Image.fromarray(imgs_comb)
        if imgs_comb.mode != 'RGB':
            imgs_comb = imgs_comb.convert('RGB') 

        imgs_comb.save('./assets/dungeon.png')
       

if __name__ == '__main__':
    dungeon = Dungeon()
    dungeon.display_dungeon()
