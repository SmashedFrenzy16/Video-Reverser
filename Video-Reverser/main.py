from tkinter import *
import cv2

root = Tk()

root.title("Video Reverser")


title_label = Label(
            root, fg="black", text="Video Reverser", font=("Arial", 48))

title_label.pack()

blank_label = Label(root, text="")

blank_label.pack()

root.mainloop()
