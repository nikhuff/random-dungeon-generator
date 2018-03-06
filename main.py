from dungeon import *
import numpy as np
import cv2

if __name__ == '__main__':
    # main function to sample dungeon generator
    # this is where we'll store the arrays of
    # type of rooms and the pre-instanciated rooms

    dungeon = Dungeon()
    dungeon.build_dungeon(4,4)
    dungeon.display_dungeon()