import time
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from util import createAndSet
from pygame import mixer

class PostureCheck(tk.Tk):
    global setTimer, stopTimer

    # init audio
    mixer.init()
    mixer.music.load("audio.mp3")

    def __init__(self):
        super().__init__()
        self.wm_title("Posture Check")

        self.geometry("300x250")

        # kinter vars
        self.hour = createAndSet("00")
        self.minute = createAndSet("00")
        self.second = createAndSet("00")

        self.started = False

        self._createEntries()
    
    def _createEntries(self):
        global hour, minute, second
        hourEntry = Entry(self, width=3, font=("Arial", 18, ""), textvariable=self.hour)
        hourEntry.place(x=90, y=40)

        minuteEntry = Entry(self, width=3, font=("Arial", 18, ""), textvariable=self.minute)
        minuteEntry.place(x=140, y=40)

        secondEntry = Entry(self, width=3, font=("Arial", 18, ""), textvariable=self.second)
        secondEntry.place(x=190, y=40)

        # buttons
        startButton = Button(self, text="Set Timer", command= lambda: setTimer(self))
        startButton.place(x = 70, y = 120)

        stopButton = Button(self, text="Stop Timer", command= lambda: stopTimer(self))
        stopButton.place(x = 180, y = 120)

    def setTimer(self):
        if self.started:
            messagebox.showinfo("Error", "Timer is already started")
            return
            
        try:
            self.temp = int(self.hour.get()) * 3600 + int(self.minute.get()) * 60 + int(self.second.get())
            orig = self.temp
        except:
            print("Improper values entered")

        self.started = True

        while self.started:
            mins,secs = divmod(self.temp, 60)
            hours = 0

            if mins > 60:
                hours, mins = divmod(mins, 60)
            
            self.hour.set("{0:2d}".format(hours))
            self.minute.set("{0:2d}".format(mins))
            self.second.set("{0:2d}".format(secs))
    
            self.update()
            time.sleep(1)
    
            if (self.temp == 0):
                self.started = True
                mixer.music.play()
                self.temp = orig
            
            self.temp -= 1

    def stopTimer(self):
        if not self.started:
            messagebox.showinfo("Error", "The timer isn't started.")
        
        self.started = False
        messagebox.showinfo("Posture Check", "Timer has been stopped.")

PostureCheck().mainloop()