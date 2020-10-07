import pyautogui
import webbrowser
import time
import random

print("****Tinder swiper V2****")

pyautogui.FAILSAFE = False
print('Make sure you are already logged in Tinder On your Browser')
a = int(input('How many people do you want to swipe?\n'))

webbrowser.open('https://www.tinder.com',new = 1,autoraise = True)
time.sleep(10)

for i in range(0,a) :
	if random.randint(0,1) > 0.5:
		pyautogui.press('right')
	else:
		pyautogui.press('left')
	time.sleep(1)
	print('person',i+1,'swiped')
