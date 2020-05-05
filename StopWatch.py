from tkinter import *
from datetime import *


class StopWatch:
    temp_seconds = 0
    after_id = ""

    def __init__(self, main):
        self.labelWatch = Label(main, font=("Times New Roman", 100))
        self.buttonStart = Button(main, text="Start", font=("Times New Roman", 30), command=self.startSW)
        self.buttonStop = Button(main, text="Stop", font=("Times New Roman", 30), command=self.stopSW)
        self.buttonContinue = Button(main, text="Continue", font=("Times New Roman", 30), command=self.continueSW)
        self.buttonReset = Button(main, text="Reset", font=("Times New Roman", 30), command=self.resetSW)
        self.buttonExit = Button(main, text="Exit", font=("Times New Roman", 30), command=self.exitSW)

        self.labelWatch.grid(row=0, columnspan=2)
        self.labelWatch["text"] = "00:00"
        self.buttonStart.grid(row=1, columnspan=2)
        self.buttonExit.grid(row=2, columnspan=2)

    def tick(self):
        self.after_id = self.buttonStart.after(1000, self.tick)
        minutes_seconds = datetime.fromtimestamp(self.temp_seconds).strftime("%M:%S")
        self.labelWatch.configure(text=str(minutes_seconds))
        self.temp_seconds += 1

    def startSW(self):
        self.buttonStart.grid_forget()
        self.buttonStop.grid(row=1, columnspan=2)
        self.tick()

    def stopSW(self):
        self.labelWatch.after_cancel(self.after_id)
        self.buttonStop.grid_forget()
        self.buttonContinue.grid(row=1, column=0)
        self.buttonReset.grid(row=1, column=1)

    def continueSW(self):
        self.buttonContinue.grid_forget()
        self.buttonReset.grid_forget()
        self.buttonStop.grid(row=1, columnspan=2)
        self.tick()

    def resetSW(self):
        self.buttonContinue.grid_forget()
        self.buttonReset.grid_forget()
        self.labelWatch.configure(text="00:00")
        self.buttonStart.grid(row=1, columnspan=2)
        self.temp_seconds = 0

    def exitSW(self):
        self.buttonExit.quit()

root = Tk()
root.title("StopWatch v1.0")

sw = StopWatch(root)

root.mainloop()