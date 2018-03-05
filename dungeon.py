


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
    in the array and recursively branches out.
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

    def get_room(self, doors, num):

        if (num == 1):
            returnRoomNum = random.randint(oneDoorRooms.length())
            return(oneDoorRooms[returnRoomNum])

        if (num == 2):
            if(doors[0] == doors[2] or doors[1] == doors[3]):
                returnRoomNum = random.randint(twoDoorRoomsS.length())
                return (twoDoorRoomsS[returnRoomNum])
            else:
                returnRoomNum = random.randint(twoDoorRoomsA.length())
                return (twoDoorRoomsA[returnRoomNum])

        if (num == 3):
            returnRoomNum = random.randint(threeDoorRooms.length())
            return (threeDoorRooms[returnRoomNum])

        if (num == 4):
            returnRoomNum = random.randint(fourDoorRooms.length())
            return (fourDoorRooms[returnRoomNum])

    def place_room(self, x, y):
        """
        Takes in new room coordinates and checks surrounding spaces in
        the array for rooms. if there is a room then it checks if it
        need to match the door of the room if not it randomly picks if
        it has a door.
        """

        new_doors = [0, 0, 0, 0]
        if self.map[x-1, y] is not None:
            if self.map[x-1, y].doors[2] == 1:
                new_doors[0] = 1
        else:
            new_doors[0] = random.randint(0, 2)

        if self.map[x, y+1] is not None:
            if self.map[x, y+1].doors[3] == 1:
                new_doors[1] = 1
        else:
            new_doors[1] = random.randint(0, 2)

        if self.map[x + 1, y] is not None:
            if self.map[x + 1, y].doors[0] == 1:
                new_doors[2] = 1
        else:
            new_doors[2] = random.randint(0, 2)

        if self.map[x, y - 1] is not None:
            if self.map[x, y - 1].doors[1] == 1:
                new_doors[3] = 1
        else:
            new_doors[0] = random.randint(0, 2)

        if x == 0:
            new_doors[0] = 0
        if y == 9:
            new_doors[1] = 0
        if x == 9:
            new_doors[2] = 0
        if y == 0:
            new_doors[3] = 0
        num_doors = sum(new_doors)
        new_room = self.create_room(new_doors, num_doors)
        return new_room

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