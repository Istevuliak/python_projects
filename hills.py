import tkinter
import random
w= 800
h= 600
okno = tkinter.Tk()
canvas = tkinter.Canvas(okno, width = w, height =h, bg = 'lightblue')
canvas.pack()

def hill():
    hill = []
    direction = random.choice((1,-1))
    hill.append(0)
    hill.append(random.randint(200,400))
    peak = random.randint(100,600)
    for i in range(peak//10):
        new_hill = hill[-1] + direction * random.randint(0,5)
        hill.append(i*10)
        hill.append(new_hill)
    direction = -1 * direction
    for i in range(h-peak//10 +10):
        new_hill = hill[-1] + direction * random.randint(0,5)
        hill.append(i*10+peak)
        hill.append(new_hill)
    hill = [0,h] + hill + [w,h]
    colour = '#{:02x}0000'.format(random.randint(10,255))
    canvas.create_polygon(hill, fill = colour, outline = 'black')

def draw(event):
    canvas.delete('all')
    for i in range(10):
        hill()

canvas.bind_all('<space>',draw)
okno.mainloop()