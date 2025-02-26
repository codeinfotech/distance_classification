# test_script.py
import cv2
import os

def test_image_loading():
    images = ['Plaksha_Faculty.jpg', 'Dr_Shashi_Tharoor.jpg']
    for img in images:
        if not os.path.exists(img):
            print(f"{img} not found")
            return False
        image = cv2.imread(img)
        if image is None:
            print(f"Failed to load {img}")
            return False
    print("All images loaded successfully!")
    return True

if __name__ == "__main__":
    if not test_image_loading():
        exit(1)