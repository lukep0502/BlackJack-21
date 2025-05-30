import os

IMAGE_SIZE = 200     #128
SCREEN_SIZE = 580   #512
NUM_TILES_SIDE = 4
NUM_TILES_TOTAL = 16
MARGIN = 8

BJCARDS_DIR = 'blackjackcards'
BJCARDS_FILES = [x for x in os.listdir(BJCARDS_DIR)]
BJCARDS_FILES2 = [x for x in os.listdir(BJCARDS_DIR)]     #if x[-3:].lower() == 'png'
#assert len(BJCARDS_FILES) == 53



