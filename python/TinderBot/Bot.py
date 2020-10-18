import pyautogui
import webbrowser
import time
import random

print("****Tinder swiper V2****")

pyautogui.FAILSAFE = False
print('Make sure you are already logged in Tinder On your Browser')
a = int(input('How many people do you want to swipe?\n'))
b=int(input('How many snapshots of profile do you want?\n'))
c=input('Enter filename with extension in which you want to save snapshots -\n')
percent_right = int(input('Probabilities of swiping right? [0-100]\n'))
probs_right = percent_right / 100.0

webbrowser.open('https://www.tinder.com', new=1, autoraise=True)
time.sleep(10)

for i in range(0, a):
	r = random.random()
	swipe_direction = None
	if r < probs_right:
		swipe_direction = 'right'
		pyautogui.press('right')
	else:
		swipe_direction = 'left'
		pyautogui.press('left')
	time.sleep(1)
	if b!=0:pyautogui.screenshot(c)
	b-=1
	time.sleep(2)
	print('person', i+1, 'swiped', swipe_direction)
