import pyautogui
import pygetwindow as gw
import time

# Uses OpenCV library
# Safety feature: moving mouse to any of the 4 corners of your screen stops the program
pyautogui.FAILSAFE = True

# Getting window and activating
window = gw.getWindowsWithTitle("Main")[0]
window.activate()
time.sleep(1)

# Get window region
region = (
    window.left,
    window.top,
    window.width,
    window.height
)

print("LDPlayer region: ", region)

# Records screen state
state1 = True #Start screen to match
state2 = False #Matching to accept
state3 = False #Match accepted to dungeon entered
state4 = False #Dungeon entered to start screen

print("Auto clicker started. Press Ctrl+C in your terminal to stop.")
print("Looking for images...")

currentDungeon = './imgs/mechasummit.png'

while True:
    if state3 == False and state4 == False:
        print(".")
    try:

        if state1:
            img1 = pyautogui.locateCenterOnScreen(currentDungeon, confidence=0.6, region=region)
            if img1 is not None:
                print("Image1 found")
                state1 = False
                state2 = True
                # Click to go to dungeon menu
                pyautogui.click(img1.x, img1.y)
                # Wait a few seconds to avoid clicking too fast
                time.sleep(2)

                #tempImg1 = pyautogui.locateCenterOnScreen('./imgs/normal.png', confidence=0.6, region=region)
                # Click to go to normal mode
                #pyautogui.click(tempImg1.x, tempImg1.y)
                # Wait a few seconds to avoid clicking too fast
                #time.sleep(2)

                tempImg2 = pyautogui.locateCenterOnScreen('./imgs/match.png', confidence=0.6, region=region)
                # Click to start matching
                pyautogui.click(tempImg2.x, tempImg2.y)
                # Wait a few seconds to avoid clicking too fast
                print("Matching...")
                time.sleep(5)
            else:
                time.sleep(2)

        if state2 or state3:
            img2 = pyautogui.locateCenterOnScreen('./imgs/accept.png', confidence=0.7, region=region)
            if img2 is not None:
                print("Image2 found")
                state2 = False
                state3 = True
                # Click to accept the matching
                pyautogui.doubleClick()
                # Wait a few seconds to avoid clicking too fast
                print("Match Found")
                print("Loading...")
                time.sleep(1)
            else:
                time.sleep(2)

        if state3:
            entered = pyautogui.locateOnScreen('./imgs/enteredDungeon.png', confidence=0.6, region=region)
            if entered is not None:
                state3 = False
                state4 = True
                print("Dungeon entered")
                time.sleep(90)
            else:
                time.sleep(2)

        if state4:                
            img3 = pyautogui.locateOnScreen('./imgs/clearedD2.png', confidence=0.6, region=region)
            if img3 is not None:
                print("Image3 found")
                state3 = False
                state1 = True
                tempImg3 = pyautogui.locateCenterOnScreen('./imgs/backbutton.png', confidence=0.6, region=region)
                # Click the center coordinates of the found image
                pyautogui.click(tempImg3.x, tempImg3.y)
                # Wait a few seconds to avoid clicking too fast
                time.sleep(1)
                print("Run completed")
                time.sleep(5)
            else:
                time.sleep(2)

    except pyautogui.ImageNotFoundException:
        # Image is not currently on screen
        time.sleep(2)
    except KeyboardInterrupt:
        print("Auto clicker stopped.")
        break
