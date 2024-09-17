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

def execute():

    vid = cv2.VideoCapture(location_e.get())

    check, video = vid.read()

    frame_count = 0

    check = True

    frame_list = []

    while check == True:

        cv2.imshow(f"video_frame_{frame_count}", video)

        check, video = vid.read()

        frame_list.append(video)

        counter += 1

    frame_list.pop()

    for i in frame_list:

        cv2.imshow("Frame:", i)

        if cv2.waitKey(25) and 0xFF == ord("q"): 
            break

location_e.insert(0, "Enter in the full video path that you want to reverse")

location_button = Button(root, text="Enter", command=execute)

location_button.pack()

root.mainloop()
