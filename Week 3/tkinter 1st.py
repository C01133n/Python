from tkinter import *  
parent = Tk()  
redbutton = Button(parent, text = "Red", fg = "red")  
redbutton.pack( side = LEFT)  
greenbutton = Button(parent, text = "Black", fg = "black")  
greenbutton.pack( side = RIGHT )  
bluebutton = Button(parent, text = "Blue", fg = "blue")  
bluebutton.pack( side = TOP )  
blackbutton = Button(parent, text = "Green", fg = "green")  
blackbutton.pack( side = BOTTOM) 

parent.mainloop()
gui = Tk(className='Python Examples - Window Color')
gui.configure(bg='teal') 
gui.mainloop()

# Import the Tkinter library
from tkinter import *

# Create an instance of Tkinter window
window=Tk()

# Set the size of the window
window.geometry("300x300")

# Set the window background color
window.configure(bg="red")

#Uncomment below lines to use

# set the window background color using bg or background property
# window['bg'] = "#32a2a8"
# window['background'] = "#8732a8"

# Create a label widget
label=Label(window, text="Hello from Educative !!!").pack()

window.mainloop()