from PIL import ImageGrab, ImageOps
import pyautogui
import time
import array
from numpy import *

class coordinates():
    replayBtn = (340, 390)
    dino = (171, 440)

def restartGame():
    pyautogui.click(coordinates.replayBtn)
    pyautogui.keyDown('down')

def pressSpace():
    pyautogui.keyDown('space')
    time.sleep(0.05)
    print('Jump')
    time.sleep(0.18)
    pyautogui.keyUp('space')
    pyautogui.keyDown('down')

def imageGrab():
    #box = (x1,y1,x2,y2) = (dinoCoord.X + distance, dinoCoord.Y, dinoCoord.X + distance + 40, dinoCoord.Y + 30)
    box = (coordinates.dino[0]+60, coordinates.dino[1],coordinates.dino[0]+150, coordinates.dino[1]+5)
    image = ImageGrab.grab(box)
    grayImage = ImageOps.grayscale(image)
    a = array(grayImage.getColors())
    
    return a.sum()

def main():
    restartGame()
    while True:
        if(imageGrab() != 697):
            pressSpace()
            time.sleep(0.1)