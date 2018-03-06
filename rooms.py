import cv2
import numpy as np

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
        self.image = image


    def rotate(self):
        self.doors = [self.doors[-1]] + self.doors[:-1]
        self.image = np.rot90(self.image, -1)
        return self
    
    # used for debugging
    def display(self):
        print(self.doors)
        print(self.num_doors)

oneDPic = cv2.imread('./assets/1_door_room.png', 0)
oneDPicTwo = cv2.imread('./assets/1_door_room2.png', 0)
oneDPicThree = cv2.imread('./assets/1_door_room3.png', 0)
oneDPicFour = cv2.imread('./assets/1_door_room4.png', 0)
oneDPicFive = cv2.imread('./assets/1_door_room5.png', 0)

# straight
twoDPic = cv2.imread('./assets/2_door_hall.png', 0)
twoDPicFour = cv2.imread('./assets/2_door_hall4.png', 0)
twoDPicSix = cv2.imread('./assets/2_door_room2.png', 0)
twoDPicSeven = cv2.imread('./assets/2_door_room3.png', 0)

# angled
twoDPicTwo = cv2.imread('./assets/2_door_hall2.png', 0)
twoDPicThree = cv2.imread('./assets/2_door_hall3.png', 0)
twoDPicFive = cv2.imread('./assets/2_door_room.png', 0)
twoDPicEight = cv2.imread('./assets/2_door_room4.png', 0)

threeDPic = cv2.imread('./assets/3_door_hall.png', 0)
threeDPicTwo = cv2.imread('./assets/3_door_hall2.png', 0)
threeDPicThree = cv2.imread('./assets/3_door_room.png', 0)
threeDPicFour = cv2.imread('./assets/3_door_room2.png', 0)
threeDPicFive = cv2.imread('./assets/3_door_room3.png', 0)
threeDPicSix = cv2.imread('./assets/3_door_room4.png', 0)

fourDPic = cv2.imread('./assets/4_door_hall.png', 0)
fourDPicTwo = cv2.imread('./assets/4_door_room.png', 0)
fourDPicThree = cv2.imread('./assets/4_door_room2.png', 0)
fourDPicFour = cv2.imread('./assets/4_door_room3.png', 0)

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
