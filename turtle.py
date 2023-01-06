import tkinter

height = 500
width = 500
okno = tkinter.Tk()

canvas = tkinter.Canvas(okno, height = height, width = width)
canvas.pack()

x = width/2
y = height/2

direction = 0
colour = 'black'

subor = open('korytnacka', 'r')
for i in subor:
    riadok = i.split()
    print(riadok)

    if 'line' in riadok:
        distance = int(riadok[1])
        if direction == 0:
            canvas.create_line(x,y,x,y-distance, fill = colour)
            y -= distance
        elif direction == 1:
            canvas.create_line(x,y,x-distance,y, fill = colour)
            x -= distance
        elif direction == 2:
            canvas.create_line(x,y,x,y+distance, fill = colour)
            y += distance
        elif direction == 3:
            canvas.create_line(x,y,x+distance, y, fill = colour)
            x += distance
    elif 'right' in riadok:
        direction = (direction + 1) % 4
    elif 'left' in riadok:
        direction = (direction - 1) % 4
    elif 'color' in riadok:
        colour = riadok[1]


okno.mainloop()

# use direction % 4 = never a negative number