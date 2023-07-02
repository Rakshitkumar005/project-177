from tkinter import *

root=Tk()
root.geometry("500x500")
root.title("Private Variable Login Page")

label_name=Label(root,text="Name: ")
label_name.place(relx=0.4,rely=0.1,anchor=CENTER)

name_input_box=Entry(root)
name_input_box.place(relx=0.6,rely=0.1,anchor=CENTER)

label_password=Label(root,text="Password: ")
label_password.place(relx=0.4,rely=0.2,anchor=CENTER)

password_input_box=Entry(root)
password_input_box.place(relx=0.6,rely=0.2,anchor=CENTER)

captcha_label=Label(root,text="Captcha: ")
captcha_label.place(relx=0.4,rely=0.3,anchor=CENTER)

captcha_input_box=Entry(root)
captcha_input_box.place(relx=0.6,rely=0.3,anchor=CENTER)

updated_name_label=Label(root)
updated_name_label.place(relx=0.5,rely=0.7,anchor=CENTER)

updated_password_label=Label(root)
updated_password_label.place(relx=0.5,rely=0.8,anchor=CENTER)

updated_captcha_label=Label(root)
updated_captcha_label.place(relx=0.5,rely=0.9,anchor=CENTER)

class userDB():
    
    def __init__(self):
        self.__username = "Rakshit"
        self.__password = "123456"
        self.captcha = captcha_input_box.get()
        
    def showUser(self):
        updated_name_label["text"] = "Name : " + self.__username
        updated_password_label["text"] = "Password : " + self.__password
        updated_captcha_label["text"] = "Captcha : " + self.captcha
        

user = userDB()

def addUser():
    global user 
    user.username = name_input_box.get()
    user.password = password_input_box.get()
    user.captcha = captcha_input_box.get()
    
add_btn = Button(root, text = "Update Login Details", command = addUser)
add_btn.place(relx = 0.4, rely = 0.5, anchor = CENTER)

show_btn = Button(root, text = "Show Profile", command = user.showUser)
show_btn.place(relx = 0.6, rely = 0.5, anchor = CENTER)

root.mainloop()