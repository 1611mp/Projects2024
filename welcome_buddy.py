from tkinter import *
window = Tk()
window.geometry("600x800")
window.title("Welcome App")

my_list =[]

def add_name():
    name = l2.get()
    my_list.append(name)
    update_listbox()

def update_listbox():
    listbox.delete(0,END)
    for name in my_list:
        listbox.insert(END, name)

 
l1 = Label(window,text="Welcome to the party!")
l1.pack()
l2 = Entry(window,text="Please enter your name")
l2.pack()
b1 = Button(window,text="Submit name",command =add_name)
b1.pack()

listbox = Listbox(window,width=50)
listbox.pack()

window.mainloop()