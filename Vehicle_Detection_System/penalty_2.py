from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
from tkinter.filedialog import askopenfile
import sys
import mysql.connector
from requests import options
from PIL import Image
from datetime import *



def submit_data():

    vehicle_no = name_entry.get()
    access_code = name_entry2.get()
    current_date = date.today()
    curent_time = datetime.now()

    if access_code == 8766805229:
        mydb = mysql.connector.connect(host="localhost",username="root",password="",db="vehicle_detection_system")
        mycursor = mydb.cursor()
        sql = f"INSERT INTO panelty_login(vehicle_no, access_code, date, time) VALUES ('{vehicle_no}', '{access_code}', '{current_date}', '{curent_time}')"
        mycursor.execute(sql)
        mydb.commit()
        root2.destroy()
        import penalty_2
    else:
        canvas.create_text(500, 575, text="Worng Access Key", fill="black", font=('Helvetica 18 bold'))



    

def back():
    root2.destroy()
    import main_landing_page


root2 = Tk()
root2.title("Vehicle Registration")
root2.resizable(False, False)
root2.geometry("1400x700+60+20")  


img2 =Image.open("penalty_bg.png")
bg2 = ImageTk.PhotoImage(img2)

# Add image
label2 = Label(root2, image=bg2, borderwidth=0)
label2.place(x = 0,y = 0)

canvas = Canvas(root2, width=1000, height=650)
canvas.pack()
png = PhotoImage(file = "white_box .png")
canvas.create_image(0, 0, image = png, anchor = "nw")
canvas.place(relx=0.5, rely=0.5, anchor=CENTER)     
canvas.create_text(500, 50, text="Penalty", fill="black", font=('Helvetica 25 bold'))
canvas.create_rectangle(100, 150 , 925, 600, fill= "white", width=5)

enrty_name_1 = Image.open("input_image.png")
resize = enrty_name_1.resize((500,70))
new_pic = ImageTk.PhotoImage(resize)
name_label = Label(root2, text="Enter the Vehicle Number", bg="white", font=('bold',25))
name_label.place(x=510,y=215)
enrty_label = Label(root2, image=new_pic, border=0)
enrty_label.place(x=450, y=270)
name_entry = Entry(root2,width=28,border=0,font=('bold',22))
name_entry.place(x=470,y=290)

enrty_name_12 = Image.open("input_image.png")
resize2 = enrty_name_12.resize((500,70))
new_pic2 = ImageTk.PhotoImage(resize2)
name_label2 = Label(root2, text="Enter the Access Code", bg="white", font=('bold',25))
name_label2.place(x=520,y=350)
enrty_label2 = Label(root2, image=new_pic2, border=0)
enrty_label2.place(x=450, y=395)
name_entry2 = Entry(root2,width=28,border=0,font=('bold',22))
name_entry2.place(x=470,y=415)

upload2 = PhotoImage(file="back_logo.png")
img_label_5 = Label(image=upload2)
b1 = Button(root2, image = upload2, text='Back',borderwidth=0, command=lambda:back())
b1.place(x = 450, y = 520)

upload3 = PhotoImage(file="submit_logo.png")
img_label_6 = Label(image=upload3)
b1 = Button(root2, image = upload3, text='Submit',borderwidth=0, command=lambda:submit_data())
b1.place(x = 700, y = 513)


root2.mainloop()