from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
from tkinter.filedialog import askopenfile
import sys
import mysql.connector
from requests import options
from PIL import Image

global filename

def upload_file():

    global img , filename 
    f_types = [('Png files','*.png'), ('Jpg Files', '*.jpg')]
    filename = filedialog.askopenfilename(filetypes=f_types)
    img=Image.open(filename)
    img_resized=img.resize((180,225)) # new width & height
    img=ImageTk.PhotoImage(img_resized)
    b2 =Button(root2,image=img) # using Button 
    b2.place(x=930, y=230)


    
def submit_data():

    

    fname = name_entry.get()
    lname = name_entry2.get()
    course = name_entry3.get()
    university = name_entry4.get()
    phone = name_entry5.get()
    email = name_entry6.get()
    license = name_entry7.get()
    vehicle = name_entry8.get()
    photoname = f"face_photo/{fname}_{lname}_{name_entry8.get()}.jpg"


    mydb = mysql.connector.connect(host="localhost",username="root",password="",db="vehicle_detection_system")
    mycursor = mydb.cursor()
    sql = f"INSERT INTO vehicle_registration_data(first_name, last_name, course, university, phone, email, license, vehicle, photoname) VALUES ('{fname}', '{lname}', '{course}', '{university}', '{phone}', '{email}', '{license}', '{vehicle}', '{photoname}')"
    mycursor.execute(sql)
    mydb.commit()

    global img , filename 
    
    with open(filename, 'rb') as fob:
        img = fob.read()

    with open(photoname, 'wb') as new_fob:
        new_fob.write(img)

    image = Image.open(photoname)
    image = image.convert("RGB")  # Convert image to RGB mode
    image.save(photoname, "JPEG")

    root2.destroy()
    import approval_form



def back():
    root2.destroy()
    import main_landing_page




root2 = Tk()
root2.title("Vehicle Registration")
root2.resizable(False, False)
root2.geometry("1400x700+60+20")  


img2 =Image.open("wallpaper3.png")
bg2 = ImageTk.PhotoImage(img2)

# Add image
label2 = Label(root2, image=bg2, borderwidth=0)
label2.place(x = 0,y = 0)

canvas = Canvas(root2, width=1000, height=650)
canvas.pack()
png = PhotoImage(file = "white_box .png") # Just an example
canvas.create_image(0, 0, image = png, anchor = "nw")
canvas.place(relx=0.5, rely=0.5, anchor=CENTER)     
canvas.create_line(650, 200, 650, 510, fill="black", width=3)
canvas.create_text(500, 50, text="Vechicle Registration Information", fill="black", font=('Helvetica 25 bold'))
canvas.create_rectangle(725, 200 , 925, 450, fill= "white", width=5)


enrty_name_1 = Image.open("input_image.png")
resize = enrty_name_1.resize((250,50))
new_pic = ImageTk.PhotoImage(resize)
name_label = Label(root2, text="First Name :- ", bg="white", font=('bold',14))
name_label.place(x=225,y=215)
enrty_label = Label(root2, image=new_pic, border=0)
enrty_label.place(x=220, y=250)
name_entry = Entry(root2,width=15,border=0,font=('bold',18))
name_entry.place(x=250,y=261)

enrty_name_2 = Image.open("input_image.png")
resize2 = enrty_name_2.resize((250,50))
new_pic2 = ImageTk.PhotoImage(resize2)
name_label2 = Label(root2, text="Second Name :- ", bg="white", font=('bold',14))
name_label2.place(x=530,y=215)
enrty_label2 = Label(root2, image=new_pic2, border=0)
enrty_label2.place(x=525, y=250)
name_entry2 = Entry(root2,width=15,border=0,font=('bold',18))
name_entry2.place(x=550,y=261)



enrty_name_3 = Image.open("input_image.png")
resize3 = enrty_name_3.resize((250,50))
new_pic3 = ImageTk.PhotoImage(resize3)
name_label3 = Label(root2, text="Course :- ", bg="white", font=('bold',14))
name_label3.place(x=225,y=300)
enrty_label3 = Label(root2, image=new_pic3, border=0)
enrty_label3.place(x=220, y=335)
name_entry3 = Entry(root2,width=15,border=0,font=('bold',18), )
name_entry3.place(x=250,y=346)

enrty_name_4 = Image.open("input_image.png")
resize4 = enrty_name_4.resize((250,50))
new_pic4 = ImageTk.PhotoImage(resize4)
name_label4 = Label(root2, text="University Name :- ", bg="white", font=('bold',14))
name_label4.place(x=530,y=300)
enrty_label4 = Label(root2, image=new_pic4, border=0)
enrty_label4.place(x=525, y=335)
name_entry4 = Entry(root2,width=15,border=0,font=('bold',18))
name_entry4.place(x=550,y=346)


enrty_name_5 = Image.open("input_image.png")
resize5 = enrty_name_5.resize((250,50))
new_pic5 = ImageTk.PhotoImage(resize5)
name_label5 = Label(root2, text="Phone Number :- ", bg="white", font=('bold',14))
name_label5.place(x=225,y=385)
enrty_label5 = Label(root2, image=new_pic5, border=0)
enrty_label5.place(x=220, y=410)
name_entry5 = Entry(root2,width=15,border=0,font=('bold',18), )
name_entry5.place(x=250,y=421)

enrty_name_6 = Image.open("input_image.png")
resize6 = enrty_name_6.resize((250,50))
new_pic6 = ImageTk.PhotoImage(resize6)
name_label6 = Label(root2, text="Email ID :- ", bg="white", font=('bold',14))
name_label6.place(x=530,y=385)
enrty_label6 = Label(root2, image=new_pic4, border=0)
enrty_label6.place(x=525, y=410)
name_entry6 = Entry(root2,width=15,border=0,font=('bold',18))
name_entry6.place(x=550,y=421)


enrty_name_7 = Image.open("input_image.png")
resize7 = enrty_name_7.resize((250,50))
new_pic7 = ImageTk.PhotoImage(resize7)
name_label7 = Label(root2, text="License Number :- ", bg="white", font=('bold',14))
name_label7.place(x=225,y=470)
enrty_label7 = Label(root2, image=new_pic7, border=0)
enrty_label7.place(x=220, y=495)
name_entry7 = Entry(root2,width=15,border=0,font=('bold',18), )
name_entry7.place(x=250,y=506)

enrty_name_8 = Image.open("input_image.png")
resize8 = enrty_name_8.resize((250,50))
new_pic8 = ImageTk.PhotoImage(resize8)
name_label8 = Label(root2, text="Vehicle Number :- ", bg="white", font=('bold',14))
name_label8.place(x=530,y=470)
enrty_label8 = Label(root2, image=new_pic8, border=0)
enrty_label8.place(x=525, y=495)
name_entry8 = Entry(root2,width=15,border=0,font=('bold',18))
name_entry8.place(x=550,y=506)





upload = PhotoImage(file="upload_logo.png")
img_label_4 = Label(image=upload)
b1 = Button(root2, image = upload, text='Upload File',borderwidth=0,command = lambda:upload_file())
b1.place(x = 900, y = 506)


upload2 = PhotoImage(file="back_logo.png")
img_label_5 = Label(image=upload2)
b1 = Button(root2, image = upload2, text='Back',borderwidth=0, command=lambda:back())
b1.place(x = 225, y = 580)


upload3 = PhotoImage(file="submit_logo.png")
img_label_6 = Label(image=upload3)
b1 = Button(root2, image = upload3, text='Submit',borderwidth=0, command=submit_data)
b1.place(x = 525, y = 575)






root2.mainloop()