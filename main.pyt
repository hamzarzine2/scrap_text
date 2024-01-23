import pygetwindow as gw
import pyautogui
from PIL import ImageGrab, Image
import pytesseract

inputValue = input("enter your window to follow : ")
window = gw.getAllWindows()

for win in window: 
    if(inputValue.lower() in win.title.lower()):
        window= win

if window:
    print(window)

    pyautogui.PAUSE = 1

    screenshot = ImageGrab.grab(bbox=(window.left, window.top, window.right, window.bottom))

    screenshot.save("NewImage.jpg", format="JPEG")
    extracted_text = pytesseract.image_to_string(screenshot)

    print(extracted_text)
    
    screenshot.show()
else:
    print("Fenêtre non trouvée.")
