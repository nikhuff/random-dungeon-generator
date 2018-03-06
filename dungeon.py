import numpy as np
import random
import cv2
from PIL import Image

class Room:
    """
    Contains the notion of a room. Doors is an array representing the
    door on that room as follows: [left, top, right, bottom]. 1 denotes
    a door while 0 denotes no door. Image is a numpy array holding the
    image of the room.
    """
    def __init__(self, doors, image):
        self.doors = doors
        self.num_doors = doors.count(1)
        self.roomImage = image


    def rotate(self):
        # rotate the doors and image 90 degrees
        self.doors = self.doors.append(self.doors.pop(0))
        np.rot90(self.roomImage)
    
    # used for debugging
    def display(self):
        print(self.doors)
        print(self.num_doors)

oneDPic = cv2.imread('1_door_room.png', 0)
oneDPicTwo = cv2.imread('1_door_room2.png')
oneDPicThree = cv2.imread('1_door_room3.png')
oneDPicFour = cv2.imread('1_door_room4.png')
oneDPicFive = cv2.imread('1_door_room5.png')

# straight
twoDPic = cv2.imread('2_door_hall.png')
twoDPicFour = cv2.imread('2_door_hall4.png')
twoDPicSix = cv2.imread('2_door_room2.png')
twoDPicSeven = cv2.imread('2_door_room3.png')

# angled
twoDPicTwo = cv2.imread('2_door_hall2.png')
twoDPicThree = cv2.imread('2_door_hall3.png')
twoDPicFive = cv2.imread('2_door_room.png')
twoDPicEight = cv2.imread('2_door_room4.png')

threeDPic = cv2.imread('3_door_hall.png')
threeDPicTwo = cv2.imread('3_door_hall2.png')
threeDPicThree = cv2.imread('3_door_room.png')
threeDPicFour = cv2.imread('3_door_room2.png')
threeDPicFive = cv2.imread('3_door_room3.png')
threeDPicSix = cv2.imread('3_door_room4.png')

fourDPic = cv2.imread('4_door_hall.png')
fourDPicTwo = cv2.imread('4_door_room.png')
fourDPicThree = cv2.imread('4_door_room2.png')
fourDPicFour = cv2.imread('4_door_room3.png')

oneDoor = Room([1, 0, 0, 0], oneDPic)
oneDoorTwo = Room([1, 0, 0, 0], oneDPicTwo)
oneDoorThree = Room([1, 0, 0, 0], oneDPicThree)
oneDoorFour = Room([1, 0, 0, 0], oneDPicFour)
oneDoorFive = Room([1, 0, 0, 0], oneDPicFive)

oneDoorRooms = [oneDoor, oneDoorTwo, oneDoorThree, oneDoorFour, oneDoorFive]

# straight
twoDoor = Room([1, 0, 1, 0], twoDPic)
twoDoorFour = Room([1, 0, 1, 0], twoDPicFour)
twoDoorSix = Room([1, 0, 1, 0], twoDPicSix)
twoDoorSeven = Room([1, 0, 1, 0], twoDPicSeven)

twoDoorRoomsS = [twoDoor, twoDoorFour, twoDoorSix, twoDoorSeven]

# angled
twoDoorTwo = Room([1, 1, 0, 0], twoDPicTwo)
twoDoorThree = Room([1, 0, 0, 1], twoDPicThree)
twoDoorFive = Room([1, 0, 0, 1], twoDPicFive)
twoDoorEight = Room([1, 0, 0, 1], twoDPicEight)

twoDoorRoomsA = [twoDoorTwo, twoDoorThree, twoDoorFive, twoDoorEight]

threeDoor = Room([1, 0, 1, 1], threeDPic)
threeDoorTwo = Room([1, 0, 1, 1], threeDPicTwo)
threeDoorThree = Room([1, 0, 1, 1], threeDPicThree)
threeDoorFour = Room([1, 0, 1, 1], threeDPicFour)
threeDoorFive = Room([1, 0, 1, 1], threeDPicFive)
threeDoorSix = Room([1, 0, 1, 1], threeDPicSix)

threeDoorRooms = [threeDoor, threeDoorTwo, threeDoorThree, threeDoorFour, threeDoorFive, threeDoorSix]

fourDoor = Room([1, 1, 1, 1], fourDPic)
fourDoorTwo = Room([1, 1, 1, 1], fourDPicTwo)
fourDoorThree = Room([1, 1, 1, 1], fourDPicThree)
fourDoorFour = Room([1, 1, 1, 1], fourDPicFour)

fourDoorRooms = [fourDoor, fourDoorTwo, fourDoorThree, fourDoorFour]

roomLists = [twoDoorRoomsA, oneDoorRooms, twoDoorRoomsS, threeDoorRooms, fourDoorRooms]

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
        print(self.map)
        # if current room has only one door, we have reached a dead end
        if self.map[x][y].num_doors == 1:
            print('base case')
            return
        else:
            doors = self.map[x][y].doors
            # loop through the doors of the current room
            for i in range(len(doors)):
                # if there is a door
                if doors[i]:
                    # if the door is on the left and there is not
                    # already a door on that side
                    if i == 0 and self.map[x - 1][y] == 0:  
                        self.place_room(x - 1, y)
                        self.build_dungeon(x - 1, y)
                    # if the door is on the right and there is not
                    # already a door on that side
                    elif i == 1 and self.map[x][y + 1] == 0:
                        self.place_room(x, y + 1)
                        self.build_dungeon(x, y + 1)
                    # if the door is on the bottom and there is not
                    # already a door on that side
                    elif i == 2 and self.map[x + 1][y] == 0:
                        self.place_room(x + 1, y)
                        self.build_dungeon(x + 1, y)
                    # if the door is on the bottom and there is not
                    # already a door on that side
                    elif i == 3 and self.map[x][y + 1] == 0:
                        self.place_room(x, y + 1)
                        self.build_dungeon(x, y + 1)
            # once you've checked all your doors, return
            return

    def get_room(self, doors, num):
        if (num == 1):
            new_room = roomLists[1][random.randint(0,3)]
            while new_room.doors != doors:
                new_room.rotate()
                print("test")
            return new_room
        
        if (num == 2):
            if(doors[0] == doors[2] or doors[1] == doors[3]):
                new_room = roomLists[2][random.randint(0,3)]
                while new_room.doors != doors:
                    new_room.rotate()
                return new_room
            else:
                new_room = roomLists[0][random.randint(0,3)]
                while new_room.doors != doors:
                    new_room.rotate()
                return new_room

        if (num == 3):
            new_room = roomLists[3][random.randint(0,5)]
            while new_room.doors != doors:
                new_room.rotate()
            return new_room

        if (num == 4):
            new_room = roomLists[4][random.randint(0,3)]
            while new_room.doors != doors:
                new_room.rotate()
            return new_room
        


        if (num == 3):
            new_room = random.randint(0,5)
            return (roomLists[3][new_room])

        if (num == 4):
            new_room = random.randint(0,3)
            return (roomLists[4][new_room])

    def place_room(self, x, y):
        """
        Takes in new room coordinates and checks surrounding spaces in
        the array for rooms. if there is a room then it checks if it
        need to match the door of the room if not it randomly picks if
        it has a door.
        """
        # if x == 0:
        #     new_doors[0] = 0
        # if y == 9:
        #     new_doors[1] = 0
        # if x == 9:
        #     new_doors[2] = 0
        # if y == 0:
        #     new_doors[3] = 0
        new_doors = [0, 0, 0, 0]
        if x > 0:
            if self.map[x-1][y] != 0:
                if self.map[x-1][y].doors[2] == 1:
                    new_doors[0] = 1
            else:
                new_doors[0] = random.randint(0, 1)

        if y < 8:
            if self.map[x, y+1] != 0:
                if self.map[x][y+1].doors[3] == 1:
                    new_doors[1] = 1
            else:
                new_doors[1] = random.randint(0, 1)

        if x < 8:
            if self.map[x + 1][y] != 0:
                if self.map[x + 1][y].doors[0] == 1:
                    new_doors[2] = 1
            else:
                new_doors[2] = random.randint(0, 1)

        if y > 0:
            if self.map[x][y - 1] != 0:
                if self.map[x][y - 1].doors[1] == 1:
                    new_doors[3] = 1
            else:
                new_doors[0] = random.randint(0, 1)

        
        num_doors = sum(new_doors)
        print('place room')
        new_room = self.get_room(new_doors, num_doors)
        self.map[x][y] = new_room

    def display_dungeon(self):
        horizontal_imgs = list()
        imgs_comb = None
        for i in range(0, len(self.map[0])):
            imgs = self.map[i]
            imgs_comb = np.hstack(imgs)
            horizontal_imgs.append(imgs_comb)

        imgs_comb = np.vstack(horizontal_imgs)
        print(imgs_comb)
        imgs_comb = Image.fromarray(imgs_comb)

        imgs_comb.save('./assets/dungeon.png')
       

if __name__ == '__main__':
    dungeon = Dungeon()
    dungeon.map[4][4].display()