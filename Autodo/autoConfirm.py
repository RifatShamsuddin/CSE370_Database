import pyautogui
import time

# Wait for 3 seconds
time.sleep(3)

# Get the current mouse position
current_x, current_y = pyautogui.position()
print(f"Current mouse position: X={current_x}, Y={current_y}")