# Import modules
import pygame as py
import json
import glob

# Load damage types
with open("classes\\damageTypes.json") as f:
    damageTypes = json.load(f)

version = "0.25"

# Define Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
LIGHTGREY = (169, 169, 169)
GREY = (100, 100, 100)
DARKGREY = (65, 65, 65)
RED = (255, 0, 0)
LIGHTRED = (230, 95, 57)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
ORANGE = (253, 204, 85)
ERROCOLOR = (255, 0, 102)

# Define Fonts
py.font.init()

buttonFont = py.font.SysFont("Comic Sans Ms", 24)
titleFont = py.font.SysFont("Comic Sans Ms", 35)
title2Font = py.font.SysFont("Comic Sans Ms", 65)
itemFont = py.font.SysFont("Comic Sans Ms", 18)
effectFont = py.font.SysFont("Comic Sans Ms", 18)

# Define Textures
boss = {
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 1, 0, 0, 1, 0, 0,
    0, 1, 0, 1, 1, 0, 1, 0,
    1, 1, 1, 1, 1, 1, 1, 1,
    1, 1, 1, 1, 1, 1, 1, 1,
    0, 0, 1, 1, 1, 1, 0, 0,
    0, 0, 1, 0, 0, 1, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0
}

downTriangle = [py.Vector2(0, 0), py.Vector2(20, 0), py.Vector2(10, 10)]
upTriangle = [py.Vector2(0, 10), py.Vector2(20, 10), py.Vector2(10, 0)]

# Weapon Types
electric = damageTypes.get("electric")
fire = damageTypes.get("fire")
physical = damageTypes.get("physical")
laser = damageTypes.get("laser")
plasma = damageTypes.get("plasma")

# Load up sprits
imageNames = glob.glob("images\\*.png")
images =  {}

for x in imageNames:
    x = x.split("\\")[1]
    images[x] = (py.image.load(f"images\\{x}"))