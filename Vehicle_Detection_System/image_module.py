from datetime import date
from tkinter import filedialog
import mysql.connector
import cv2
import tkinter as tk
from PIL import Image, ImageTk
import easyocr
import re
from tkinter import CENTER, Canvas, Label, PhotoImage, Toplevel

harcascade = "model/haarcascade_russian_plate_number.xml"
global license_plate
global cleaned_string
# Initialize Tkinter window
window = tk.Tk()
window.title("License Plate Recognition")
window.resizable(False, False)
window.geometry("1500x750+10+10")

img =Image.open('video_bg.png')
bg = ImageTk.PhotoImage(img)

# Add image
label = tk.Label(window, image=bg, borderwidth=0)
label.place(x = 0,y = 0)

canvas = tk.Canvas(window, width=1300, height=700)
canvas.pack()
png = tk.PhotoImage(file = "white_box .png") # Just an example
canvas.create_image(0, 0, image = png, anchor = "nw")
canvas.create_line(800, 200, 800, 510, fill="black", width=3)
canvas.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
canvas.create_text(650, 60, text="Vehicle Detection Using Photo", fill="black", font=('Helvetica 25 bold'))
canvas.create_rectangle(50, 125 , 690, 605, fill= "white", width=3)
canvas.create_rectangle(900, 125 , 1205, 230, fill= "white", width=3)




video_frame = tk.Label(window, borderwidth=0)
video_frame.place(x=150, y=150)

roi_label = tk.Label(window, borderwidth=0)
roi_label.place(x=1000, y=150)


# Create an OpenCV video capture object
cap = cv2.VideoCapture(0)
cap.set(3, 390)
cap.set(4, 450)

# Create EasyOCR reader
reader = easyocr.Reader(['en'])

global first_name, last_name, vehicle_no

# Minimum area to consider for license plate detection
min_area = 500

def open_search_window(cleaned_string):
    search_window = Toplevel(window)
    search_window.title("Search Information")
    search_window.resizable(False, False)
    search_window.geometry("1500x750+10+10")

  
    img2 =Image.open('wallpaper.png')
    bg2 = ImageTk.PhotoImage(img2)

    # Add image
    label = Label(search_window, image=bg2, borderwidth=0)
    label.place(x = 0,y = 0)

    canvas = Canvas(search_window, width=1300, height=650)
    canvas.pack()
    png = PhotoImage(file = "white_box .png") # Just an example
    canvas.create_image(0, 0, image = png, anchor = "nw")
    canvas.place(relx=0.5, rely=0.5, anchor=CENTER)  
    canvas.create_line(850, 200, 850, 510, fill="black", width=3)
    canvas.create_text(700, 50, text="Vehicle Owner Information", fill="black", font=('Helvetica 25 bold'))
  

    print(cleaned_string)
    
    mydb = mysql.connector.connect(host="localhost",username="root",password="",db="vehicle_detection_system")
    mycursor = mydb.cursor()
    sql = f"SELECT first_name, last_name, phone, course, university, vehicle, license, email FROM vehicle_registration_data WHERE RIGHT(vehicle, 4) = '{cleaned_string[-4:]}'"
    mycursor.execute(sql)

    records = mycursor.fetchone()

    if records is not None:
        first_name = records[0]
        last_name = records[1]
        phone = records[2]
        course = records[3]
        university_name = records[4]
        vehicle_no = records[5]
        License_no = records[6]
        email = records[7]
        mydb.commit()

        label_fname = tk.Label(search_window, text=f"First Name :- {first_name}", font=('Helvetica 14 bold'), bg="white",borderwidth=0)
        label_fname.place(x=150, y=200)
        label_lname = tk.Label(search_window, text=f"Last Name :- {last_name}", font=('Helvetica 14 bold'), bg="white",borderwidth=0)
        label_lname.place(x=550, y=200)
        label_phone = tk.Label(search_window, text=f"Phone Number :- {phone}", font=('Helvetica 14 bold'), bg="white",borderwidth=0)
        label_phone.place(x=150, y=300)
        label_course = tk.Label(search_window, text=f"Course Name :- {course}", font=('Helvetica 14 bold'), bg="white",borderwidth=0)
        label_course.place(x=150, y=400)
        label_university = tk.Label(search_window, text=f"University Name :- {university_name}", font=('Helvetica 14 bold'), bg="white",borderwidth=0)
        label_university.place(x=550, y=400)
        label_vehicle = tk.Label(search_window, text=f"Vehicle Number :- {vehicle_no}", font=('Helvetica 14 bold'), bg="white",borderwidth=0)
        label_vehicle.place(x=150, y=500)
        label_License = tk.Label(search_window, text=f"License Number :- {License_no}", font=('Helvetica 14 bold'), bg="white",borderwidth=0)
        label_License.place(x=550, y=500)
        label_date = tk.Label(search_window, text=f"Email ID :- {email}", font=('Helvetica 14 bold'), bg="white",borderwidth=0)
        label_date.place(x=550, y=300)

        # Additional code for the search window
        #label = tk.Label(search_window, text=cleaned_string)
        #label.pack()
    else:
        # Handle the case when no records are found
        label = tk.Label(search_window, text="No records found")
        label.pack()

    upload3 = PhotoImage(file="back_logo.png")
    img_label_5 = Label(image=upload3)
    b1 = tk.Button(search_window, image = upload3, text='Back',borderwidth=0, command=lambda:back())
    b1.place(x = 300, y = 615)

    upload4 = PhotoImage(file="main_page_logo.png")
    img_label_5 = Label(image=upload4)
    b1 = tk.Button(search_window, image = upload4, text='Back',borderwidth=0, command=lambda:main_page())
    b1.place(x = 600, y = 615)

    upload5 = PhotoImage(file="give_penalty_logo.png")
    img_label_6 = Label(image=upload5)
    b1 = tk.Button(search_window, image = upload5, text='Back',borderwidth=0, command=lambda:panelty())
    b1.place(x = 900, y = 615)


    def main_page():
        window.destroy()
        import main_landing_page
    
    def back():
        window.destroy()
        import video_module_2

    def panelty():
        window.destroy()
        import penalty

        

    # Additional code for the search window
    #label = tk.Label(search_window, text=cleaned_string)
    #label.pack()

    def open_img(first_name, last_name, vehicle_no):
        image_path = f"face_photo/{first_name}_{last_name}_{vehicle_no}.jpg"  # Replace with the actual path to your image
        image = Image.open(image_path)
        desired_width = 275
        desired_height = 300

        # Resize the image
        image_re = image.resize((desired_width, desired_height), Image.ANTIALIAS)

        img_label = tk.Label(search_window)
        img_label.place(x=1000, y=250)

        # Convert the resized image to Tkinter PhotoImage
        tk_image = ImageTk.PhotoImage(image_re)

        # Configure the label with the resized image
        img_label.config(image=tk_image)
        img_label.img_re = tk_image
        search_window.mainloop()

    open_img(first_name, last_name, vehicle_no)

    


def process_frame():
    # Load the uploaded photo
    file_path = filedialog.askopenfilename()

    img = cv2.imread(file_path)

    # Convert the frame to grayscale
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Perform license plate detection
    plate_cascade = cv2.CascadeClassifier(harcascade)
    plates = plate_cascade.detectMultiScale(img_gray, 1.1, 4)

    for (x, y, w, h) in plates:
        area = w * h

        if area > min_area:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(img, "Number Plate", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 0, 255), 2)

            # Extract the license plate region
            img_roi = img[y: y + h, x: x + w]

            img_roi_rgb = cv2.cvtColor(img_roi, cv2.COLOR_BGR2RGB)
            img_roi_pil = Image.fromarray(img_roi_rgb)

            # Resize the ROI image to fit the label
            img_roi_pil = img_roi_pil.resize((300, 100))

            # Convert the ROI image to Tkinter-compatible format
            img_roi_tk = ImageTk.PhotoImage(img_roi_pil)

            # Display the ROI image in a label
            roi_label.configure(image=img_roi_tk)
            roi_label.image = img_roi_tk

            # Save the scanned image
            cv2.imwrite("scanned_img.jpg", img_roi)

    # Display the video frame in Tkinter
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(img)
    img_re = img.resize((635, 475))
    img = ImageTk.PhotoImage(img_re)
    video_frame.configure(image=img)
    video_frame.image = img
    

def detect():
    # Perform OCR on the scanned image
    output = reader.readtext("scanned_img.jpg")
    if len(output) > 0:
        license_plate = output[0][-2]
        print(license_plate)

        cleaned_string = re.sub(r'[^a-zA-Z0-9]', '', license_plate)
        cleaned_string = cleaned_string.replace(' ', '')


        number = tk.Label(window, text=cleaned_string, font=('Helvetica 25 bold'), borderwidth=0)
        number.place(x = 1050, y = 400)
        return cleaned_string

def back():
    window.destroy()
    import main_landing_page
    

    

# Start processing the video frames
upload2 = tk.PhotoImage(file="upload_logo.png")
img_label_5 = tk.Label(image=upload2)
b1 = tk.Button(window, image = upload2, text='Open',borderwidth=0, command=lambda:process_frame())
b1.place(x = 475, y = 650)


upload4 = tk.PhotoImage(file="back_logo.png")
img_label_4 = tk.Label(image=upload4)
b4 = tk.Button(window, image = upload4, text='Open',borderwidth=0, command=lambda:back())
b4.place(x = 200, y = 650)

upload3 = tk.PhotoImage(file="scan_logo.png")
img_label_3 = tk.Label(image=upload3)
b3 = tk.Button(window, image = upload3, text='Open',borderwidth=0, command=lambda:detect())
b3.place(x = 1025, y = 300)

upload5 = tk.PhotoImage(file="search_logo.png")
img_label_5 = tk.Label(image=upload5)
b5 = tk.Button(window, image = upload5, text='Open',borderwidth=0, command=lambda:open_search_window(detect()))
b5.place(x = 1025, y = 625)


text_widget = tk.Label(window, text ="If Scanned Number is correct then click on \nSearch Button to get Info.Else if Scanned \nNumber is Worng. Then upload the Photo \nagain and scan it again", font=('Helvetica 14 bold'), bg="white",borderwidth=0)
text_widget.place(x = 950, y = 500)






# Run the Tkinter main loop
window.mainloop()
