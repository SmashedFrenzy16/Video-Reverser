from tkinter import *
import cv2

root = Tk()

root.title("Video Reverser")


title_label = Label(
            root, fg="black", text="Video Reverser", font=("Arial", 48))

title_label.pack()

blank_label = Label(root, text="")

blank_label.pack()

location_e = Entry(root, width=100, borderwidth=5)

location_e.pack()

location_e.insert(0, "Enter in the full video path that you want to reverse")

location_button = Button(root, text="Enter", command=execute)

location_button.pack()

root.mainloop()
