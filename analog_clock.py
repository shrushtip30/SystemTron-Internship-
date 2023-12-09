import tkinter as tk
import time
import math
window=tk.Tk()
window.geometry("960x960")
def update_clock():
    hours=int(time.strftime("%I"))
    minutes=int(time.strftime("%M"))
    seconds=int(time.strftime("%S"))

    seconds_x=seconds_hand_len*math.sin(math.radians(seconds*6))+center_x
    seconds_y=-1*seconds_hand_len*math.cos(math.radians(seconds*6))+center_y
    canvas.coords(seconds_hand,center_x,center_y,seconds_x,seconds_y)

    minutes_x=minutes_hand_len*math.sin(math.radians(minutes*6))+center_x
    minutes_y=-1*minutes_hand_len*math.cos(math.radians(minutes*6))+center_y
    canvas.coords(minutes_hand,center_x,center_y,minutes_x,minutes_y)

    hours_x=hours_hand_len*math.sin(math.radians(hours*30))+center_x
    hours_y=-1*hours_hand_len*math.cos(math.radians(hours*30))+center_y
    canvas.coords(hours_hand,center_x,center_y,hours_x,hours_y)

    window.after(1000,update_clock)
    
canvas=tk.Canvas(window,width=960,height=960,bg="black")
canvas.pack(expand=True,fill="both")

bg=tk.PhotoImage(file="download.png")
canvas.create_image(480,480,image=bg)

center_x=480
center_y=480
seconds_hand_len=60
minutes_hand_len=40
hours_hand_len=20

seconds_hand=canvas.create_line(480,480,480+seconds_hand_len,480+seconds_hand_len,width=1.5,fill="red")
minutes_hand=canvas.create_line(480,480,480+minutes_hand_len,480+minutes_hand_len,width=3,fill="grey")
hours_hand=canvas.create_line(480,480,480+hours_hand_len,480+hours_hand_len,width=5,fill="white")

update_clock()
window.mainloop()
