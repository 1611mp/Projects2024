from tkinter import *
window = Tk()
window.title("Rectangle Area Calculator")
window.geometry("600x800")

def calc_area():
    """Calculates the area of the Rectangle"""
    length = float(e1.get())
    width = float(e2.get())
    area = length * width
    area_label.config(text=f"The area of the rectangle is: {area}")

l1 = Label(window,text="Enter the Length of the rectangle")
l1.pack()
e1 = Entry(window)
e1.pack()
l2 = Label(window, text="Enter the width of the recatngle")
l2.pack()
e2 = Entry(window)
e2.pack()
b1 = Button(window,text="Calculate", command=calc_area )
b1.pack()
area_label = Label(window,text="")
area_label.pack()
window.mainloop()