# import tkinter as tk
# from tkinter import ttk
# from tkinter import Frame
# import PIL
# from PIL import Image, ImageTk
# import cv2

# white 		= "#ffffff"
# lightBlue2 	= "#adc5ed"
# font 		= "Constantia"
# fontButtons = (font, 12)
# maxWidth  	= 800
# maxHeight 	= 480

# #Graphics window
# mainWindow = tk.Tk()
# mainWindow.configure(bg=lightBlue2)
# mainWindow.geometry('%dx%d+%d+%d' % (maxWidth,maxHeight,0,0))
# mainWindow.resizable(0,0)
# # mainWindow.overrideredirect(1)

# mainFrame = Frame(mainWindow)
# mainFrame.place(x=20, y=20)                

# #Capture video frames
# lmain = tk.Label(mainFrame)
# lmain.grid(row=0, column=0)

# cap = cv2.VideoCapture('vint.avi')

# def show_frame():
# 	ret, frame = cap.read()
# 	cv2image   = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

# 	img   = Image.fromarray(cv2image).resize((500, 400))
# 	imgtk = ImageTk.PhotoImage(image = img)
# 	lmain.imgtk = imgtk
# 	lmain.configure(image=imgtk)
# 	lmain.after(1, show_frame)

# closeButton = tk.Button(mainWindow, text = "CLOSE", font = fontButtons, bg = white, width = 20, height= 1)
# closeButton.configure(command= lambda: mainWindow.destroy())              
# closeButton.place(x=270,y=430)	

# show_frame()  #Display
# mainWindow.mainloop()  #Starts GUI

# import tkinter
# import PIL
# from PIL import Image, ImageTk
# import cv2
# import time
# import io 
# import threading
# import os, sys
 
# class App:
#     def __init__(self, window, window_title, video_source=0):
#         self.window = window
#         self.window.title(window_title)
#         self.video_source = video_source

#         # open video source (by default this will try to open the computer webcam)
#         self.vid = MyVideoCapture(self.video_source)

#         # Create a canvas that can fit the above video source size
#         self.canvas = tkinter.Canvas(window, width = 500, height = 500)
#         self.canvas.pack()

#         # Button that lets the user take a snapshot
#         # self.btn_snapshot=tkinter.Button(window, text="Snapshot", width=50, command=self.snapshot)
#         # self.btn_snapshot.pack(anchor=tkinter.CENTER, expand=True)

#         # After it is called once, the update method will be automatically called every delay milliseconds
#         self.delay = 1
#         self.update()

#         self.window.mainloop()

#     def snapshot(self):
#         # Get a frame from the video source
#         ret, frame = self.vid.get_frame()

#         if ret:
#             cv2.imwrite("frame-" + time.strftime("%d-%m-%Y-%H-%M-%S") + ".jpg", cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY))

#     def update(self):
#         # Get a frame from the video source
#         ret, frame = self.vid.get_frame()

#         if ret:
#             self.photo = ImageTk.PhotoImage(image= Image.fromarray(frame).resize(760,400))
#             self.canvas.create_image(0, 0, image = self.photo, anchor = tkinter.NW)
            
#         self.window.after(self.delay, self.update)


# class MyVideoCapture:
#     def __init__(self, video_source=0):
#         # Open the video source
#         self.vid = cv2.VideoCapture(video_source)
#         if not self.vid.isOpened():
#             raise ValueError("Unable to open video source", video_source)

#         # Get video source width and height
#         self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
#         self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)

#     def get_frame(self):
#         # lmain = tk.label
#         # lmain = tk.Label()
#         if self.vid.isOpened():
#             ret, frame = self.vid.read()
#             if ret:
#                 # Return a boolean success flag and the current frame converted to BGR
#                 cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#                 # img = Image.fromarray(cv2image).resize((760,400))
#                 # imgtk = ImageTk.PhotoImage(image = img)
#                 # lmain.imgtk = imgtk 
#                 # lmain.configure(image=imgtk)

#                 return (ret, cv2image)
#             else:
#                 return (ret, None)
#         else:
#             return (ret, None)

#     # Release the video source when the object is destroyed
#     def __del__(self):
#         if self.vid.isOpened():
#             self.vid.release()

# # Create a window and pass it to the Application object
# App(tkinter.Tk(), "Tkinter and OpenCV","vint.avi")

import numpy
from pygame import mixer
import time
import cv2
from tkinter import *
from tkinter.ttk import Combobox
from PIL import Image, ImageTk
import io 
import threading
import os, sys

class MyVideoCapture:
    def intsrc(self, video_source='vint.avi'):
        # Open the video source
        self.vid = cv2.VideoCapture(video_source)
        if not self.vid.isOpened():
            raise ValueError("Unable to open video source", video_source)
  
        # Get video source width and height
        self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)
 
    # Release the video source when the object is destroyed
    def delsrc(self):
        if self.vid.isOpened():
            self.vid.release()
        self.window.mainloop()


    def load_video_frame(self):
        # cap = cv2.VideoCapture('vint.avi')
        # processed = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        if self.vid.isOpened():
            ret, frame = self.vid.read()
            if ret: 
                return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            else:
                return (ret, None)
        else:
            return (ret, None)

    # while rval: 
    #     rval, frame = cap.read()
    #     img = Image.fromarray(frame)
    #     #img = resize(img)
    #     imgtk = ImageTk.PhotoImage(img)
    #     #lbl.config(image=imgtk)
    #     #lbl.img = imgtk
    #     if stop_ == True: 
    #         cap.release()
    #         break 
    #     cv2.waitKey(1)
    # cap.release()

class root:
    def stop_():
        global stop
        stop = True

    def start_():
        stop_ = False
        t = threading.Thread(target=load_video_frame)
        t.start()

    self.geometry('800x580')
    self.title('AI-Drone GUI')
    siz = (200, 200)

    # ----- UPPER FRAME -----

    selVid_label = Label(root, text="Select video:",font=('helvetica 10'))
    selVid_label.place(relx = 0.1, rely = 0.05)

    v = ["Power Transmission 4600ft", "Power Transmission 5100ft"]
    selVid = Combobox(root, values=v)
    selVid.place(relx = 0.285, rely = 0.05)

    start_btn=Button(root,padx=5,pady=5,bg='white',fg='black',relief=GROOVE,text='START',font=('helvetica 10'), command=start_)
    start_btn.place(relwidth = 0.1, relheight = 0.05, relx = 0.650, rely = 0.0485)

    stop_btn=Button(root,padx=5,pady=5,bg='white',fg='black',relief=GROOVE,text='STOP',font=('helvetica 10'), command=stop_)
    stop_btn.place(relwidth = 0.1, relheight = 0.05, relx = 0.750, rely = 0.0485)

    # ----- LOWER FRAME -----
    rawVid_label = Label(root, text="Raw Video",font=('helvetica 10'))
    rawVid_label.place(relx = 0.1, rely = 0.4)

    # rawVidFrame = Frame(root)
    # rawVidFrame.place(relwidth = 0.07, relheight = 0.03, relx = 0.489, rely = 0.243)

    # ----- RIGHT LOWER FRAME -----
    procVid_label = Label(root, text="Processed Video",font=('helvetica 10'))
    procVid_label.place(relx = 0.500, rely = 0.4)

    # procVidFrame = Frame(root)
    # procVidFrame.place(relwidth = 0.07, relheight = 0.03, relx = 0.489, rely = 0.243)

    # cap.release()
    # cv2.close
    # cv2.destroyAllWindows()


    root.mainloop()
