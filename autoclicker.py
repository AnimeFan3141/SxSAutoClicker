import pyautogui
import pygetwindow as gw
import time

def find_image(path, confidence=0.6):
    try:
        return pyautogui.locateCenterOnScreen(
            path,
            confidence=confidence,
            region=region,
            grayscale=True
        )
    except pyautogui.ImageNotFoundException:
        return None

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

## Change this variable to switch between different dungeons. Make sure to update the image in the imgs folder as well.
currentDungeon = './imgs/Dungeons/mechasummit.png'
dungeonDifficulty = 'normal' #normal or hard

while True:
    try:

        if state1:
            img1 = find_image(currentDungeon)
            if img1 is not None:
                state1 = False
                state2 = True
                # Click to go to dungeon menu
                pyautogui.click(img1.x, img1.y)
                time.sleep(0.5)

                if dungeonDifficulty == 'normal':
                    tempImg1 = find_image('./imgs/normal.png')
                    if tempImg1 is not None:
                        #Click to go to normal mode
                        pyautogui.click(tempImg1.x, tempImg1.y)
                        time.sleep(0.5)

                tempImg2 = find_image('./imgs/match.png')
                # Click to start matching
                pyautogui.click(tempImg2.x, tempImg2.y)
                print("Matching...")

        if state2:
            img2 = find_image('./imgs/accept.png')
            if img2 is not None:
                state2 = False
                state3 = True
                # Click to accept the matching
                pyautogui.click(img2.x, img2.y)
                print("Match Found")
                time.sleep(0.5)
                print("Loading...")

        if state3:
            entered = find_image('./imgs/dungeonEntered.png')
            if entered is not None:
                state3 = False
                state4 = True
                print("Dungeon entered")
            else:
                checkDeclined = find_image('./imgs/accept.png')
                if checkDeclined is not None:
                    pyautogui.click(checkDeclined.x, checkDeclined.y)
                time.sleep(0.5)

        if state4:
            counter = 0
            while True:
                checkReady = find_image('./imgs/ready.png')
                if checkReady is not None and counter < 2:
                    pyautogui.click(checkReady.x, checkReady.y)
                    counter = counter + 1
                    time.sleep(1)
                if counter >= 2:
                    break
            print("Waiting for run to complete...")
            while True:
                img3 = find_image('./imgs/cleared.png')
                if img3 is not None:
                    state4 = False
                    state1 = True
                    tempImg3 = find_image('./imgs/backbutton.png')
                    if tempImg3 is not None:
                        # Click the center coordinates of the found image
                        pyautogui.click(tempImg3.x, tempImg3.y)
                        print("Run completed")
                        time.sleep(0.1)
                        break
        
        time.sleep(0.1)

    except KeyboardInterrupt:
        print("Auto clicker stopped.")
        break
