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
    try:

        if state1:
            img1 = pyautogui.locateCenterOnScreen(currentDungeon, confidence=0.6, region=region)
            if img1 is not None:
                state1 = False
                state2 = True
                # Click to go to dungeon menu
                pyautogui.click(img1.x, img1.y)
                time.sleep(0.5)

                #tempImg1 = pyautogui.locateCenterOnScreen('./imgs/normal.png', confidence=0.6, region=region)
                # Click to go to normal mode
                #pyautogui.click(tempImg1.x, tempImg1.y)

                tempImg2 = pyautogui.locateCenterOnScreen('./imgs/match.png', confidence=0.6, region=region)
                # Click to start matching
                pyautogui.click(tempImg2.x, tempImg2.y)
                print("Matching...")

        if state2:
            while True:
                img2 = pyautogui.locateCenterOnScreen('./imgs/accept.png', confidence=0.7, region=region)
                if img2 is not None:
                    state2 = False
                    state3 = True
                    # Click to accept the matching
                    pyautogui.doubleClick()
                    print("Match Found")
                    print("Loading...")
                    break

        if state3:
            while True:
                entered = pyautogui.locateOnScreen('./imgs/enteredDungeon.png', confidence=0.6, region=region)
                if entered is not None:
                    state3 = False
                    state4 = True
                    print("Dungeon entered")
                    break
                else:
                    tempImg = pyautogui.locateOnScreen('./imgs/queuepop.png', confidence=0.6, region=region)
                    if tempImg is not None:
                        state3 = False
                        state2 = True
                        print("Match declined, retrying...")
                        break

        if state4:
            img3 = pyautogui.locateOnScreen('./imgs/clearedD2.png', confidence=0.6, region=region)
            if img3 is not None:
                state3 = False
                state1 = True
                tempImg3 = pyautogui.locateCenterOnScreen('./imgs/backbutton.png', confidence=0.6, region=region)
                # Click the center coordinates of the found image
                pyautogui.click(tempImg3.x, tempImg3.y)
                print("Run completed")

    except pyautogui.ImageNotFoundException:
        # Image is not currently on screen
        time.sleep(0.1)  # Sleep briefly to avoid high CPU usage
    except KeyboardInterrupt:
        print("Auto clicker stopped.")
        break
