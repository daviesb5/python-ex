import random

feet_in_mile = 5280
meters_in_kilometer = 1000
musicians = ["Led Zeppelin", "Queen", "AC/DC", "Phil Collins", "Coldplay", "Bon Jovi", "Chicago", "Def Leppard", "Genesis", "David Bowie", "Van Halen", "Journey", "All American Rejects", "Weezer", "Relient K"]

def get_file_ext(filename):
    return filename[filename.index(".") + 1:]

def roll_dice(num):
    return random.randint(1, num)