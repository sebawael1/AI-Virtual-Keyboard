import cv2
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

detector = HandDetector(detectionCon=0.8)

keys = [
    ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "Del"],
    ["A", "S", "D", "F", "G", "H", "J", "K", "L", ";"],
    ["Z", "X", "C", "V", "B", "N", "M", ",", ".", "/"],
    ["", "", "Space", "", ""]  # Space centered with padding
]

class Button():
    def __init__(self, pos, text, size=[20, 20]):
        self.pos = pos
        self.size = size
        self.text = text

def drawAll(img, buttonList):
    for button in buttonList:
        x, y = button.pos
        w, h = button.size
        cv2.rectangle(img, button.pos, (x + w, y + h), (255, 0, 255), cv2.FILLED)

        font_scale = 1.5 if button.text != "Space" else 1.3  # smaller font
        offset = 7 if button.text != "Space" else 50
        cv2.putText(img, button.text, (x + offset, y + int(h * 0.7)),
                    cv2.FONT_HERSHEY_PLAIN, font_scale, (0, 0, 0), 1)  # thinner text
    return img

startX = 40
spacingX = 54 # less horizontal space between buttons
spacingY = 54 # less vertical space between rows
keyWidth = 51  # smaller button width
keyHeight = 51  # smaller button height

buttonList = []
for i in range(len(keys)):
    row = keys[i]
    for j, key in enumerate(row):
        if key == "":
            continue  # skip empty placeholders

        if key == "Space":
            width = 200
        elif key == "Del":
            width = 60
        else:
            width = keyWidth

        x = startX + spacingX * j
        y = 50 + spacingY * i
        buttonList.append(Button([x, y], key, size=[width, keyHeight]))

finalText = ""
delayCounter = 0

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    hands, img = detector.findHands(img)
    img = drawAll(img, buttonList)

    if hands:
        lmList = hands[0]["lmList"]
        if lmList and len(lmList) >= 13:
            for button in buttonList:
                x, y = button.pos
                w, h = button.size

                if x < lmList[8][0] < x + w and y < lmList[8][1] < y + h:
                    cv2.rectangle(img, button.pos, (x + w, y + h), (0, 255, 0), cv2.FILLED)
                    cv2.putText(img, button.text, (x + 7, y + int(h / 1.5)),
                                cv2.FONT_HERSHEY_PLAIN, 1.0, (0, 0, 0), 1)

                    length, _, _ = detector.findDistance(lmList[8][:2], lmList[12][:2])
                    if length < 30 and delayCounter == 0:
                        keyPressed = button.text.strip()
                        if keyPressed == "Del":
                            finalText = finalText[:-1]
                        elif keyPressed == "Space":
                            finalText += " "
                        else:
                            finalText += keyPressed
                        delayCounter = 1

    if delayCounter != 0:
        delayCounter += 1
        if delayCounter > 10:
            delayCounter = 0

    # Display the typed text
    cv2.rectangle(img, (50, 350), (1100, 450), (175, 0, 175), cv2.FILLED)
    cv2.putText(img, finalText, (60, 430),
                cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 0), 3)

    cv2.imshow("Virtual Keyboard", img)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
