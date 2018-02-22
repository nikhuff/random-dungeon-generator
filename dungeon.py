import random

class Room:
    def __init__(self):
        self.room_left = None
        self.room_top = None
        self.room_bottom = None
        self.room_right = None

    def add_left(self, room):
        self.room_left = room

    def add_top(self, room):
        self.room_top = room

    def add_right(self, room):
        self.room_right = room

    def add_bottom(self, room):
        self.room_bottom = room

class Dungeon:
    def __init(self, room):
        self.starting_room = Room()

    def build_dungeon(self, room):
        choice = random.randint(1, 10)

        if choice == 1:
            new_room = Room()
            self.build_dungeon(new_room)
            room.add_left(new_room)
        elif choice == 2:
            new_room = Room()
            self.build_dungeon(new_room)
            room.add_top(new_room)
        elif choice == 3:
            new_room = Room()
            self.build_dungeon(new_room)
            room.add_right(new_room)
        elif choice == 4:
            new_room = Room()
            self.build_dungeon(new_room)
            room.add_bottom(new_room)
        else:
            return

    def create_dungeon(self):
        return self.build_dungeon(self.starting_room)
    
    def display_dungeon(self, room, indent=0):
        print('\t' * indent + str(indent))
        if room.room_left != None:
            self.display_dungeon(room.room_left, indent + 1)
        elif room.room_top != None:
            self.display_dungeon(room.room_top, indent + 1)
        elif room.room_right != None:
            self.display_dungeon(room.room_right, indent + 1)
        elif room.room_right != None:
            self.display_dungeon(room.room_bottom, indent + 1)
        else:
            print('\t' * (indent + 1) + str(indent))

# if __name__ == 'main':
#     Dungeon.create_dungeon()