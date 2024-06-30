import pyautogui
from pynput import mouse

def on_click(x, y, button, pressed):
    if pressed:
        print(f"Clicked at (X: {x}, Y: {y})")

def start_listener():
    listener = mouse.Listener(on_click=on_click)
    listener.start()

if __name__ == "__main__":
    start_listener()
    input("Press Enter to stop...")
