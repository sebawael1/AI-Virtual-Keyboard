# Virtual Keyboard with Hand Tracking
###### 🚀 Overview
Ever imagined typing without touching a single key? Welcome to the future of interaction — a gesture-controlled virtual keyboard that lets you type in mid-air using just your fingers and a webcam!
This project combines the power of computer vision and machine learning to create a futuristic typing experience. With just your hand and a camera, you can type letters, hit space, and even delete — all without a physical keyboard. Whether you're building for accessibility, exploring human-computer interaction, or just love cool tech, this project delivers a fun, interactive experience that feels like something out of a sci-fi movie.

##### How To Play:
1. Run the program on your computer.
2. Position your hand in front of the webcam (index finger pointing up).
3. Hover your finger over the desired key on the screen.
4. Pinch your fingers together to simulate pressing the key.
5. The pressed key will appear in the text box on the screen.


[![Watch the demo](https://github.com/user-attachments/assets/f1f8501c-477d-4e68-8dde-83815ee85342)



## 🖥️ Requirements

Install the dependencies with:

```bash
pip install opencv-python
pip install cvzone
```


## 🛠️ Tech Stack

| Technology | Role |
|------------|------|
| **Python** | Core Programming Language |
| **OpenCV** | Image and video processing |
| **cvzone** | Simplified hand tracking and drawing |
| **MediaPipe** | Underlying hand tracking model via cvzone |

## 🧩 How It Works

- **Hand Detection**: Uses `cvzone.HandTrackingModule` (based on MediaPipe) to track hand landmarks in real-time.
- **Finger Logic**: Detects when the index finger is over a button and middle finger gets close to register a "press."
- **Virtual Buttons**: Drawn using OpenCV, with click logic built in.
- **Dynamic Typing**: Pressed keys are shown in a text box on-screen, simulating real typing

## 🧠 Features
Fully interactive virtual keyboard
Real-time hand detection and gesture recognition
Simulates real keyboard layout with space and delete functionality
Clean, responsive UI with visual feedback
Adjustable font sizes and button dimensions



## Lastly, This project combines computer vision and human-computer interaction in an engaging way. It's not only fun to use but also opens the door for accessibility tools, gaming input systems, or gesture-controlled interfaces
