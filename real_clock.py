# from tkinter import *
# import math
# import time
# window = Tk()
# w = 400
# h = 400
# canvas = Canvas(width = w, height = h)
# canvas.pack()
#
#
# def watch(hours,minutes, seconds):
#     canvas.create_oval(70,70,330,330, width = 2, fill = 'lightgreen')
#     canvas.create_oval(100,100,300,300, fill = 'white', width = 2)
#     for i in range(1,13):
#         angle = i * 30
#         length = 70
#         length1 = 100
#         x = 200 + length * math.sin(math.radians(angle))
#         y = 200 - length  * math.cos(math.radians(angle))
#         x1 = 200 + length1 * math.sin(math.radians(angle))
#         y1 = 200 - length1 * math.cos(math.radians(angle))
#         canvas.create_line(w//2,h//2 , x1,y1, fill = 'blue', width = 1)
#         canvas.create_line(w//2,h//2, x,y, fill = 'white')
#     # for i in range(1,61):
#     #     angle = i * 6
#     #     length = 90
#     #     length1 = 100
#     #     x = 200 + length * math.sin(math.radians(angle))
#     #     y = 200 - length * math.cos(math.radians(angle))
#     #     x1 = 200 + length1 * math.sin(math.radians(angle))
#     #     y1 = 200 - length1 * math.cos(math.radians(angle))
#     #     canvas.create_line(w // 2, h // 2, x1, y1, fill='black')
#     #     canvas.create_line(w // 2, h // 2, x, y, fill='white')
#
#
#
#     angle = seconds * 6
#     length = 90
#     x = 200 + length * math.sin(math.radians(angle))
#     y = 200 - length * math.cos(math.radians(angle))
#     canvas.create_line(w//2, h//2, x, y , fill = 'red', width = 2)
#
#     angle = minutes * 6 + seconds/60 * 6
#     length = 90
#     x = 200 + length * math.sin(math.radians(angle))
#     y = 200 - length * math.cos(math.radians(angle))
#     canvas.create_line(w//2, h//2, x, y, fill = 'black', width = 4)
#
#     angle = hours * 30 + minutes/60 * 30
#     length = 50
#     x = 200 + length * math.sin(math.radians(angle))
#     y = 200 - length * math.cos(math.radians(angle))
#     canvas.create_line(w // 2, h // 2, x, y, fill='green', width=6)
#
#
#     for i in range(1,13):
#         angle = i * 30
#         length = 115
#         a = 200 + length * math.sin(math.radians(angle))
#         b = 200 - length * math.cos(math.radians(angle))
#         canvas.create_text(a,b,text = i, font = 'freesansbold.ttf 15')
#     canvas.create_oval(w//2-5,h//2-5,w//2+5,h//2+5, fill = 'lightgreen', outline = 'lightgreen')
#
#
# while True:
#     canvas.delete('all')
#     hours, minutes, seconds = time.localtime()[3:6]
#     watch(hours,minutes, seconds)
#     canvas.update()
#     canvas.after(1000)
#
import tkinter
import math
import time

w = 400
h = 400
okno = tkinter.Tk()
canvas = tkinter.Canvas(okno, width = w, height = h, bg = 'white')
canvas.pack()

def clock(hours, minutes, seconds):
    canvas.create_oval(70,70 ,330,330, fill = 'black', width = 2)
    canvas.create_oval(100,100,300,300, fill = 'white', width = 2)

    for i in range(1,13):
        angle = i * 30
        length = 70
        length1 = 100
        x = 200 + length * math.sin(math.radians(angle))
        y = 200 - length * math.cos(math.radians(angle))
        x1 = 200 + length1 * math.sin(math.radians(angle))
        y1 = 200 - length1 * math.cos(math.radians(angle))
        canvas.create_line(w//2,h//2,x1,y1,fill = 'grey')
        canvas.create_line(w//2,h//2,x,y,fill = 'white')

    for i in range(1,13):
        angle = i * 30
        length = 115
        x = 200 + length * math.sin(math.radians(angle))
        y = 200 - length * math.cos(math.radians(angle))
        canvas.create_text(x,y, text = i, fill = 'pink')


    angle = seconds * 6
    length = 90
    x = 200 + length * math.sin(math.radians(angle))
    y = 200 - length * math.cos(math.radians(angle))
    canvas.create_line(w//2,h//2, x,y, fill = 'blue', width = 3)

    angle = minutes * 6 + seconds/60 * 6
    length = 70
    x = w//2 + length * math.sin(math.radians(angle))
    y = h//2 - length * math.cos(math.radians(angle))
    canvas.create_line(w//2,h//2, x,y, fill = 'green', width = 5)

    angle = hours * 30 + minutes/60 * 30
    length = 50
    x = w//2 + length * math.sin(math.radians(angle))
    y = h//2 - length * math.cos(math.radians(angle))
    canvas.create_line(w // 2, h // 2, x, y, fill='red', width=7)


while True:
    canvas.delete('all')
    hours,minutes,seconds = time.localtime()[3:6]
    clock(hours,minutes,seconds)
    canvas.update()
    canvas.after(1000)

okno.mainloop()