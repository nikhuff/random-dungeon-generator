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
        self.roomImage = image


    def rotate(self):
        self.doors = [self.doors[-1]] + self.doors[:-1]
        self.roomImage = np.rot90(self.roomImage, -1)
        return self
    
    # used for debugging
    def display(self):
        print(self.doors)
        print(self.num_doors)

oneDPic = cv2.imread('./assets/1_door_room.png')
oneDPicTwo = cv2.imread('./assets/1_door_room2.png')
oneDPicThree = cv2.imread('./assets/1_door_room3.png')
oneDPicFour = cv2.imread('./assets/1_door_room4.png')
oneDPicFive = cv2.imread('./assets/1_door_room5.png')

# straight
twoDPic = cv2.imread('./assets/2_door_hall.png')
twoDPicFour = cv2.imread('./assets/2_door_hall4.png')
twoDPicSix = cv2.imread('./assets/2_door_room2.png')
twoDPicSeven = cv2.imread('./assets/2_door_room3.png')

# angled
twoDPicTwo = cv2.imread('./assets/2_door_hall2.png')
twoDPicThree = cv2.imread('./assets/2_door_hall3.png')
twoDPicFive = cv2.imread('./assets/2_door_room.png')
twoDPicEight = cv2.imread('./assets/2_door_room4.png')

threeDPic = cv2.imread('./assets/3_door_hall.png')
threeDPicTwo = cv2.imread('./assets/3_door_hall2.png')
threeDPicThree = cv2.imread('./assets/3_door_room.png')
threeDPicFour = cv2.imread('./assets/3_door_room2.png')
threeDPicFive = cv2.imread('./assets/3_door_room3.png')
threeDPicSix = cv2.imread('./assets/3_door_room4.png')

fourDPic = cv2.imread('./assets/4_door_hall.png')
fourDPicTwo = cv2.imread('./assets/4_door_room.png')
fourDPicThree = cv2.imread('./assets/4_door_room2.png')
fourDPicFour = cv2.imread('./assets/4_door_room3.png')

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
