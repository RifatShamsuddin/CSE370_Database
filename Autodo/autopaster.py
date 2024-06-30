import pyautogui
import time
import random
import sys


# Wait for 3 seconds
time.sleep(3)
tab_x, tab_y = 110, 3
tab_end_x, tab_end_y = 231, 15
tab_save_x, tab_save_y = 670, 1045
# Get the current mouse position
current_x, current_y = pyautogui.position()

#Have to change this time to time
x, y = 1940, 754  # Example pixel coordinates
X_Paste, Y_Paste = 2349, 540
i=0
while i<5:
    pyautogui.moveTo(tab_x, tab_y)
    pyautogui.click(tab_x, tab_y)

    for remaining in range(2, 0, -1):
        sys.stdout.write("\r")
        sys.stdout.write("{:2d} seconds remaining.".format(remaining))
        sys.stdout.flush()
        time.sleep(2)

    pyautogui.moveTo(tab_save_x, tab_save_y)
    pyautogui.click(tab_save_x, tab_save_y)

    for remaining in range(2, 0, -1):
        sys.stdout.write("\r")
        sys.stdout.write("{:2d} seconds remaining.".format(remaining))
        sys.stdout.flush()
        time.sleep(2)

    pyautogui.moveTo(tab_end_x, tab_end_y)
    pyautogui.click(tab_end_x, tab_end_y)

    for remaining in range(2, 0, -1):
        sys.stdout.write("\r")
        sys.stdout.write("{:2d} seconds remaining.".format(remaining))
        sys.stdout.flush()
        time.sleep(2)

    pyautogui.moveTo(x, y)
    pyautogui.click(x, y)
    pyautogui.press('pagedown')
    pyautogui.click(x, y)
    pyautogui.click(x, y)
    pyautogui.click(x, y)
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.click(X_Paste, Y_Paste)
    pyautogui.hotkey('ctrl', 'v')

#usually increments 30 & 16

    y = y+30
    Y_Paste = Y_Paste+16
    i = i+1

    r=random.randint(200, 260)
    for remaining in range(r, 0, -1):
        sys.stdout.write("\r")
        sys.stdout.write("{:2d} seconds remaining.".format(remaining))
        sys.stdout.flush()
        time.sleep(1)

# # pyautogui.moveTo(x, y)

print(f"Current mouse position: X={current_x}, Y={current_y}")


# import time
# import sys
#
# for remaining in range(10, 0, -1):
#     sys.stdout.write("\r")
#     sys.stdout.write("{:2d} seconds remaining.".format(remaining))
#     sys.stdout.flush()
#     time.sleep(1)
#
# sys.stdout.write("\rComplete!            \n")
