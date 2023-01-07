from tkinter import *

def click():
    sus = entry.get()
    print("the code that you entered was: "+ sus)
def delete():
    entry.delete(0,END)
def backspace():
    entry.delete(len(entry.get())-1,END)
def show():
    entry.get(show=False)
def display():
    if(X.get() == 1):
        print("you agree to be scammed")
    else:
        print("you disagree to being scammed")

    

window = Tk()
window.geometry("420x420")
window.config(background= "#34c3eb")
window.title("Chibong's Code Reader")
photo = PhotoImage('gundu.png')

x = IntVar()



entry = Entry(window,font=("Arial",50),bg="red",show="*")
entry.pack(side=BOTTOM)

gabel = Label(window,
text = "Chibong presents",
font=("Arial",40), 
fg="red",
bg="black",
padx=15,
pady=15,
relief=RAISED)
gabel.pack(side = TOP)

label = Label(window,
text = "Chibong Secret code reader",
font=("Arial",40),
 fg="red",
 bg="black",
 padx=15,
 pady=15,
 relief=RAISED)
label.pack()


sabel = Label(window,
text = "Enter a secret message that you can't even see",
font=("Arial",40),
 fg="red",
 bg="black",
 padx=15,
 pady=15,
 relief=RAISED)
sabel.pack()

dabel = Label(window,
text = "the message you send will be printed in the terminal",
font=("Arial",40),
 fg="red",
 bg="black",
 padx=15,
 pady=15,
 relief=RAISED)
dabel.pack()

tabel = Label(window,
text = "type the secret code in the red box ",
font=("Arial",15),
 fg="red",
 bg="black",
 padx=15,
 pady=15,
 relief=RAISED)
tabel.pack(side=BOTTOM)

button = Button(window,text="submit",
font=("Arial",16,'bold'),
bg= "#f5f536",
fg="#88308a",
padx="10",
pady="10",
relief=RAISED,
command=click,
state= ACTIVE)

del_button = Button(window,text="DELETE",
font=("Arial",16,'bold'),
bg= "#f5f536",
fg="#88308a",
padx="10",
pady="10",
relief=RAISED,
command=delete,
state= ACTIVE)

backspace = Button(window,text="Backspace",
font=("Arial",16,'bold'),
bg= "#f5f536",
fg="#88308a",
padx="10",
pady="10",
relief=RAISED,
command=backspace,
state= ACTIVE)

check_button =Checkbutton(window,
text="you agree to selling all your property to me for free",
variable=X,
onvalue=1,
offvalue=0,
font=("Arial",14))


button.pack(side=RIGHT)
del_button.pack(side=RIGHT)
backspace.pack(side = RIGHT)
check_button.pack(side=LEFT)
window.mainloop()