from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
from tkinter.filedialog import askopenfile


root = Tk() 
root.title("Vehical Detection System")
root.resizable(False, False)
root.geometry("1400x700+60+20")  


img =Image.open('wallpaper.png')
bg = ImageTk.PhotoImage(img)

# Add image
label = Label(root, image=bg, borderwidth=0)
label.place(x = 0,y = 0)

canvas = Canvas(root, width=1000, height=500)
canvas.pack()
png = PhotoImage(file = "white_box .png") # Just an example
canvas.create_image(0, 0, image = png, anchor = "nw")
canvas.place(relx=0.5, rely=0.5, anchor=CENTER)     
img = ImageTk.PhotoImage(Image.open("car_search_logo.png"))  
canvas.create_image(130, 180, anchor=NW, image=img)
canvas.create_line(500, 200, 500, 400, fill="black", width=3)
canvas.create_text(500, 50, text="Vehicle Detection System", fill="black", font=('Helvetica 25 bold'))

def vehicle_regisration():
    root.destroy()
    import Vehicle_Register_Form

def vehicle_video():
    root.destroy()
    import video_module_2

def image():
    root.destroy()
    import image_module

def penalty():
    root.destroy()
    import penalty
    


vehicle_register_btn = PhotoImage(file="Vehicle_Register_logo.png")
img_label = Label(image=vehicle_register_btn)
my_vehicle_btn = Button(root, image = vehicle_register_btn, command=vehicle_regisration, borderwidth=0)
my_vehicle_btn.place(x = 795, y = 250)

vehicle_register_btn_2 = PhotoImage(file="Search_by_Photo.png")
img_label_2 = Label(image=vehicle_register_btn_2)
my_vehicle_btn_2 = Button(root, image = vehicle_register_btn_2, command=image, borderwidth=0)
my_vehicle_btn_2.place(x = 785, y = 320)

vehicle_register_btn_3 = PhotoImage(file="Search_by_Video.png")
img_label_3 = Label(image=vehicle_register_btn_3)
my_vehicle_btn_3 = Button(root, image = vehicle_register_btn_3, command=vehicle_video, borderwidth=0)
my_vehicle_btn_3.place(x = 791, y = 390)

vehicle_register_btn_4 = PhotoImage(file="Penalty_logo.png")
img_label_4 = Label(image=vehicle_register_btn_4)
my_vehicle_btn_4 = Button(root, image = vehicle_register_btn_4, command=penalty, borderwidth=0)
my_vehicle_btn_4.place(x = 810, y = 460)


root.mainloop()  
