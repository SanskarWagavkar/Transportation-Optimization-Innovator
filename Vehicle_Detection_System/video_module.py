import cv2
from cv2 import minAreaRect
import easyocr
import tkinter as tk
from PIL import ImageTk, Image
from functools import partial

harcascade = "model/haarcascade_russian_plate_number.xml"

# Initialize the tkinter window
window = tk.Tk()
window.title("Number Plate Detection")
window.geometry("800x600")

# Create a label to display the video stream from the camera
video_label = tk.Label(window)
video_label.pack()

# Create buttons for camera, scan, and detect
camera_button = tk.Button(window, text="Open Camera")
scan_button = tk.Button(window, text="Scan Image")
detect_button = tk.Button(window, text="Detect Number Plate")

# Set up the video capture
cap = cv2.VideoCapture(0)

def open_camera():
    _, frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(frame)
    img = img.resize((640, 480))
    img_tk = ImageTk.PhotoImage(img)
    video_label.img_tk = img_tk
    video_label.configure(image=img_tk)
    video_label.after(10, open_camera)

def scan_image():
    min_area = 500
    _, frame = cap.read()
    plate_cascade = cv2.CascadeClassifier(harcascade)
    img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    plates = plate_cascade.detectMultiScale(img_gray, 1.1, 4)

    for (x, y, w, h) in plates:
        area = w * h

        if area > min_area:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame, "Number Plate", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 0, 255), 2)
            
            img_roi = frame[y: y + h, x:x + w]
            cv2.imshow("ROI", img_roi)
            cv2.waitKey(0)
    
    cv2.imshow("Result", frame)

def detect_number_plate():
    _, frame = cap.read()
    cv2.imwrite("scanned_img.jpg", frame)
    reader = easyocr.Reader(['en'])
    output = reader.readtext("scanned_img.jpg")
    if len(output) > 0:
        number_plate = output[0][-2]
        print("Detected Number Plate:", number_plate)
    else:
        print("No number plate detected.")
    
    cv2.imshow("Result", frame)

# Define button actions
camera_button.configure(command=open_camera)
scan_button.configure(command=scan_image)
detect_button.configure(command=detect_number_plate)

# Pack the buttons
camera_button.pack()
scan_button.pack()
detect_button.pack()

# Run the tkinter event loop
window.mainloop()

# Release the video capture and destroy windows
cap.release()
cv2.destroyAllWindows()
