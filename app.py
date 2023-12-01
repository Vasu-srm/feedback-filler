from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

def pressTab():
    keyboard.press(Key.tab)
    time.sleep(0.1)
    keyboard.release(Key.tab)
    time.sleep(0.1)

def selectOption(option):
    for _ in range(option):
        pressDown()

def fill_feedback():
    # Select "excellent"
    selectOption(option=1)

    # Move to the next field
    pressTab()

# Print a message to indicate when the script is about to start
print("Get ready and point your cursor at the first index position...")
time.sleep(3)

# Infinite loop to keep filling the form
while True:
    fill_feedback()
    # Add any additional logic if needed (e.g., break the loop after a certain number of iterations)
