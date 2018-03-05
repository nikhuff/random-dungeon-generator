import pygame as py
import numpy as np
import cv2
import matplotlib.pylab as plt


class Room:
    def __init__(self, doors, image):#image stuff here

        self.doors = doors
        self.numDoors = doors.count(1)
        self.roomImage = image


oneDPic = plt.imread('1_door_room.png')
oneDPicTwo = plt.imread('1_door_room2.png')
oneDPicThree = plt.imread('1_door_room3.png')
oneDPicFour = plt.imread('1_door_room4.png')
oneDPicFive = plt.imread('1_door_room5.png')


# straight
twoDPic = plt.imread('2_door_hall.png')
twoDPicFour = plt.imread('2_door_hall4.png')
twoDPicSix = plt.imread('2_door_room2.png')
twoDPicSeven = plt.imread('2_door_room3.png')


# angled
twoDPicTwo = plt.imread('2_door_hall2.png')
twoDPicThree = plt.imread('2_door_hall3.png')
twoDPicFive = plt.imread('2_door_room.png')
twoDPicEight = plt.imread('2_door_room4.png')


threeDPic = plt.imread('3_door_hall.png')
threeDPicTwo = plt.imread('3_door_hall2.png')
threeDPicThree = plt.imread('3_door_room.png')
threeDPicFour = plt.imread('3_door_room2.png')
threeDPicFive = plt.imread('3_door_room3.png')
threeDPicSix = plt.imread('3_door_room4.png')


fourDPic = plt.imread('4_door_hall.png')
fourDPicTwo = plt.imread('4_door_room.png')
fourDPicThree = plt.imread('4_door_room2.png')
fourDPicFour = plt.imread('4_door_room3.png')

oneDoor = Room([1, 0, 0, 0], oneDPic)
oneDoorTwo = Room([1, 0, 0, 0],oneDPicTwo)
oneDoorThree = Room([1, 0, 0, 0],oneDPicThree)
oneDoorFour = Room([1, 0, 0, 0],oneDPicFour)
oneDoorFive = Room([1, 0, 0, 0],oneDPicFive)

oneDoorRooms =[oneDoor, oneDoorTwo, oneDoorThree, oneDoorFour, oneDoorFive]

# straight
twoDoor = Room([1, 0, 1, 0],twoDPic)
twoDoorFour = Room([1, 0, 1, 0],twoDPicFour)
twoDoorSix = Room([1, 0, 1, 0],twoDPicSix)
twoDoorSeven = Room([1, 0, 1, 0],twoDPicSeven)

twoDoorRoomsS = [twoDoor, twoDoorFour, twoDoorSix, twoDoorSeven]

# angled
twoDoorTwo = Room([1, 1, 0, 0],twoDPicTwo)
twoDoorThree = Room([1, 0, 0, 1],twoDPicThree)
twoDoorFive = Room([1, 0, 0, 1],twoDPicFive)
twoDoorEight = Room([1, 0, 0, 1],twoDPicEight)

twoDoorRoomsA = [twoDoorTwo, twoDoorThree, twoDoorFive, twoDoorEight]

threeDoor = Room([1, 0, 1, 1],threeDPic)
threeDoorTwo = Room([1, 0, 1, 1],threeDPicTwo)
threeDoorThree = Room([1, 0, 1, 1],threeDPicThree)
threeDoorFour = Room([1, 0, 1, 1],threeDPicFour)
threeDoorFive = Room([1, 0, 1, 1],threeDPicFive)
threeDoorSix = Room([1, 0, 1, 1],threeDPicSix)

threeDoorRooms = [threeDoor, threeDoorTwo, threeDoorThree, threeDoorFour, threeDoorFive, threeDoorSix]

fourDoor = Room([1, 1, 1, 1],fourDPic)
fourDoorTwo = Room([1, 1, 1, 1],fourDPicTwo)
fourDoorThree = Room([1, 1, 1, 1],fourDPicThree)
fourDoorFour = Room([1, 1, 1, 1],fourDPicFour)

fourDoorRooms = [fourDoor, fourDoorTwo, fourDoorThree, fourDoorFour]

